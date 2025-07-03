# 3D Color Map Visualizer (CPU + GPU)

A Python tool to visualize the distribution of an image's pixels in 3D color space (RGB or HSV).  
Supports both:
- CPU rendering via `matplotlib` (static 3D plot)
- GPU rendering via `VisPy` (interactive)

## Features

- Supports RGB and HSV color space mapping
- Sample pixel subset for performance
- Interactive GPU view with mouse drag/zoom/rotate
- Optimized for Intel and Apple Silicon (M1/M2/M3) Macs

---

## CLI Options

<table>
  <thead>
    <tr>
      <th>Option</th>
      <th>Required</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>--img</code></td>
      <td>Path to input image file</td>
      <td><code>--img ./img/photo.jpg</code></td>
    </tr>
    <tr>
      <td><code>--samplesize</code></td>
      <td>Number of pixels to sample (default: <code>5000</code>)</td>
      <td><code>--samplesize 10000</code></td>
    </tr>
    <tr>
      <td><code>--mode</code></td>
      <td>Color space to visualize (<code>rgb</code> or <code>hsv</code>)</td>
      <td><code>--mode hsv</code></td>
    </tr>
    <tr>
      <td><code>--chip</code></td>
      <td>Rendering method: <code>cpu</code> (matplotlib) or <code>gpu</code> (VisPy)</td>
      <td><code>--chip gpu</code></td>
    </tr>
  </tbody>
</table>

---

## CPU Example (Matplotlib)

Displays a static 3D scatter plot using sampled pixels.

> ![matplotlib Screenshot](/matplotlib.png)  

---

## GPU Example (VisPy)

Displays an interactive 3D color map rendered via OpenGL.  

> ![VisPy Screenshot](/VisPy.png)  

---
## Requirements

    •	Python 3.8–3.12
	•	numpy
	•	opencv-python
	•	matplotlib
	•	vispy
	•	PyQt5 (or PySide2)

---

## Usage

To install requirements via pip:

```bash
pip install numpy opencv-python matplotlib vispy PyQt5

```
To run the program:

```bash
python3 colormapgpu.py --img path/to/image.jpg --mode rgb --chip gpu