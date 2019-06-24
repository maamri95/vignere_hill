import sys

from PyQt5.QtWidgets import QApplication

from interface import View

if __name__ == '__main__':
    application = QApplication(sys.argv)
    fenetrePrincipale = View()
    fenetrePrincipale.show()
    applicationExec = application.exec_()
    sys.exit(applicationExec)
