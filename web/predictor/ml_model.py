import os
import pickle
import numpy

# Get path for the folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "titanic_model.pkl")

print(BASE_DIR)
print(MODEL_PATH)

# Load the model
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

