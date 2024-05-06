import io
import os
from PIL import Image
from rembg import remove

def convert_and_remove_bg(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):  # Check if the file is a JPG
            # Full path of the current file
            file_path = os.path.join(input_folder, filename)
            # Load the image
            with open(file_path, 'rb') as file:
                img_data = file.read()
                img_no_bg = remove(img_data)  # Remove background

            # Convert image to PNG
            img = Image.open(io.BytesIO(img_no_bg))
            # Creating PNG filename by replacing jpg with png
            png_filename = filename[:-4] + '.png'
            # Full path for the output file
            output_file_path = os.path.join(output_folder, png_filename)
            # Save the PNG image
            img.save(output_file_path, "PNG")

    print("Conversion and background removal completed.")

# Specify the input and output folders
input_folder = r""
output_folder = r""

# Call the function
convert_and_remove_bg(input_folder, output_folder)