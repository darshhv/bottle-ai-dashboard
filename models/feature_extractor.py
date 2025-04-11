import cv2
import numpy as np

def extract_features(image_path):
    """
    Extracts basic visual features from a bottle image using edge detection.

    Args:
        image_path (str): Path to the image file.

    Returns:
        dict: Extracted features such as dimensions and edge count.
    """
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Edge detection
    edges = cv2.Canny(gray, 100, 200)
    
    # Get image dimensions
    height, width = gray.shape

    # Count non-zero pixels (edges)
    edge_count = np.count_nonzero(edges)

    return {
        "Width (px)": width,
        "Height (px)": height,
        "Edge Pixels": edge_count,
        "Aspect Ratio": round(width / height, 2)
    }
