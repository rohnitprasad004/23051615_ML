import cv2
import os

# Step 1: Define folders
input_folder = "images"
output_folder = "processed"

# Step 2: Loop through all images
for image_file in os.listdir(input_folder):

    # Only process images
    if image_file.endswith((".jpg", ".png", ".jpeg")):
        
        img_path = os.path.join(input_folder, image_file)
        img = cv2.imread(img_path)

        if img is None:
            print(f"Could not load {image_file}. Skipping...")
            continue

        # Step 3: Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Step 4: Save processed image
        output_path = os.path.join(output_folder, f"gray_{image_file}")
        cv2.imwrite(output_path, gray)

        print(f"Processed and saved: {output_path}")

print("\nAll images processed successfully!")
