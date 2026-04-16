import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
import os

def extract_palette(image_paths, num_colors=5):
    pixels=[]

    for img_path in image_paths:
        img=Image.open(img_path).convert("RGB")
        img=img.resize((100,100))
        pixel_array=np.array(img).reshape(-1,3)
        pixels.append(pixel_array)

    pixels=np.vstack(pixels)

    print("Extracting color palette...")
    kmeans=KMeans(n_clusters=num_colors, random_state=42)
    kmeans.fit(pixels)

    colors = kmeans.cluster_centers_.astype(int)
    palette=[tuple(color) for color in colors]
    print("Color palette extracted:", palette)

    return palette