import os
from PIL import Image, ExifTags

# Maximum allowed dimension
MAX_DIMENSION = 900

# Directory containing the images
IMAGE_DIR = "."  # You can change this to a specific path

def apply_exif_orientation(image):
    try:
        exif = image._getexif()
        if exif is not None:
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break
            orientation_value = exif.get(orientation, None)

            if orientation_value == 3:
                image = image.rotate(180, expand=True)
            elif orientation_value == 6:
                image = image.rotate(270, expand=True)
            elif orientation_value == 8:
                image = image.rotate(90, expand=True)
    except Exception as e:
        print(f"Warning: Could not apply EXIF orientation: {e}")
    return image

def resize_image(image_path):
    try:
        with Image.open(image_path) as img:
            img = apply_exif_orientation(img)
            width, height = img.size

            if width <= MAX_DIMENSION and height <= MAX_DIMENSION:
                print(f"Skipping {image_path}, already small enough.")
                return

            # Compute new size maintaining aspect ratio
            scale = min(MAX_DIMENSION / width, MAX_DIMENSION / height)
            new_size = (int(width * scale), int(height * scale))
            resized_img = img.resize(new_size, Image.ANTIALIAS)
            resized_img.save(image_path)
            print(f"Resized {image_path} to {new_size}")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def main():
    for filename in os.listdir(IMAGE_DIR):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff")):
            image_path = os.path.join(IMAGE_DIR, filename)
            resize_image(image_path)

if __name__ == "__main__":
    main()
