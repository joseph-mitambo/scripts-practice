from PIL import Image
import os

# Function to process images
def process_image(input_path="images", output_path="/opt/icons", rotation_angle=90, target_size=(128, 128), output_format="JPEG"):
    # Open the image
    image = Image.open(input_path)

    # Rotate the image
    rotated_image = image.rotate(rotation_angle, expand=True)

    # Resize the image
    resized_image = rotated_image.resize(target_size)

    # Save the image
    resized_image.save(output_path, format=output_format)

# Directory containing images
input_directory = input_path

# Directory to save processed images
output_directory = output_path

# Create output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Process each image in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        input_path = os.path.join(input_directory, filename)
        output_path = os.path.join(output_directory, filename)

        # Process the image
        process_image(input_path, output_path)

print("Image processing complete.")
