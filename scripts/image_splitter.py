import os
import numpy as np
import shutil

# Define the directories
data_dir = r"C:\Users\Brand\Downloads"
image_dir = data_dir + r"\Bombini"


class Image_Splitter:
    
    def __init__(self, image_dir) -> None:
        self.imgs = [filename for filename in os.listdir(image_dir) if filename.endswith(".jpg")]
    
    def __len__(self) -> int:
        return len(self.imgs)
    
    # Create split_images method
    def split_by_k(self, name, k: int=2) -> None:
        """
        Splits the images into k equal sections and places them into directories

        Args:
            k (int, optional): _description_. Defaults to 2.
        """
        split_image_files = np.array_split(self.imgs, k)
        
        for i, image_file in enumerate(split_image_files):
            image_save_path = data_dir + f"\{name}_{i + 1}"
            if not os.path.exists(image_save_path):
                os.makedirs(image_save_path)
            
            for img in image_file:
                image_path = os.path.join(image_dir, img)
                shutil.move(image_path, image_save_path)

    def split_by_percentage(self, name, percentage: float = 0.5) -> None:
        """
        Splits the images into percentage groups and places them into directories

        Args:
            percentages (list, optional): a list of percentages. Defaults to [0.5, 0.5].
        """
        
        
        split_image_files = [int(self.imgs[0: len(self.imgs)] * percentage)], self.imgs[int(len(self.imgs) * percentage): len(self.imgs)]]
        
        for i, image_file in enumerate(split_image_files):
            image_save_path = data_dir + f"\{name}_{i + 1}"
            
            if not os.path.exists(image_save_path):
                os.makedirs(image_save_path)
            for img in image_file:
                image_path = os.path.join(image_dir, img)
                shutil.move(image_path, image_save_path)
                
    def split_by_quantity(self, name, amt):
        """_summary_

        Args:
            name (_type_): _description_
            amt (_type_): _description_
        """
        split_image_files = [self.imgs[0: amt], self.imgs[amt: len(self.imgs)]]
        
        for i, image_file in enumerate(split_image_files):
            image_save_path = data_dir + f"\{name}_{i + 1}"
            
            if not os.path.exists(image_save_path):
                os.makedirs(image_save_path)
                
            for img in image_file:
                image_path = os.path.join(image_dir, img)
                shutil.move(image_path, image_save_path)

if __name__ == "__main__":
    img_splitter = Image_Splitter(image_dir)
    img_splitter.split_by_quantity("Bombini", 8000)