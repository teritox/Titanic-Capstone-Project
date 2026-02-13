# Titanic-Capstone-Project

Python AI / ML student project. Capstone project built on machine learning system based on real-world data and deployed as a Django web application.


## Contents
1. [Project Overview](#porject-overview)
2. [How to set up files and run locally](#how-to-set-up-the-file-and-run-locally)
3. [Description of the ML model](#description-of-the-machine-learning-models)
4. [Overview of the system architecture](#overview-of-the-system-architecture)

## Project Overview 
The Titanic++ Capstone Project is an end-to-end machine learning and web development project that demonstrates how a predictive model can be built from raw data and deployed as a real-world application.
Using historical passenger data from the Titanic disaster, this project builds a machine learning model to predict whether a passenger survived based on demographic and travel-related features such as age, gender, passenger class, and family size. The trained model is integrated into a Django-based web application where users can input passenger details and receive survival predictions along with probability scores.
The system also persists prediction inputs and results in a database, allowing users to view prediction history. The project follows software engineering best practices including modular design, version control with Git, and clear documentation.
This project simulates a realistic production-style workflow that combines data science, machine learning, backend web development, and deployment principles.


The purpose of this project is to gain hands-on experience in building and deploying a complete machine learning system rather than focusing only on model accuracy.
Specifically, this project aims to:

- Develop a strong understanding of data preprocessing, feature engineering, and model evaluation
- Practice building reproducible machine learning pipelines
- Learn how to deploy a trained ML model inside a Django web application
- Understand how machine learning systems interact with databases and user interfaces
- Apply software engineering best practices, including modular design and separation of concerns
- Improve proficiency with Git and GitHub through continuous, meaningful commits
- Simulate a real-world ML product lifecycle, from raw data to user-facing application
  Overall, the project bridges the gap between theoretical machine learning and practical software development by delivering a fully functional prediction system that mirrors how ML-powered applications are built in industry.

Go back to [Contents](#contents).

## How to set up the file and run locally
Download the Titanic dataset at [Titanic]( https://www.kaggle.com/c/titanic/data)

Go back to [Contents](#contents).
## Description of the machine learning models

 



Go back to [Contents](#contents).
## Overview of the System Architecture

### 1. Data Preprocessing
#### 1️⃣ Handling Missing Values
#### Age
Instead of using a global average, missing **Age** values were imputed using **title-based grouping**:

- **Title Extraction:** Extracted from the `Name` column.

  Example:
  - `"Braund, Mr. Owen Harris" → Mr`
  - `"Cumings, Mrs. John Bradley" → Mrs`
- **Title Grouping:** 
  
  A new feature called **Title** by extracting it from **Name** column and grouping titles into **Mr, Mrs, Miss, Master** and **Rare** categories. Missing **Age** values(NaN) are then replaced with the mean age within each title group.

- **Age Imputation:** 
  
  Missing **Age** values were filled with the **mean age** of the corresponding title group.  

#### Embarked
This feature contains only two missing values, which are unlikely to affect the model's performance. Therefore, these values are imputed with letter **C**

#### 2️⃣ Feature Engineering 
- **FamilySize:**
  A new feature called `FamilySize` is created by adding `SibSp + Parch +1`. This represents the **total number of family members aboard**, including the passenger themselves.

- **CabinDeck:**
  `CabinDeck` is extracted from cabin numbers, yielding values `['Unknown', 'C', 'E', 'G', 'D', 'A', 'B', 'F', 'T']`. Survival was significantly lower for passengers with `Unknown` deck, while decks `B`, `D`, and `E` showed the highest survival rates.

- **AgeBin:** 
  The age feature is grouped into categorical age ranges to reduce noise and capture life-stage patterns that may influence survival. The bins are defined as:
  
  - **Child:** 0-12 years
  - **Teen:** 13-19 years
  - **Adult:** 20-39 years
  - **Middle Aged:** 40-59 years
  - **Senior:** 60+ years

#### 3️⃣ Encoding Categorical Variables
One-hot encoding was used for `AgeBin`,`Embarked` and `Title` features to prevent the model from assuming any ordinal relationship.

  - **Sex:**
    - `male → 0`
    - `female → 1`
  - **Embarked(C/Q/S):**
    - `Embarked_C: 0/1`
    - `Embarked_Q: 0/1`
    - `Embarked_S: 0/1`
  - **AgeBin:**
    - `AgeBin_Child: 0/1`
    - `AgeBin_Teen: 0/1`
    - `AgeBin_Adult: 0/1`
    - `AgeBin_Middle Aged: 0/1`
    - `AgeBin_Senior: 0/1`
    
  - **Title:**
    - Grouping titles into **Mr, Mrs, Miss, Master** and **Rare** which were also encoded:
      - `Title_Master: 0/1`
      - `Title_Miss: 0/1`
      - `Title_Mrs: 0/1`
      - `Title_Mr: 0/1`
      - `Title_Rare: 0/1`
    - Each title category is converted into a binary (0/1) column.This allows logistic regression to learn survival patterns related to:
      - Gender (Mr vs Mrs vs Miss)
      - Age group (Master = young boys)
      - Social status (Rare titles)
  
  - **Example:**

    Table 1: Original Title Feature Before One-Hot Encoding
    | PassengerId | Title  |
    | ----------- | ------ |
    | 1           | Mr     |
    | 2           | Mrs    |

    Table 2: Title Features After One-Hot Encoding
    | PassengerId | Title_Master | Title_Miss | Title_Mrs | Title_Mr | Title_Rare |
    | ----------- | ------------ | ---------- | --------- | -------- | ---------- |
    | 1           | 0            | 0          | 0         | 1        | 0          |
    | 2           | 0            | 0          | 1         | 0        | 0          |



### 2. Model Training and Evaluation
#### 1️⃣ Describe the model selection (why Logistic Regression or Random Forest) 
  - **Baseline Model: Logistic Regression**  
    We start with logistic regression as a baseline because survival is a binary outcome (`0`/`1`). It is a simple model that provides a strong reference point for comparing more complex models.
  - **Candidate Model 1: Random Forest**  
    *TODO: Why it may improve on baseline (e.g., nonlinearity, interactions).*
  - **Candidate Model 2: XGBoost**  
    *TODO*
#### 2️⃣ Validation Strategy

  - **Train, Test and Validation Datasets** 

    The Titanic dataset has 891 rows, which is relatively small. A 0.1 test split gives more training data, but the test set would only have 89 rows, making the metrics less stable. A 0.3 test split provides a larger test set but reduces the training data, which could slightly hurt model performance. 
    
    Therefore, We split data with `test_size=0.2` (80% train / 20% test), balancing enough training data with a sufficiently large test set for stable evaluation.
    - Traning dataset = 713 rows → enough to train logistic regression
    - Test dataset = 178 rows →enough to get stable f1 scores

    We use **Stratified K-Fold Cross-Valiation** : 
    
    Split training data into k folds, train on k-1 folds and validate on the remaining fold and repeat k times. The class distribution in each fold is fixed
    ```python
    cv = StratifiedKFold(n_splits=5, shuffle=True,random_state=42)
    f1_scores = cross_val_score(model, X_train, y_train, cv=cv, scoring='f1')

#### 3️⃣ Evaluation Metrics  

  The Titanic Dataset is slightly imbalanced as shown below:

  | Class               | Count | Percentage |
  | ------------------- | ----- | ---------- |
  | 0 (Not survived) | 549   | ~62%       |
  | 1 (Survived)        | 342   | ~38%       |
  
  With 62% non-survivors (Majority Class) and 38% survivors (Minority Class). The accuracy is biased towards to non-survivors, therefore we focus on `f1` for the survivors (minority class). 
  And Use `stratify=y` in `train_test_split` so that so that **the class distribution in train and test sets matches the original distribution of y**.
  - **Logistic Model Overall Performance**
  
    Mean F1-score = 0.7566
    | Class                   | Precision | Recall | F1-Score | Support |
    | ----------------------- | --------- | ------ | -------- | ------- |
    | **0 – Not Survive** | ✔0.87      | ✔0.80   | ✔0.83     | 105     |
    | **1 – Survived**        | •0.74      | ✔0.82   | •**0.78**     | 74      |
    | **Accuracy**            |           |        | ✔**0.81** | 179     |
    | **Macro Avg**           | 0.80      | 0.81   | 0.81     | 179     |
    | **Weighted Avg**        | 0.82      | 0.81   | 0.81     | 179     |

  - **Random Forest** 

  - **Confusion Matrix**  
  The model performs well at distinguishing between survivors and non-survivors, correctly identifying most passengers. It occasionally overestimates survival, but overall the confusion matrix shows that the model makes relatively few misclassifications and captures the patterns in the data effectively.

    ![confusion matrix](web/static/images/confusion_matrix.jpg) 

### 3. Django Integration
- Explain how the model is loaded  
- Show form design and validation  
- Explain preprocessing applied to user input  
- Describe how predictions are displayed 

Go back to [Contents](#contents).
