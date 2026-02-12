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
 
    age = input_data["age"]
    if age <=12:
        age_bin = "Child"
    elif 12< age <= 19:
        age_bin = "Teen"
    elif 19< age <= 39:
        age_bin = "Adult"
    elif 39< age <= 59:
        age_bin = "Middel Aged"
    else:
        age_bin = "Senior"

    age_bins = ["Child", "Teen","Adult","Middel Aged", "Senior"]
    agebin_dict = {f"AgeBin_{a}": int(age_bin == a) for a in age_bins}

    family_size = input_data["siblings_or_spouses"] + input_data["parch"] + 1
    embarked = input_data["embark"]
    
    #title_map = {"Mr": 0, "Mrs": 1, "Miss": 2, "Master": 3, "Other": 4}
    #title = title_map.get(input_data["title"], 4)
    
    # add ALL columns exactly as training
    # order of the features in our model
    # "Sex","Pclass","Fare","FamilySize",
    # "AgeBin_Child","AgeBin_Teen","AgeBin_Adult", "AgeBin_Middle Aged","AgeBin_Senior",
    # "Embarked_C","Embarked_Q","Embarked_S",
    # "Title_Master", "Title_Miss","Title_Mrs","Title_Mr","Title_Rare",
    data = {
        "Sex": input_data["gender"],
        "Pclass": input_data["passenger_class"],
        "Fare": input_data["ticket_fare"],
        "FamilySize": family_size,
        **agebin_dict,
        "Title": 1,  # TODO change to title after we added the title in prediction form
        
        
         
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
  