from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QListWidget, QLabel, QLineEdit, QComboBox
from PyQt5.QtCore import Qt

class WorkfileManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('3ds Max Workfile Manager')
        self.setGeometry(100, 100, 800, 600)

        main_layout = QVBoxLayout()

        self.file_combobox = QComboBox()
        self.file_combobox.currentIndexChanged.connect(self.show_file_info)
        main_layout.addWidget(self.file_combobox)

        self.file_info = QLabel("Select a file to view details")
        main_layout.addWidget(self.file_info)

        self.add_button = QPushButton('Add File')
        self.add_button.clicked.connect(self.add_file)
        main_layout.addWidget(self.add_button)

        self.update_button = QPushButton('Update File')
        self.update_button.clicked.connect(self.update_file)
        main_layout.addWidget(self.update_button)

        self.delete_button = QPushButton('Delete File')
        self.delete_button.clicked.connect(self.delete_file)
        main_layout.addWidget(self.delete_button)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.load_files()

    def load_files(self):
        self.file_combobox.clear()
        data = load_data()
        for item in data:
            self.file_combobox.addItem(item['file_name'])

    def show_file_info(self):
        file_name = self.file_combobox.currentText()
        data = load_data()
        for file in data:
            if file['file_name'] == file_name:
                self.file_info.setText(
                    f"File Name: {file['file_name']}\n"
                    f"Creation Date: {file['creation_date']}\n"
                    f"Modification Date: {file['modification_date']}\n"
                    f"Version: {file['version']}\n"
                    f"Tags: {', '.join(file['tags'])}"
                )
                break

    def add_file(self):
        # Logic to add file
        pass

    def update_file(self):
        # Logic to update file
        pass

    def delete_file(self):
        # Logic to delete file
        pass

if __name__ == '__main__':
    app = QApplication([])
    manager = WorkfileManager()
    manager.show()
    app.exec_()
