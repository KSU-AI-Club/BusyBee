import os
import shutil
import random

# Define the directories
data_dir = "../data/se_us_bee_data/total/"
image_dir = data_dir + "images/"
text_dir = data_dir + "labels/"
img_val_dir = data_dir + "images/val/"
txt_val_dir = data_dir + "labels/val/"

# Create validation directories if it doesn't exist
if not os.path.exists(img_val_dir):
    os.makedirs(img_val_dir)
if not os.path.exists(txt_val_dir):
    os.makedirs(txt_val_dir)

# Get a list of all image files
image_files = [filename for filename in os.listdir(image_dir) if filename.endswith(".jpg")]

# Calculate the number of files to move
num_files_to_move = int(len(image_files) * 0.2)

# Select random files to move
files_to_move = random.sample(image_files, num_files_to_move)

# Move selected files and their associated text files to validation directory
for file_to_move in files_to_move:
    image_path = os.path.join(image_dir, file_to_move)
    text_path = os.path.join(text_dir, file_to_move.replace(".jpg", ".txt"))
    
    validation_image_path = os.path.join(img_val_dir, file_to_move)
    validation_text_path = os.path.join(txt_val_dir, file_to_move.replace(".jpg", ".txt"))
    
    shutil.move(image_path, validation_image_path)
    shutil.move(text_path, validation_text_path)
    
    print(f"Moved {file_to_move} and its associated text file to validation directory.")

