# 🖼️ Simple Image Posterizer in Python

This is a small Python project that takes an input image and reduces the number of colors while optionally applying a custom color tint and adjustable contrast. The goal was simple — to experiment with posterization, color quantization, and basic image manipulation using **Pillow** and **NumPy**.  

This was never meant to be a large-scale image editor or professional tool — just a fun, educational script to play around with image processing. However, it can still give some surprisingly aesthetic results with the right parameters.

---

## ⚠️ Disclaimer

Before using this script:
- There’s **no GUI**, only a **CLI**.
- **Performance** depends on image size — larger images will take longer to process.
- There’s **no input validation**, so incorrect values might cause errors or crashes.
- The project will **not be actively developed further**, but the repository will remain open for anyone who wants to experiment, fork, or modify it.

---

## 🧠 Introduction

**Simple Image Posterizer** is a standalone Python script that lets you:
- Limit an image to a fixed number of colors.
- Optionally apply a **custom tint** (with RGB values you define).
- Adjust the **contrast** for a more stylized look.

It’s written entirely in Python using the **Pillow** and **NumPy** libraries, both of which are required to run the script.

---

## 📦 Installation

### Requirements

You’ll need:
- Python 3.8 or higher  
- Pillow (`pip install pillow`)  
- NumPy (`pip install numpy`)  

### How to run

1. Clone or download this repository.  
2. Open a terminal or command prompt inside the project folder.  
3. Run the script:

   ```bash
   python image-filter.py

---

## 🧪 Examples

### 🖼️ Input
![Input Image](./examples/input.png)

### 🎨 Output
![Output Image](./examples/output.png)

### ⚙️ Parameters Used
```bash
color_limit = 8
contrast = 1.5
mode = 2  # 1 = Default mode, 2 = Custom tint mode
tint_color = (255, 150, 0)
