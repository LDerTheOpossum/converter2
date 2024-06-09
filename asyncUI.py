import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from concurrent.futures import ThreadPoolExecutor
import threading

executor = ThreadPoolExecutor(max_workers=2)

class ConverterUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.lock = threading.Lock()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.label = QLabel("Select files to convert", self)
        self.layout.addWidget(self.label)

        self.openButton = QPushButton("Open File", self)
        self.openButton.clicked.connect(self.show_file_dialog)
        self.layout.addWidget(self.openButton)

        self.saveButton = QPushButton("Save As", self)
        self.saveButton.clicked.connect(self.save_file_dialog)
        self.layout.addWidget(self.saveButton)

        self.convertButton = QPushButton("Convert", self)
        self.convertButton.clicked.connect(self.convert)
        self.layout.addWidget(self.convertButton)

        self.setLayout(self.layout)

    def show_file_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;JSON Files (*.json);;YAML Files (*.yaml);;XML Files (*.xml)", options=options)
        if file_name:
            self.label.setText(file_name)
            self.input_file = file_name

    def save_file_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "All Files (*);;JSON Files (*.json);;YAML Files (*.yaml);;XML Files (*.xml)", options=options)
        if file_name:
            self.label.setText(file_name)
            self.output_file = file_name

    def convert(self):
        self.label.setText("Converting...")
        executor.submit(self.async_convert)

    def async_convert(self):
        with self.lock:
            convert(self.input_file, self.output_file)
        self.label.setText("Conversion Completed")

def main():
    app = QApplication(sys.argv)
    converter = ConverterUI()
    converter.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
