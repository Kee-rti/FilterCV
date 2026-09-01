# Development Log

This document tracks the chronological progress, architectural decisions, and key technical steps taken during the development of FilterCV.

## Initial Setup
- **Date**: August 27, 2026
- **Decision**: Initialized project structure (`src`, `docs`, `assets`).
- **Decision**: Selected OpenCV, MediaPipe, and NumPy as the core tech stack for real-time edge processing.
- **Action**: Created basic `main.py` for webcam capture testing.
- **Action**: Setup `requirements.txt` and `.gitignore`.

## Phase 2: Face Tracking Integration
- **Date**: August 28, 2026
- **Decision**: Integrated MediaPipe `FaceMesh` to get 468 3D facial landmarks in real-time. We configured `refine_landmarks=True` to enhance precision around the eyes and lips, crucial for accurate AR asset placement.
- **Action**: Modified `src/main.py` to convert BGR frames to RGB, run `FaceMesh.process()`, and overlay the mesh, contours, and irises using `drawing_utils`.

## Phase 3: 2D Asset Overlay
- **Date**: September 1, 2026
- **Decision**: Implemented an explicit alpha blending utility (`src/overlay_utils.py`) using OpenCV bitwise operations instead of simple binary masking, preserving semi-transparent pixels in AR assets.
- **Action**: Modified `src/main.py` to calculate facial rotation based on eye landmarks (indices 33 and 263) and position the glasses asset using the nose bridge (index 168) as the anchor point.
