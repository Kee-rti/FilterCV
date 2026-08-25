# FilterCV

A real-time, interactive Computer Vision application that overlays dynamic Augmented Reality (AR) filters onto human faces, mimicking core features found in modern social media applications.

## Overview

This project leverages edge computing to perform real-time facial landmark detection and apply geometric transformations to 2D assets. It processes live webcam feeds locally, ensuring high performance (30+ FPS) and low latency without relying on cloud inference.

## Features

- **Real-Time Face Tracking:** Fast and robust face detection using a 468-point 3D face mesh.
- **Dynamic Asset Overlay:** Applies 2D assets (e.g., glasses, masks) that dynamically scale and rotate accurately according to facial movements.
- **Edge Computing Optimized:** Built to run efficiently on standard CPUs.

## Tech Stack

- **Python 3**
- **OpenCV:** For video capture, matrix transformations, and alpha blending.
- **Google MediaPipe:** For lightweight, real-time facial landmark inference.
- **NumPy:** For high-performance matrix operations and image array manipulation.

## Getting Started

*(Installation and usage instructions will be updated here as the project develops.)*
