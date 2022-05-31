# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(649, 127)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.drink_button = QRadioButton(self.frame)
        self.drink_button.setObjectName(u"drink_button")
        self.drink_button.setStyleSheet(u"QRadioButton{\n"
"    border-radius:8px;\n"
"}\n"
"QRadioButton::indicator {\n"
"	font: 700 12pt \"Microsoft YaHei UI\";\n"
"    width: 0px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton::indicator:disabled{\n"
"    background-color: #7f8c8d;\n"
"    color: white\n"
"}\n"
"QRadioButton::checked{\n"
"    background-color: #7f8c8d;\n"
"    color: white\n"
"}\n"
"QRadioButton:hover:checked{\n"
"    background-color: #7f8c8d;\n"
"    color: white\n"
"}\n"
"QRadioButton:hover{\n"
"    background-color: #bdc3c7;\n"
"    color: white\n"
"}")

        self.verticalLayout.addWidget(self.drink_button)

        self.class_button = QRadioButton(self.frame)
        self.class_button.setObjectName(u"class_button")
        self.class_button.setStyleSheet(u"QRadioButton{\n"
"    border-radius:8px;\n"
"}\n"
"QRadioButton::indicator {\n"
"	font: 700 12pt \"Microsoft YaHei UI\";\n"
"    width: 0px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton::indicator:disabled{\n"
"    background-color: #7f8c8d;\n"
"    color: white\n"
"}\n"
"QRadioButton::checked{\n"
"    background-color: #7f8c8d;\n"
"    color: white\n"
"}\n"
"QRadioButton:hover:checked{\n"
"    background-color: #7f8c8d;\n"
"    color: white\n"
"}\n"
"QRadioButton:hover{\n"
"    background-color: #bdc3c7;\n"
"    color: white\n"
"}")

        self.verticalLayout.addWidget(self.class_button)

        self.setting_button = QRadioButton(self.frame)
        self.setting_button.setObjectName(u"setting_button")
        self.setting_button.setStyleSheet(u"QRadioButton{\n"
"    border-radius:8px;\n"
"}\n"
"QRadioButton::indicator {\n"
"	font: 700 12pt \"Microsoft YaHei UI\";\n"
"    width: 0px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton::indicator:disabled{\n"
"    background-color: #7f8c8d;\n"
"    color: white\n"
"}\n"
"QRadioButton::checked{\n"
"    background-color: #7f8c8d;\n"
"    color: white\n"
"}\n"
"QRadioButton:hover:checked{\n"
"    background-color: #7f8c8d;\n"
"    color: white\n"
"}\n"
"QRadioButton:hover{\n"
"    background-color: #bdc3c7;\n"
"    color: white\n"
"}")

        self.verticalLayout.addWidget(self.setting_button)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(5)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.drink_page = QWidget()
        self.drink_page.setObjectName(u"drink_page")
        self.horizontalLayout_3 = QHBoxLayout(self.drink_page)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.label = QLabel(self.drink_page)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.drink_interval = QLineEdit(self.drink_page)
        self.drink_interval.setObjectName(u"drink_interval")

        self.horizontalLayout_3.addWidget(self.drink_interval)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.drink_on = QCheckBox(self.drink_page)
        self.drink_on.setObjectName(u"drink_on")

        self.horizontalLayout_3.addWidget(self.drink_on)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.drink_words = QPushButton(self.drink_page)
        self.drink_words.setObjectName(u"drink_words")

        self.horizontalLayout_3.addWidget(self.drink_words)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.stackedWidget.addWidget(self.drink_page)
        self.setting_page = QWidget()
        self.setting_page.setObjectName(u"setting_page")
        self.gridLayout_2 = QGridLayout(self.setting_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.submit_title = QPushButton(self.setting_page)
        self.submit_title.setObjectName(u"submit_title")

        self.gridLayout_2.addWidget(self.submit_title, 0, 3, 1, 1)

        self.label_3 = QLabel(self.setting_page)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_10, 0, 5, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_11, 0, 4, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_9, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.setting_page)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 0, 2, 1, 1)

        self.if_start_on_boot = QCheckBox(self.setting_page)
        self.if_start_on_boot.setObjectName(u"if_start_on_boot")

        self.gridLayout_2.addWidget(self.if_start_on_boot, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.setting_page)
        self.class_page = QWidget()
        self.class_page.setObjectName(u"class_page")
        self.gridLayout = QGridLayout(self.class_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 0, 6, 1, 1)

        self.class_on_notify = QCheckBox(self.class_page)
        self.class_on_notify.setObjectName(u"class_on_notify")

        self.gridLayout.addWidget(self.class_on_notify, 0, 1, 1, 1)

        self.label_2 = QLabel(self.class_page)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)

        self.import_class = QPushButton(self.class_page)
        self.import_class.setObjectName(u"import_class")

        self.gridLayout.addWidget(self.import_class, 1, 1, 1, 2)

        self.add_class = QPushButton(self.class_page)
        self.add_class.setObjectName(u"add_class")

        self.gridLayout.addWidget(self.add_class, 1, 3, 1, 2)

        self.class_off_notify = QCheckBox(self.class_page)
        self.class_off_notify.setObjectName(u"class_off_notify")

        self.gridLayout.addWidget(self.class_off_notify, 0, 2, 1, 2)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 1, 5, 1, 1)

        self.class_notify_before = QLineEdit(self.class_page)
        self.class_notify_before.setObjectName(u"class_notify_before")

        self.gridLayout.addWidget(self.class_notify_before, 0, 5, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 0, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.class_page)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 649, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.drink_button.setText(QCoreApplication.translate("MainWindow", u"\u559d\u6c34", None))
        self.class_button.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u8bfe", None))
        self.setting_button.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u559d\u6c34\u63d0\u9192\u95f4\u9694\u65f6\u95f4(\u79d2)", None))
        self.drink_on.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f ", None))
        self.drink_words.setText(QCoreApplication.translate("MainWindow", u"\u8bcd\u5e93", None))
        self.submit_title.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u4fee\u6539", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u6807\u9898\u540d\u79f0", None))
        self.if_start_on_boot.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u673a\u81ea\u542f", None))
        self.class_on_notify.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u8bfe\u63d0\u9192 ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u524d\u63d0\u9192\u65f6\u95f4(\u5206) ", None))
        self.import_class.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u8bfe\u7a0b", None))
        self.add_class.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u8bfe\u7a0b", None))
        self.class_off_notify.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8bfe\u63d0\u9192 ", None))
    # retranslateUi

