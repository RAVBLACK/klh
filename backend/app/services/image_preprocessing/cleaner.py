"""
Image Preprocessing - Cleaner
Image cleaning and enhancement
"""

import cv2
import numpy as np


class ImageCleaner:
    """Clean and preprocess invoice images"""
    
    def __init__(self):
        pass
    
    def clean(self, image: np.ndarray) -> np.ndarray:
        """
        Clean and enhance image
        - Remove noise
        - Adjust brightness/contrast
        - Deskew
        """
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Denoise
        denoised = cv2.fastNlMeansDenoising(gray)
        
        # Adaptive threshold
        binary = cv2.adaptiveThreshold(
            denoised, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY, 11, 2
        )
        
        return binary
    
    def resize(self, image: np.ndarray, max_width: int = 1024) -> np.ndarray:
        """Resize image to optimal OCR size"""
        height, width = image.shape[:2]
        
        if width > max_width:
            ratio = max_width / width
            new_height = int(height * ratio)
            resized = cv2.resize(image, (max_width, new_height))
            return resized
        
        return image
