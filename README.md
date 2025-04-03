# FacialRecoSys

## Overview

**FacialRecoSys** is a face authentication system using OpenCV and LBPH (Local Binary Patterns Histograms). The system captures face samples, trains a recognizer, and performs real-time authentication with voice feedback.

## Features

-   Face detection using Haar Cascade.
-   Face recognition with LBPHFaceRecognizer.
-   Voice-based authentication confirmation.
-   User-friendly interface with on-screen messages.
-   Automatic dataset generation and model training.

## Installation

1.  Clone the repository:

    ```sh
    git clone [https://github.com/yourusername/FacialRecoSys.git](https://github.com/yourusername/FacialRecoSys.git)
    cd FacialRecoSys
    ```

2.  Create a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # On Windows use: venv\Scripts\activate
    ```

3. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Download the Haar Cascade XML file for face detection (if not included):

    ```sh
    wget [https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml) -P engine/auth/
    ```

## Usage

1.  Capture face samples:

    ```sh
    python src/capture_face.py
    ```

2.  Train the face recognition model:

    ```sh
    python src/train_model.py
    ```

3.  Run the authentication system:

    ```sh
    python src/authenticate.py
    ```

The system will open the webcam and display a message: "Authentication in process..."

-   If a registered face is detected, it will display the name and say "You are authenticated."
-   If the face is unknown, it will display "Unknown" and deny authentication.

## Project Structure

```bash
FacialRecoSys/
├── engine/
│   ├── auth/
│   │   ├── haarcascade_frontalface_default.xml
│   │   ├── trainer.yml
│   │   ├── samples/  # Stores captured face images
├── src/
│   ├── capture_face.py
│   ├── train_model.py
│   ├── authenticate.py
├── requirements.txt
├── README.md