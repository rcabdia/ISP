import os

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QMainWindow, QPushButton

from isp import ROOT_DIR
from isp.Gui.Frames import FilesView, BaseFrame
from isp.Gui.Frames.qt_components import Pagination


class MyMainWindow(QMainWindow):

    def __init__(self, parent=None):

        super(MyMainWindow, self).__init__(parent)
        self.form_widget = FormWidget(self)
        print("Main = ", self.form_widget.layout())
        self.setCentralWidget(self.form_widget)


class FormWidget(QWidget):

    def __init__(self, parent):
        super(FormWidget, self).__init__(parent)
        self.vbl = QVBoxLayout(self)
        self.setLayout(self.vbl)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        print("Init FormWidget")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    root = os.path.join(ROOT_DIR, "260", "RAW")
    main = MyMainWindow()
    # w = FilesView(root, main.form_widget)
    p = Pagination(main.form_widget, 6)
    p.bind_onItemPerPageChange_callback(lambda v: print("Item per page changed to {}".format(v)))
    p.bind_onPage_changed(lambda v: print("Page changed to {}".format(v)))

    main.show()
    sys.exit(app.exec_())
