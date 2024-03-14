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


class BusyBeeScraping:
    def __init__(self, dataset:pd.DataFrame) -> None:
        self.dataset = dataset[["image_url", "taxon_tribe_name"]]
        self.dataset = self.dataset[~self.dataset["taxon_tribe_name"].isnull()]
        
        self.save_path = Path(os.getcwd())
    
    def generate_dir(self) -> None:
        """
        Generates the directory structure to store the train and test data from our bee dataset

        Args:
            parent_dir (str): The path location of the parent directory
            file_structure (dict): a dictionary containing file structure 
            
        file_structure Example:
            
            {'data': ['Xylocopini', 'Bombini', 'Apini', 'Ammobatoidini', 'Megachilini',
                    'Eucerini', 'Emphorini', 'Anthidiini', 'Halictini', 'Anthophorini',
                    'Osmiini', 'Augochlorini', 'Sphecodini', 'Nomadini', 'Ceratinini',
                        nan, 'Epeolini', 'Protandrenini', 'Andrenini', 'Calliopsini',
                    'Panurgini', 'Caupolicanini', 'Melectini']),
            }
            
        """
        
        file_structure = self.dataset["taxon_tribe_name"].unique()
        
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)
        
        for file_types in file_structure:
            if not os.path.exists(self.save_path / str(file_types)):
                os.makedirs(self.save_path / str(file_types))
    
    def k_split_bee_images(self, k: int) -> list[pd.DataFrame]:
        
        """Splits the dataset into k batches of data

        Returns:
            k (int): the number of batches of data
        """
        
        return np.array_split(self.dataset, k)
    
    def scrape_bee_images(self, datasets):
        """
        Iterates through the dataset to save it into the labeled folders
        Uses requests to get image content and PIL to convert the request content into an Image
        Saves the Image based on the tribe label name

        Args:
            save_path (Path): the save_path for where you want to store your data
            
        """
        
        total_img = len(datasets)
    
        epoch_div_time = time.time()
        for i in range(total_img): # set the 1000 for now, should be the size of the entire dataset
            try:
                image_url, image_label = datasets.iloc[i]
            

                response = requests.get(image_url)
                image = Image.open(BytesIO(response.content))
                
                image_save_path = self.save_path / image_label
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
        
        self.generate_dir()
        dataframes = self.k_split_bee_images(k)
        
        with concurrent.futures.ProcessPoolExecutor() as executor:
            executor.map(self.scrape_bee_images, dataframes)
            
        end = time.perf_counter()
        print(f"Finished in {round((end-start) / 60, 2)} minutes(s)")

    def set_save_path(self, save_path: Path):
        """
        Sets save_path from user input if save_path 
        is not a valid folder/directory.
        
        Args:
            save_path (Path): the save_path for where you want to store your data
        """
        self.save_path = save_path
        
        while (not os.path.isdir(self.save_path)):
            print("Invalid path!")
            self.save_path = Path(str(input("Enter the path of where the data is to be stored: ")))
            

if __name__ == "__main__":
    data = pd.read_csv(r"C:\Users\Brand\Documents\Branden's Stuff\Python\BusyBee\Jupyter\se_us_data.csv")
    beeScrape = BusyBeeScraping(data)
    beeScrape.set_save_path(Path(r"C:\Users\Brand\Documents\Branden's Stuff\Python\BusyBee\Jupyter\data"))
    beeScrape.run()

