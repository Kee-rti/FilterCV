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
