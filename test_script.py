import os
import cv2


def check_image(file_path):
    """Check if an image file exists and can be opened."""
    if not os.path.exists(file_path):
        print(f"Image not found: {file_path}")
        return False
    
    image = cv2.imread(file_path)
    if image is None:
        print(f"Failed to load image: {file_path}")
        return False
    
    print(f"Image loaded successfully: {file_path}")
    return True


# Test image path (update this to match your setup)
image_path = 'Plaksha_Faculty.jpg'

if __name__ == "__main__":
    if check_image(image_path):
        print("Test passed: Image is present and valid.")
    else:
        print("Test failed: Image is missing or invalid.")