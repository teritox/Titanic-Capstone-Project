import os
import pickle
import numpy as np
import pandas as pd

# Get path for the folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "titanic_model.pkl")

print(BASE_DIR)
print(MODEL_PATH)

# Load the model
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# Convert input data from prediction form into model data form

def preprocess_data(input_data):
    pclass = input_data["passenger_class"]
    sex = input_data["gender"]
    age = float(input_data["age"])
    fare = input_data["ticket_fare"]
    family_size = input_data["siblings_or_spouses"] + input_data["parch"] + 1
    embarked = input_data["embark"]
    
    #title_map = {"Mr": 0, "Mrs": 1, "Miss": 2, "Master": 3, "Other": 4}
    #title = title_map.get(input_data["title"], 4)
    
    # add ALL columns exactly as training
    # Right now we have only 3 features in our modeldef preprocess_data(input_data):
    data = {
        "Sex": sex,
        "Pclass": pclass,
        "Age": age,
        "Fare": fare,
        "Title": 1,  # TODO change to title after we added the title in prediction form
        "FamilySize": family_size,
         
    }

    # The dataset is Dataframe in our training model, so important to convert to df form
    df = pd.DataFrame([data])
    return df 


def prediction(input_data):
    X = preprocess_data(input_data)
    print(X)  
    prediction_result = model.predict(X)[0]
    probability = model.predict_proba(X)[0][1]
    print("The prediction result is:",prediction_result)
    print("Type of prediction result",type(prediction_result))
    print("The probability is:", probability)
    print("Type of the probability",type(probability))
    return prediction_result, probability
  