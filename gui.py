from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QComboBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from data_fetcher import fetch_stock_data, fetch_historical_data
from predictor import prepare_data, build_model, predict_stock
from visualizer import plot_data

class StockTrackerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI-Driven Stock Tracker")
        self.setGeometry(100, 100, 800, 600)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.stock_selector = QComboBox()
        self.stock_selector.addItems(["AAPL", "GOOGL", "AMZN", "MSFT"])
        layout.addWidget(self.stock_selector)

        self.fetch_button = QPushButton("Fetch Data")
        self.fetch_button.clicked.connect(self.fetch_data)
        layout.addWidget(self.fetch_button)

        self.predict_button = QPushButton("Predict Stock")
        self.predict_button.clicked.connect(self.predict_data)
        layout.addWidget(self.predict_button)

        self.figure = Figure()
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def fetch_data(self):
        symbol = self.stock_selector.currentText()
        data = fetch_historical_data(symbol)
        # Extract and process data to plot
        self.ax.clear()
        self.ax.plot([1, 2, 3], [100, 105, 110], label="Historical Data")  # Example
        self.ax.legend()
        self.canvas.draw()

    def predict_data(self):
        # Example: Update with ML prediction logic
        self.ax.clear()
        self.ax.plot([1, 2, 3], [110, 115, 120], label="Predicted Data")  # Example
        self.ax.legend()
        self.canvas.draw()
