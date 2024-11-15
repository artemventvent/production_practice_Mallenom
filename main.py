import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PIL import Image

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Processor")
        self.setFixedSize(1200, 900)  # Фиксированный размер окна

        # Основной горизонтальный макет
        main_layout = QHBoxLayout()

        # Левая панель (путь, кнопки)
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(20, 20, 20, 20)
        left_layout.setSpacing(15)

        # Поле для ввода пути
        self.path_input = QLineEdit()
        self.path_input.setPlaceholderText("Enter image path here")
        self.path_input.setFixedWidth(300)
        left_layout.addWidget(self.path_input)

        # Кнопка для выбора файла
        self.browse_button = QPushButton("Browse")
        self.browse_button.setFixedWidth(300)
        self.browse_button.clicked.connect(self.browse_image)
        left_layout.addWidget(self.browse_button)

        # Кнопка для конвертации изображения
        self.process_button = QPushButton("Convert to Grayscale")
        self.process_button.setFixedWidth(300)
        self.process_button.clicked.connect(self.convert_to_grayscale)
        left_layout.addWidget(self.process_button)

        # Кнопка для перемещения изображения
        self.move_button = QPushButton("Move Image")
        self.move_button.setFixedWidth(300)
        self.move_button.clicked.connect(self.move_image)
        left_layout.addWidget(self.move_button)

        # Заполняем оставшееся пространство
        left_layout.addStretch()

        # Правая панель (изображение)
        self.image_label = QLabel()
        self.image_label.setFixedSize(800, 800)  # Размер области изображения
        self.image_label.setAlignment(Qt.AlignCenter)

        # Добавляем левую и правую панели в основной макет
        main_layout.addLayout(left_layout)
        main_layout.addWidget(self.image_label)

        # Устанавливаем основной макет
        self.setLayout(main_layout)

    # Получаем путь к файлу через диалог
    def browse_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.xpm *.jpg)")
        if file_path:
            self.path_input.setText(file_path)
            self.display_image(file_path)

    def display_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio))

    # Делаем чб
    def convert_to_grayscale(self):
        image_path = self.path_input.text()
        if not image_path or not os.path.exists(image_path):
            QMessageBox.warning(self, "Warning", "Please select a valid image file.")
            return
        try:
            img = Image.open(image_path).convert('L')
            grayscale_path = os.path.splitext(image_path)[0] + '_grayscale.png'
            img.save(grayscale_path)
            self.display_image(grayscale_path)
            QMessageBox.information(self, "Success", f"Grayscale image saved as {grayscale_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to convert image: {e}")

    # Перемещение файла
    def move_image(self):
        image_path = self.path_input.text()
        if not image_path or not os.path.exists(image_path):
            QMessageBox.warning(self, "Warning", "Please select a valid image file.")
            return
        new_dir = QFileDialog.getExistingDirectory(self, "Select Destination Folder")
        if new_dir:
            try:
                new_path = os.path.join(new_dir, os.path.basename(image_path))
                os.rename(image_path, new_path)
                QMessageBox.information(self, "Success", f"Image moved to {new_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not move image: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
