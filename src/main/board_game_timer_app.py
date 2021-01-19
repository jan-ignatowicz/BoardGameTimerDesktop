"""The BoardGameTimer runner"""

import sys
from PyQt5.QtWidgets import QApplication
# https://stackoverflow.com/questions/56726580/no-name-qapplication-in-module-pyqt5-qtwidgets-error-in-pylint

from src.main.window.bgt_main import BgtMain

from src.main.db import init_database as init_db

if __name__ == "__main__":
    init_db.init_database()

    app = QApplication(sys.argv)
    bgtd_app = BgtMain()
    bgtd_app.show()
    sys.exit(app.exec_())
