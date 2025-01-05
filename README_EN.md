# Hand Detection Project

This is a Python application that detects and visualizes hand movements in real-time camera footage.

## Features

- Real-time hand detection
- Hand skeleton visualization
- Blue dot markers for fingertips
- Multiple hand support (can detect up to 2 hands simultaneously)

## Requirements

- Python 3.10 or higher
- OpenCV (`opencv-python`)
- MediaPipe
- NumPy

## Installation

1. Install the required libraries:
```bash
pip install -r requirements.txt
```

2. Run the program:
```bash
python3 main.py
```

## Usage

- When the program starts, the camera view will open
- Show your hands to the camera
- The program will automatically detect and mark your hands
- Press 'q' to exit the program

## Notes

- Good lighting conditions are required for optimal performance
- Make sure camera permissions are granted
- The program can detect up to 2 hands simultaneously

## License

This project is licensed under the MIT License. 