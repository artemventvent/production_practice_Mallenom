from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QFileDialog, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from image_processing import convert_to_grayscale
from file_utils import move_file
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Processor")
        self.setFixedSize(1200, 900)

        main_layout = QHBoxLayout()

        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(20, 20, 20, 20)
        left_layout.setSpacing(15)

        self.path_input = QLineEdit()
        self.path_input.setPlaceholderText("Enter image path here")
        self.path_input.setFixedWidth(300)
        left_layout.addWidget(self.path_input)

        self.browse_button = QPushButton("Browse")
        self.browse_button.setFixedWidth(300)
        self.browse_button.clicked.connect(self.browse_image)
        left_layout.addWidget(self.browse_button)

        self.process_button = QPushButton("Convert to Grayscale")
        self.process_button.setFixedWidth(300)
        self.process_button.clicked.connect(self.handle_grayscale)
        left_layout.addWidget(self.process_button)

        self.move_button = QPushButton("Move Image")
        self.move_button.setFixedWidth(300)
        self.move_button.clicked.connect(self.handle_move)
        left_layout.addWidget(self.move_button)

        left_layout.addStretch()

        self.image_label = QLabel()
        self.image_label.setFixedSize(800, 800)
        self.image_label.setAlignment(Qt.AlignCenter)

        main_layout.addLayout(left_layout)
        main_layout.addWidget(self.image_label)

        self.setLayout(main_layout)

    def browse_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.xpm *.jpg)")
        if file_path:
            self.path_input.setText(file_path)
            self.display_image(file_path)

    def display_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio))

    def handle_grayscale(self):
        image_path = self.path_input.text()
        if not image_path or not os.path.exists(image_path):
            QMessageBox.warning(self, "Warning", "Please select a valid image file.")
            return
        try:
            grayscale_path = convert_to_grayscale(image_path)
            self.display_image(grayscale_path)
            QMessageBox.information(self, "Success", f"Grayscale image saved as {grayscale_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to convert image: {e}")

    def handle_move(self):
        image_path = self.path_input.text()
        if not image_path or not os.path.exists(image_path):
            QMessageBox.warning(self, "Warning", "Please select a valid image file.")
            return
        new_dir = QFileDialog.getExistingDirectory(self, "Select Destination Folder")
        if new_dir:
            try:
                new_path = move_file(image_path, new_dir)
                QMessageBox.information(self, "Success", f"Image moved to {new_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not move image: {e}")