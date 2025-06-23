# 🖋️ Generate Text & Delete Animation Video

This Python script creates a writing-and-deleting animation video from a list of sentences using OpenCV. Each sentence is animated as if being typed out, paused, and then erased — useful for visual presentations, educational videos, or simulation demos.

## 📽️ Demo Output

The script generates:

* A series of **PNG image frames** simulating the typing and deletion effect.
* A compiled **MP4 video** (`writing_animation.mp4`) showing the full animation.

---

## 📁 Project Structure

```
.
├── generate_text_delete_video.py   # Main script
├── frames/                         # Auto-generated folder with image frames
└── writing_animation.mp4          # Output video file
```

---

## 🚀 Features

* ⏱️ Adjustable frame rate (FPS)
* ✍️ Typing effect with configurable font size and frame size
* ⏹️ Pause between typing and deleting
* 🧹 Automatic cleanup/rewrite of frames directory

---

## 🛠️ Requirements

* Python 3.x
* OpenCV
* NumPy

### Install dependencies:

```bash
pip install opencv-python numpy
```

---

## 🧾 Usage

### Run the script:

```bash
python generate_text_delete_video.py
```

### Output:

* Frames saved in the `frames/` directory.
* Final video saved as `writing_animation.mp4`.

---

## ⚙️ Configuration Options

You can change the following parameters in the script:

```python
sentences = [
    "Generate a Polycrystal RVE . . .",
    "Generate a Fiber Reinforced Concrete RVE . . .",
    "Generate a Multiscale Woven Fabric Model  . . .",
    "Generate a Ballistic Impact Model . . ."
]

frame_output_dir = "frames"         # Folder to save image frames
video_output_file = "writing_animation.mp4"
fps = 30                            # Frames per second
font_size = 20                      # Font size for the text
frame_size = (500, 100)            # Width x Height of each frame
```

---

## 📦 Example Use Cases

* Tutorial video intros
* Simulation text visualizations
* Research or education content
* UI/UX demos for text interactions

