from PIL import Image
import os

def convert_webp_to_jpg(source_folder, output_folder):
    # Create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the source folder
    for filename in os.listdir(source_folder):
        if filename.endswith('.webp'):
            # Construct the full file path
            webp_path = os.path.join(source_folder, filename)
            # Open the .webp image file
            with Image.open(webp_path) as img:
                # Define the output file path, change extension to .jpg
                jpg_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.jpg')
                # Convert the image to RGB mode and save it as a .jpg
                img.convert('RGB').save(jpg_path, 'jpeg')

    print(f"All .webp images from {source_folder} have been converted to .jpg in {output_folder}")

# Example usage
source_folder = r""
output_folder = r""
convert_webp_to_jpg(source_folder, output_folder)