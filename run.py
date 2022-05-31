# 使用浅色主题
import sys
import PySide6
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow
from main_window import DrinkMainWindow

if __name__ == '__main__':
    # sys.modules["pyside2"] = PySide6
    # create the application and the main window
    app = QtWidgets.QApplication(sys.argv)
    QtWidgets.QApplication.setQuitOnLastWindowClosed(False)  # 关闭最后一个窗口不退出程序
    window = DrinkMainWindow()

    # setup stylesheet
    # app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=True))

    # run
    window.show()
    sys.exit(app.exec())
