# Module for processing and working with images

A PyQt5-based application for image processing that allows users to convert images to grayscale and move them to different folders. This GUI tool is user-friendly and provides a fixed-size window layout for easy image management.

## Screenshot
![Image Processor Interface](preview.png)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/artemventvent/production_practice_Mallenom.git
   cd production_practice_Mallenom
2. Install required packages:
   ```bash
   pip install -r requirements.txt
4. Run the application:
   ```bash
   python main.py

## Usage
1. Browse for an Image: Click the "__Browse__" button to select an image file.
2. Convert to Grayscale: Click the "__Convert to Grayscale__" button to process the image.
3. Move Image: Click the "__Move Image__" button to select a folder where the image will be moved.
4. The converted grayscale image will be saved in the same directory as the original image.

## Requirements
- Python 3.7+
- PyQt5
- Pillow (PIL)
