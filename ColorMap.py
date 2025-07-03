"""
3D Color Mapping

Displays an image's pixel distribution in RGB or HSV color space
using either a CPU-based matplotlib plot or a GPU-accelerated VisPy view.

Usage:
    python3 colormapgpu.py --img path/to/image.jpg --mode rgb --chip gpu

Options:
    --mode: 'rgb' or 'hsv'
    --chip: 'cpu' for matplotlib, 'gpu' for interactive OpenGL (VisPy)
    --samplesize: Optional. Number of pixels to sample (default: 5000)

Note:
- GPU mode uses OpenGL via VisPy for real-time 3D rendering.
- CPU mode is better for quick static plots or low-resource systems.
"""

import argparse
import numpy as np
import cv2 as cv
from vispy import scene, app
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_color_map(image_path, sample_size, mode, chip):
    #input validation
    img = cv.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Could not load image: {image_path}")
    
    sample_size = int(sample_size) if sample_size else 5000

    mode_map = {"rgb": cv.COLOR_BGR2RGB,
                "hsv": cv.COLOR_BGR2HSV}
    if mode not in mode_map:
        raise ValueError(f"Unsupported mode: {mode}. Choose 'rgb' or 'hsv'.")
    
    #opencv image processing
    img_converted = cv.cvtColor(img, mode_map[mode])
    pixels = img_converted.reshape(-1, 3)
    
    if len(pixels) > sample_size:
        idx = np.random.choice(len(pixels), sample_size, replace=False)
        pixels = pixels[idx]

    x, y, z = pixels[:, 0 ], pixels[:, 1], pixels[:, 2]
    colors = pixels / 255.0


    if chip == "cpu":
        r, g, b = cv.split(img_converted)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(r.flatten(), g.flatten(), b.flatten(), 
                c=img_converted.reshape(-1, 3)/255.0, s=1)
        
        ax.set_xlabel('Red')
        ax.set_ylabel('Green')
        ax.set_zlabel('Blue')

        plt.show()

    elif chip == "gpu":
        #add GPU-rendered interactive 3d canvas (drag-to-rotate)
        canvas = scene.SceneCanvas(keys='interactive', show=True, bgcolor='black', 
                                title='3D Color Map')
        view = canvas.central_widget.add_view()
        view.camera = 'turntable' 

        scatter = scene.visuals.Markers()
        scatter.set_data(np.stack([x, y, z], axis = -1), face_color=colors, size= 5, edge_width = 0)
        view.add(scatter)

        #labels
        axis = scene.visuals.XYZAxis(parent = view.scene)
        canvas.app.run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="3D color Map using VisPy")
    parser.add_argument("--img", required=True, help="Path to image")
    parser.add_argument("--samplesize", required=False, help="Number of pixels to sample")
    parser.add_argument("--mode", required=True, choices=['rgb', 'hsv'],
                        help="Choose color space to map")
    parser.add_argument("--chip", required=True, choices=["cpu", "gpu"], 
                        help="Choose to run on CPU or GPU")
    args = parser.parse_args()

    visualize_color_map(args.img, args.samplesize, args.mode, args.chip)
