import math
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.cuda as cuda
from torch.utils.data import DataLoader
import os
import time
from torchvision import datasets, transforms
import torch.optim as optim
from torch.optim.lr_scheduler import StepLR
from tqdm.notebook import tqdm
import matplotlib.pyplot as plt
from PIL import Image
# %matplotlib inline
# Use Nvidia GPU if available, for faster results
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")         

# How can we allow for varying hyperparameters within an experiment? 
# Abstracting to hyperparameter class throws strange bugs

class training_statistics:
    model_names = [] 
    train_dl = None 
    test_dl = None
    loss_dict = {}
    accuracy_dict = {}
    time_to_train_dict = {}
    test_accuracy_dict = {}
    num_epochs = None
    batch_size = None
    lr = None
    gamma = None
    
    
    def __init__(self, model_names, num_epochs, batch_size, lr, gamma):
        self.model_names = model_names
        self.num_epochs = num_epochs
        self.batch_size = batch_size
        self.lr = lr
        self.gamma = gamma
        
    def plot_loss(self):
        # Background Loss
        plt.figure(figsize=(20,10))
        for model in self.model_names:
            loss_list = self.loss_dict.get(model)
            plt.plot(loss_list, label=model)

        plt.xticks(range(0,epochs), labels=range(1,epochs+1))
        plt.grid(True)
        plt.xlabel("Epoch", fontsize=14)
        plt.ylabel("Loss (Cross Entropy)", fontsize=14)
        plt.title("Training Loss Convergence", fontsize=16)
        plt.legend()

        plt.show()

    def chart_accuracy(self):
        # Final Training Accuracy
        acc_list = []
        #colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive']
        for model in self.model_names:
            acc_list.append(self.test_accuracy_dict.get(model))

        plt.figure(figsize=(20,10))
        plt.bar(models, acc_list)#, color=colors)
        plt.xlabel("Models")
        plt.ylabel("Accuracy (Percentage Points)")
        plt.title("Accuracy Comparison of Vision Transformer Variants")
        plt.show()

    def chart_train_time(self):
        # Training Time
        times_list = []
        for model in self.model_names:
            times_list.append(self.time_to_train_dict[model])
    
        plt.figure(figsize=(20, 10))
        plt.bar(models, times_list, color=colors)
        plt.xlabel("Models")
        plt.ylabel("Training Time (per Example)")
        plt.title("Training Time Comparison of Vision Transformer Variants")
        plt.show()

    def train_model(self, model, name):
        # Loss Function
        criterion = nn.CrossEntropyLoss()
        # Optimizer
        optimizer = optim.Adam(model.parameters(), lr=self.lr)
        # Scheduler
        scheduler = StepLR(optimizer, step_size=1, gamma=self.gamma)
        
        print("")
        print("++++++++++++++++++++++++++++++++++++++++")
        print(f"Training Run [Model: {name}]")
        print("++++++++++++++++++++++++++++++++++++++++")

        # Training Statistics Init
        loss_list = []
        accuracy_list = []
    
        # Training Time
        start_event = cuda.Event(enable_timing=True)
        end_event = cuda.Event(enable_timing=True)
        # Begin Clock
        start_event.record()
    
        # Training Loop
        for epoch in range(self.num_epochs):
            epoch_loss = 0
            epoch_accuracy = 0
        
            for data, label in tqdm(self.train_dl):
                data = data.to(device) # Ensure we're processing data on GPU
                label = label.to(device)
        
                output = model(data)
                loss = criterion(output, label)
        
                optimizer.zero_grad() # Zero out the gradient -- we'll experience weird bugs if we forget to do so
                loss.backward()
                optimizer.step()
        
                acc = (output.argmax(dim=1) == label).float().mean()
                epoch_accuracy += acc / len(self.train_dl)
                epoch_loss += loss / len(self.train_dl)
        
            print(f"Epoch: {epoch+1} - loss: {epoch_loss:.4f} - acc: {epoch_accuracy:.4f}")
            loss_list.append(epoch_loss.cpu().detach().numpy().item())
            accuracy_list.append(epoch_accuracy.cpu().detach().numpy().item())
       
        # End Clock
        end_event.record()
        cuda.synchronize() # Wait for GPU operations to complete
        time = start_event.elapsed_time(end_event) / 1000 # Convert to seconds
        num_examples = self.batch_size * len(self.train_dl)
        time_per_example = time / (num_examples * self.num_epochs)
        print(f"It took {time} seconds to train {name} on {num_examples} examples over {self.num_epochs} epochs.")
        print(f"That averages to {time_per_example} seconds per example")

        # Test run
        print("++++++++++++++++++++++++++++++++++++++++")
        print(f"Test Run [Model: {name}] ")
        print("++++++++++++++++++++++++++++++++++++++++")
        accuracies = []
        batch_acc = 0
        for data, label in tqdm(self.test_dl):
            data = data.to(device)
            label = label.to(device)
            output = model(data)
            acc = (output.argmax(dim=1) == label).float().mean().cpu().detach().numpy()
            batch_acc += acc / len(self.test_dl)
            accuracies.append(batch_acc)
        
        print(f"Test Accuracy: {accuracies[-1]} - Number of test cases: {len(self.test_dl) * self.batch_size}")

        # Update training stats
        self.loss_dict.update({name: loss_list})
        self.accuracy_dict.update({name: accuracy_list})
        self.time_to_train_dict.update({name: time_per_example})
        self.test_accuracy_dict.update({name: accuracies[-1]})

    def load_data(self, dataset_path, transform):
        seed = 2147483647
        # We'll use a PyTorch Generator to make things repeatable (deterministic)
        g = torch.Generator().manual_seed(seed)
    
        # Load Datasets with labels
        dset = datasets.ImageFolder(dataset_path, transform=transform) # Automatially assigns labels to examples based on the directory name

        # Generate 2 splits: Train (80%), Test (20%)
        dset_size = len(dset)
        train_size = int(0.8 * dset_size)
        test_size = dset_size - train_size

             #split dataset into 5 pieces 
        splitindex_1 = [dset_size/5] #split after fifth of dataset
        splitindex_2 = [2 * dset_size/5] #split after 2/5
        splitindex_3 = [3 * dset_size/5] #split after 3/5
        splitindex_4 = [4 * dset_size/5] #split after 4/5

        subset1 = torch.utils.data.Subset(dset,indices = range(0,splitindex_1))
        subset2 = torch.utils.data.Subset(dset,indices = range(splitindex_1,splitindex_2))
        subset3 = torch.utils.data.Subset(dset,indices = range(splitindex_2,splitindex_3))
        subset4 = torch.utils.data.Subset(dset,indices = range(splitindex_3,splitindex_4))
        subset5 = torch.utils.data.Subset(dset,indices = range(splitindex_4,dset_size))
    

    #k fold distribution - there are 5 iterations 

        self.train_dl = DataLoader(torch.utils.data.ConcatDataset(subset2,subset3,subset4,subset5), batch_size = self.batch_size,shuffle = False)
        self.test_d1 = DataLoader(subset1, batch_size = self.batch_size, shuffle = False)

        self.train_d2 = DataLoader(torch.utils.data.ConcatDataset(subset1,subset3,subset4,subset5), batch_size = self.batch_size,shuffle = False)
        self.test_d2 = DataLoader(subset2, batch_size = self.batch_size, shuffle = False)

        self.train_d3 = DataLoader(torch.utils.data.ConcatDataset(subset1,subset2,subset4,subset5), batch_size = self.batch_size,shuffle = False)
        self.test_d3 = DataLoader(subset3, batch_size = self.batch_size, shuffle = False)

        self.train_d4 = DataLoader(torch.utils.data.ConcatDataset(subset1,subset2,subset3,subset5), batch_size = self.batch_size,shuffle = False)
        self.test_d4 = DataLoader(subset4, batch_size = self.batch_size, shuffle = False)

        self.train_d4 = DataLoader(torch.utils.data.ConcatDataset(subset1,subset2,subset3,subset4), batch_size = self.batch_size,shuffle = False)
        self.test_d5 = DataLoader(subset5, batch_size = self.batch_size, shuffle = False)

"""
        train, test = torch.utils.data.random_split(dset, [train_size, test_size], generator=g)

        # Create Data Loaders from splits
        self.train_dl = DataLoader(train, batch_size=self.batch_size, shuffle=True)
        self.test_dl = DataLoader(test, batch_size=self.batch_size, shuffle=True)
"""

