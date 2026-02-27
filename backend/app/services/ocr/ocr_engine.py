"""
OCR Engine
Text extraction from images
"""

import pytesseract
from typing import Dict, List
import cv2
import numpy as np


class OCREngine:
    """Extract text from invoice images"""
    
    def __init__(self):
        # Configure Tesseract
        self.config = r'--oem 3 --psm 6'
    
    def extract_text(self, image: np.ndarray) -> str:
        """Extract raw text from image"""
        text = pytesseract.image_to_string(image, config=self.config)
        return text
    
    def extract_with_boxes(self, image: np.ndarray) -> List[Dict]:
        """Extract text with bounding boxes"""
        data = pytesseract.image_to_data(
            image, output_type=pytesseract.Output.DICT
        )
        
        results = []
        for i in range(len(data['text'])):
            if int(data['conf'][i]) > 0:
                results.append({
                    'text': data['text'][i],
                    'confidence': data['conf'][i],
                    'x': data['left'][i],
                    'y': data['top'][i],
                    'width': data['width'][i],
                    'height': data['height'][i]
                })
        
        return results
    
    def extract_structured(self, image: np.ndarray) -> Dict:
        """Extract structured data from invoice"""
        text = self.extract_text(image)
        boxes = self.extract_with_boxes(image)
        
        return {
            'raw_text': text,
            'boxes': boxes
        }
