import sys
from PySide2.QtWidgets import QApplication, QLabel
from pyguitest import MyFun

if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel(MyFun())
    label.show()
    sys.exit(app.exec_())
