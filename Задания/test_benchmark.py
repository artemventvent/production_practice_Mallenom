import time
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow
from image_processing import convert_to_grayscale
from file_utils import move_file
import os
import shutil

# Тестовые данные
TEST_IMAGE_PATH = "test_image.jpg"
TEST_DIR = "test_dir"
GRAYSCALE_IMAGE_PATH = "test_image_grayscale.png"

# Создание тестовых файлов и директорий
def setup_environment():
    if not os.path.exists(TEST_IMAGE_PATH):
        # Создаем пустое изображение, если его нет
        from PIL import Image
        img = Image.new('RGB', (100, 100), color='white')
        img.save(TEST_IMAGE_PATH)
    
    if not os.path.exists(TEST_DIR):
        os.mkdir(TEST_DIR)

# Удаление тестовой среды
def cleanup_environment():
    if os.path.exists(TEST_IMAGE_PATH):
        os.remove(TEST_IMAGE_PATH)
    if os.path.exists(GRAYSCALE_IMAGE_PATH):
        os.remove(GRAYSCALE_IMAGE_PATH)
    if os.path.exists(TEST_DIR):
        shutil.rmtree(TEST_DIR)

# Замеры выполнения
def benchmark():
    setup_environment()
    try:
        # 1. Инициализация QApplication
        app = QApplication([])

        # 2. Измеряем время создания окна
        start_time = time.time()
        window = MainWindow()
        gui_time = time.time() - start_time

        # 3. Измеряем время конвертации в градации серого
        start_time = time.time()
        convert_to_grayscale(TEST_IMAGE_PATH)
        processing_time = time.time() - start_time

        # 4. Измеряем время перемещения файла
        start_time = time.time()
        move_file(TEST_IMAGE_PATH, TEST_DIR)
        move_time = time.time() - start_time

        # 5. Суммарное время
        total_time = gui_time + processing_time + move_time

        # Вывод результатов
        print(f"GUI Initialization Time: {gui_time:.4f} seconds")
        print(f"Image Processing Time: {processing_time:.4f} seconds")
        print(f"File Moving Time: {move_time:.4f} seconds")
        print(f"Total Time: {total_time:.4f} seconds")

    finally:
        cleanup_environment()

# Запуск замеров
if __name__ == "__main__":
    benchmark()
