# 🔍 Object Detection Web App

A **Streamlit**-based web application for real-time object detection on uploaded images, powered by **YOLOv5** weights and the **Ultralytics** inference pipeline. Upload one or more images, tune the confidence threshold, and get bounding-box visualizations along with a structured detection results table — all in the browser.

---

## ✨ Features

- 📤 **Multi-image upload** — process multiple PNG/JPG/JPEG files in a single run
- 🎚️ **Adjustable confidence threshold** — interactive slider (0.0 – 1.0, default 0.4)
- 📊 **Detection results table** — per-image DataFrame showing detected classes, bounding boxes, and confidence scores
- 🖼️ **Annotated output images** — YOLO-rendered images with bounding boxes displayed in the UI
- 🔄 **Reset button** — clears the `runs/` output directory with one click
- 📐 **Auto-resize** — images are resized to 640×640 before inference for consistent model input

---

## 🛠️ Tech Stack

| Component | Library / Tool |
|---|---|
| Web UI | [Streamlit](https://streamlit.io/) |
| Object Detection Model | YOLOv5 (`yolov5s.pt`) |
| Inference Backend | [Ultralytics](https://github.com/ultralytics/ultralytics) `8.2.34` |
| Deep Learning | PyTorch `2.3.1` + Torchvision `0.18.1` |
| Image Processing | OpenCV (headless), Pillow |
| Data Handling | NumPy, Pandas |

---

## 📁 Project Structure

```
object-detection-web/
├── app.py                  # Main Streamlit application
├── yolov5s.pt              # Pre-trained YOLOv5s weights
├── requirements.txt        # Python dependencies
├── modules/
│   ├── load_model.py       # Detect class — loads model & runs inference
│   └── get_image.py        # GetImage class — reads output images from runs/
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/pan-k15/object-detection-web.git
cd object-detection-web
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> **Note:** PyTorch `2.3.1` is included in `requirements.txt`. If you want GPU acceleration, install the CUDA-compatible version of PyTorch separately from [pytorch.org](https://pytorch.org/get-started/locally/) before running pip install.

### 4. Run the app

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`.

---

## 📋 Usage

1. Use the **confidence slider** to set the detection threshold (lower = more detections, higher = stricter).
2. Click **"Upload Images"** and select one or more image files.
3. Each image is displayed at preview size, followed by a **results DataFrame** showing detected objects.
4. Scroll down to the **Detection** section to see annotated output images with bounding boxes.
5. Click **Reset** to clear all saved detection outputs from the `runs/` directory.

---

## ⚠️ Notes

- The model weights `yolov5s.pt` are committed to the repository — no separate download required.
- Detection outputs are saved by YOLO to `runs/detect/` and read back by `GetImage` for display.
- The app uses `opencv-python-headless`, so no display environment (GUI) is needed on the server.
- Requires Python 3.8+.

---

## 📄 License

This project is open source. Feel free to fork and extend.

---

## 👤 Author

**Pan** — [github.com/pan-k15](https://github.com/pan-k15)
