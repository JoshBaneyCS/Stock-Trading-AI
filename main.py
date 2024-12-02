from PyQt5.QtWidgets import QApplication
from gui import StockTrackerApp
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StockTrackerApp()
    window.show()
    sys.exit(app.exec_())
