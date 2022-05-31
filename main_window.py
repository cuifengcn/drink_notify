# coding:utf-8
import sys
import time
import datetime as dt
from random import choice
from functools import partial
import copy
import PySide6.QtGui
from threading import Thread
from PySide6.QtWidgets import (QPushButton, QMainWindow, QSystemTrayIcon, QMenu, QMessageBox, QDialog, QTableWidgetItem,
                               QWidget, QLayout, QHBoxLayout)
from PySide6.QtGui import QPixmap, QIcon, QAction, QIntValidator
from PySide6.QtCore import QThreadPool, QByteArray, QTimer, Signal, QCoreApplication, QSize, QSettings
from ui_main import Ui_MainWindow
from mysetting import Constant, SettingClass, load_setting
from ui_drink_words_table import Ui_dialog as D_W_WIN


class DrinkWordsWin(QDialog, D_W_WIN):
    def __init__(self):
        super(DrinkWordsWin, self).__init__()
        self.setupUi(self)
        self.tableWidget.setColumnWidth(0, 300)
        self.tableWidget.setColumnWidth(1, 100)
        self.pushButton.clicked.connect(self.add_word)
        self.flush()

    def add_word(self):
        word = self.lineEdit.text()
        if not word:
            return
        if word not in SettingClass.drink_words:
            SettingClass.drink_words.append(word)
            self.flush()
            self.lineEdit.clear()

    def delete_word(self, word):
        for i in range(self.tableWidget.rowCount()):
            print(self.tableWidget.item(i, 0).text())
            if self.tableWidget.item(i, 0).text() == word:
                self.tableWidget.removeRow(i)
                SettingClass.drink_words.remove(word)
                return

    def delete_button(self, word):
        _widget = QWidget()
        _layout = QHBoxLayout()
        _layout.setSpacing(0)
        _layout.setContentsMargins(0, 0, 0, 0)
        b = QPushButton("删除")
        b.setFixedSize(QSize(80, 25))
        b.clicked.connect(partial(self.delete_word, word))
        _layout.addWidget(b)
        _widget.setLayout(_layout)
        return _widget

    def flush(self):
        n = self.tableWidget.rowCount()
        words = copy.copy(SettingClass.drink_words)
        for i in range(n, len(words), 1):
            self.tableWidget.insertRow(i)
            _item = QTableWidgetItem(words[i])
            _item.setToolTip(words[i])
            self.tableWidget.setItem(i, 0, _item)
            _button_widget = self.delete_button(words[i])
            self.tableWidget.setCellWidget(i, 1, _button_widget)


class DrinkMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(DrinkMainWindow, self).__init__()
        self.setupUi(self)
        load_setting()
        self.exited = False
        self.setting = SettingClass
        self.setWindowTitle(self.setting.title)
        self.drink_interval.setText(str(self.setting.drink_notify_interval))
        self.drink_on.setChecked(self.setting.drink_open)
        pixmap = QPixmap()
        pixmap.loadFromData(QByteArray.fromBase64(Constant.icon))
        self.icon = QIcon(pixmap)
        self.setWindowIcon(self.icon)
        self.stackedWidget.setCurrentWidget(self.drink_page)
        self.drink_button.setChecked(True)
        self.drink_button.clicked.connect(lambda: self.change_main_page(self.drink_page))
        self.class_button.clicked.connect(lambda: self.change_main_page(self.class_page))
        self.setting_button.clicked.connect(lambda: self.change_main_page(self.setting_page))
        self.drink_on.stateChanged.connect(self.drink_on_changed)
        num_vali = QIntValidator(10, 100000)
        self.drink_interval.setValidator(num_vali)
        self.drink_interval.textEdited.connect(self.drink_edit_line_conn)
        self.drink_words.clicked.connect(lambda: self.show_window(DrinkWordsWin, "_drink_words_win"))
        self.start_on_boot_setting = QSettings(Constant.RUN_PATH, QSettings.NativeFormat)
        self.if_start_on_boot.setChecked(self.start_on_boot_setting.contains("drink_notify"))
        self.if_start_on_boot.clicked.connect(self.on_boot_start)

        self.submit_title.clicked.connect(self.change_title)

        self.openAction = QAction("打开", self)
        self.openAction.setIcon(QIcon.fromTheme("media-record"))
        self.quitAction = QAction("退出", self)
        self.quitAction.setIcon(QIcon.fromTheme("application-exit"))  # 从系统主题获取图标
        self.quitAction.triggered.connect(self.quitApp)
        self.openAction.triggered.connect(self.openApp)
        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.addAction(self.openAction)
        self.trayIconMenu.addAction(self.quitAction)

        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)
        self.trayIcon.setIcon(self.icon)
        self.trayIcon.setToolTip(self.setting.title)
        self.trayIcon.show()
        self.trayIcon.setProperty("title", "test")
        self.trayIcon.activated[QSystemTrayIcon.ActivationReason].connect(self.iconActivated)

        self.drink_thread = DrinkThread(self,
                                        interval=self.setting.drink_notify_interval,
                                        words=self.setting.drink_words,
                                        init_on=self.setting.drink_open)

    def change_main_page(self, w):
        self.stackedWidget.setCurrentWidget(w)

    def change_title(self, checked):
        _text = self.lineEdit.text()
        if _text:
            self.setWindowTitle(_text)
            self.setting.title = _text
            self.setting.save()

    def closeEvent(self, event):
        # 右上角的X
        if self.trayIcon.isVisible():
            if not self.setting.min_notified and not self.exited:
                QMessageBox.information(
                    self, "系统托盘", "程序将继续在系统托盘中运行。要终止该程序，请在系统托盘条目的上下文菜单中选择[退出]。")
                self.setting.min_notified = True

    def quitApp(self):
        # 关闭软件
        self.exited = True  # 为了不跳出最小化提示
        QCoreApplication.quit()

    def openApp(self):
        # 显示界面
        self.showNormal()

    def iconActivated(self, reason):
        # 说及托盘图标可以展示隐藏
        if reason == QSystemTrayIcon.DoubleClick:
            if self.isHidden():
                self.show()
            else:
                self.hide()

    def drink_on_changed(self, state):
        # 是否开启饮水
        if state == 0:
            # 未被选中
            self.setting.drink_open = False
            self.setting.save()
            self.drink_thread.off()
        elif state == 2:
            # 被选中
            if not self.drink_interval.text():
                self.drink_interval.setText(str(self.setting.drink_notify_interval))
            self.setting.drink_open = True
            self.setting.save()
            self.drink_thread.on()

    def drink_popup_notify(self, title, word):
        self.trayIcon.showMessage(title, word, self.icon, 200)

    def drink_edit_line_conn(self, checked):
        if checked:
            _interval = int(float(checked))
            self.setting.drink_notify_interval = _interval
            self.drink_thread.update(interval=_interval)
            self.setting.save()

    def show_window(self, win, win_name):
        _win = getattr(self, win_name, None)
        if _win is None:
            setattr(self, win_name, win())
            _win = getattr(self, win_name)
        else:
            _win.flush()
        _win.show()

    def on_boot_start(self, checked):
        if checked:
            self.start_on_boot_setting.setValue("drink_notify", sys.argv[0])
        else:
            self.start_on_boot_setting.remove("drink_notify")


class DrinkThread:
    def __init__(self, master, interval, words, init_on):
        self.master = master
        self.interval = interval
        self.words = words
        self.last_notify_time = dt.datetime.now()
        self.running = True
        self.notify = init_on
        self.thread = Thread(target=self.run, daemon=True, name="drink_thread")
        self.thread.start()

    def on(self):
        self.notify = True

    def off(self):
        self.notify = False

    def update(self, interval=None, words=None):
        if interval is not None:
            self.interval = interval
        if words is not None:
            self.words = words

    def run(self):
        while self.running:
            if self.notify:
                now = dt.datetime.now()
                if (now - self.last_notify_time).total_seconds() >= self.interval:
                    if self.words:
                        self.master.drink_popup_notify("喝水提示", choice(self.words))
                        self.last_notify_time = now
            time.sleep(1)
