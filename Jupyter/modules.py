import concurrent.futures
import multiprocessing
import os
import time
from io import BytesIO
from pathlib import Path

import numpy as np
import pandas as pd
import requests
from PIL import Image

save_path = Path(r"C:\Users\Brand\Documents\Branden's Stuff\Python\Machine Learning\PyTorch\bee_data")

class BusyBeeScraping:
    def __init__(self, dataset, cores) -> None:
        self.dataset = dataset
        self.cores = cores
    
    def k_split_bee_images(self, k: int) -> list[pd.DataFrame]:
        
        """Splits the dataset into k batches of data

        Returns:
            k (int): the number of batches of data
        """
        
        self.dataset = self.dataset[["image_url", "taxon_tribe_name"]]
        self.dataset = self.dataset[~self.dataset["taxon_tribe_name"].isnull()]
        
        return np.array_split(self.dataset, k)
    
    def scrape_bee_images(self, save_path: Path=save_path):
        """
        Iterates through the dataset to save it into the labeled folders
        Uses requests to get image content and PIL to convert the request content into an Image
        Saves the Image based on the tribe label name

        Args:
            save_path (Path): the save_path for where you want to store your data
            
        """
        
        total_img = len(self.dataset)
    
        epoch_div_time = time.time()
        for i in range(total_img): # set the 1000 for now, should be the size of the entire dataset
            try:
                image_url, image_label = self.dataset.iloc[i]
            

                response = requests.get(image_url)
                image = Image.open(BytesIO(response.content))
                
                image_save_path = save_path / image_label
                unique_index = len(os.listdir(image_save_path)) # variable to save index names
                
                try:
                    image.save(os.path.join(image_save_path, f"{image_label}_{unique_index + 1}.jpg"))
                except:
                    print("Image was RGBA, Converting to RGB Image...")
                    converted_image = image.convert('RGB')
                    converted_image.save(os.path.join(image_save_path, f"{image_label}_{unique_index + 1}.jpg"))
                
                if i % 100 == 0:
                    print(f"Image {i}: Total Run Time -> {time.time() - epoch_div_time}")
                    epoch_div_time = time.time()
                    
            except:
                print("Error 404: Failure to Access Image URL")
    
    def run(self, k: int=15):
        """Runs the scrapping application

        Args:
            k (int, optional): def. Defaults to 15.
        """
        
        start = time.perf_counter()
        
        dataframes = self.k_split_bee_images(k)
        
        with concurrent.futures.ProcessPoolExecutor() as executor:
            executor.map(self.scrape_bee_images, dataframes)
            
        end = time.perf_counter()
        print(f"Finished in {round((end-start) / 60, 2)} minutes(s)")
