import os

print("Running script")
# Define the directory path
directory = "../data/se_us_bee_data/total/"

img_dir = directory + "images/"
label_dir = directory + "labels/"

# Get a list of all image files
image_files = [filename for filename in os.listdir(img_dir) if filename.endswith(".jpg")]

# Iterate through the image files and check if the corresponding text file exists
for image_file in image_files:
    text_file = os.path.join(label_dir, image_file.replace(".jpg", ".txt")) 
    if not os.path.exists(text_file):
        # For imputation here we're going to just remove the image
        # We know every image contains a bee, but if the annotator model did not find it 
        # we don't want it to drag down the performance of our prod model
        print(image_file + " has no accompanying text file. Deleting...")
        os.remove(os.path.join(img_dir, image_file))

