import os
from PIL import Image

def convert_to_yolo_format(image_dir, annotation_dir, output_dir):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all the annotation files
    annotation_files = [f for f in os.listdir(annotation_dir) if f.endswith('.txt')]

    for annotation_file in annotation_files:
        # Get the corresponding image file (assuming the same name but different extension)
        image_file = annotation_file.replace('.txt', '.jpg')  # Assuming the image extension is .jpg
        image_path = os.path.join(image_dir, image_file)
        
        # Open the image and get its dimensions
        with Image.open(image_path) as img:
            image_width, image_height = img.size

        # Open the corresponding annotation file
        annotation_path = os.path.join(annotation_dir, annotation_file)
        with open(annotation_path, 'r') as f:
            lines = f.readlines()

        # Open the output file to save YOLO annotations
        output_path = os.path.join(output_dir, annotation_file)
        with open(output_path, 'w') as f:
            for line in lines:
                
                try:
                  parts = list(map(float, line.strip().split(',')))
                except ValueError:
                  print(f"Skipping line due to ValueError: {line.strip()}")
                  continue

                # Extract coordinates and class ID
                class_id = int(parts[4])
                x_min = parts[0]
                y_min = parts[1]
                width = parts[2]
                height = parts[3]

                # Calculate the YOLO format values (normalized)
                x_center = (x_min + width / 2) / image_width
                y_center = (y_min + height / 2) / image_height
                width_normalized = width / image_width
                height_normalized = height / image_height

                # Write the YOLO annotation line
                f.write(f"{class_id} {x_center} {y_center} {width_normalized} {height_normalized}\n")


# Example usage
image_dir = "./images"  # Directory containing the images
annotation_dir = "./annotations"  # Directory containing the VisDrone annotations
output_dir = "./output_annotations"  # Output directory for YOLO annotations

convert_to_yolo_format(image_dir, annotation_dir, output_dir)
