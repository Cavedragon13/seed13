from PIL import Image
import os

input_dir = 'Images'        # Folder with your original images
output_dir = 'thumbnails'   # Folder to save thumbnails
os.makedirs(output_dir, exist_ok=True)

max_size = (220, 160)       # Max width and height for thumbnails

for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(input_dir, filename)
        img = Image.open(img_path)
        img.thumbnail(max_size)  # This preserves aspect ratio
        thumb_path = os.path.join(output_dir, filename)
        img.save(thumb_path)
        print(f"Saved thumbnail: {thumb_path}")