from flask import Flask, request, jsonify
import pickle
import numpy as np 
from PIL import Image
import io

app = Flask(__name__)

#template for loading model with pickle, will be updated once model is uploaded
def load_model():
    with open("app/model/model.pk1", "rb") as model_file:
        model = pickel.load(model_file)
    return model

model = load_model()

