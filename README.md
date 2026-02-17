# Titanic-Capstone-Project

Python AI / ML student project. Capstone project built on machine learning system based on real-world data and deployed as a Django web application.

## Contents

1. [Project Overview](#project-overview)
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

## How to Set Up and Run Locally

### Prerequisites

- Python 3.14
- Conda
- pip
- Git

### Clone the repository

```bash
git clone https://github.com/teritox/Titanic-Capstone-Project.git
cd Titanic-Capstone-Project
```

### Create and activate the virtual environment

```bash
conda env create -f environment.yml
conda activate titanic-capstone-env # or the name specified in environment.yml
```

### Set up the database (first-time setup)

This project uses Django and a SQLite database to store previous predictions.

```bash
python web/manage.py migrate
```

**If you encounter migration issues, ensure the virtual environment is activated before running Django commands.**

### Run the server locally

```bash
python web/manage.py runserver
```

Then open your browser and go to:
http://127.0.0.1:8000/

### Dataset source

The required dataset is already included in the project.

The original dataset source can be found on Kaggle:
https://www.kaggle.com/c/titanic/data

Go back to [Contents](#contents).

## Description of the machine learning models

This project solves a binary classification problem: predicting `Survived` (0/1) from passenger features in the Titanic dataset.

Models evaluated:
- Logistic Regression (baseline linear classifier)
- Random Forest (non-linear ensemble baseline)

Feature pipeline (used during training and prediction):
- Missing value handling (Age, Embarked)
- Engineered features: `Title`, `FamilySize`, `AgeBin`, `CabinDeck`
- Categorical encoding for model-ready inputs

Evaluation approach:
- 80/20 train-test split with stratification
- 5-fold stratified cross-validation
- Metrics: Accuracy, Confusion Matrix, Precision/Recall/F1

Result summary:
- Both models achieve about 81% accuracy.
- Logistic Regression provides better recall for survivors and is used for deployment.
- Trained model artifact: `web/predictor/titanic_model.pkl`.

See detailed discussion in [Overview of the system architecture](#overview-of-the-system-architecture).

Go back to [Contents](#contents).

## Overview of the System Architecture

### 1. Data Preprocessing

#### 1.1 Handling Missing Values

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

#### 1.2 Feature Engineering

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

#### 1.3 Encoding Categorical Variables

One-hot encoding with baseline was used for `AgeBin`,`Embarked` ,`Pcalss` and `Title` features to prevent the model from assuming any ordinal relationship.

- **Sex:**
  - `male → 0`
  - `female → 1`
- **Embarked(C/Q/S):**
  - `Baseline: Embarked = S`
  - `Embarked_C: 0/1`
  - `Embarked_Q: 0/1`
- **Pclass:**
  - `Baseline: Pclass = 1`
  - `Pclass_2: 0/1`
  - `Pclass_3: 0/1`
- **AgeBin:**
  - `Baseline: AgeBin = Child`
  - `AgeBin_Teen: 0/1`
  - `AgeBin_Adult: 0/1`
  - `AgeBin_Middle Aged: 0/1`
  - `AgeBin_Senior: 0/1`
- **Title:**
  - Grouping titles into **Mr, Mrs, Miss, Master** and **Rare** which were also encoded:
    - `Baseline: Title`
    - `Title_Miss: 0/1`
    - `Title_Mrs: 0/1`
    - `Title_Mr: 0/1`
    - `Title_Rare: 0/1`
  - Each title category is converted into a binary (0/1) column.This allows logistic regression to learn survival patterns related to:
    - Gender (Mr vs Mrs vs Miss)
    - Age group (Master = young boys)
    - Social status (Rare titles)

- **Example:**

  Table 1: Original Title Feature Before One-Hot Encoding with `Master` as baseline
  | PassengerId | Title |
  | ----------- | ------ |
  | 1 | Mr |
  | 2 | Mrs |

  Table 2: Title Features After One-Hot Encoding
  | PassengerId | Title_Miss | Title_Mrs | Title_Mr | Title_Rare |
  | ----------- | ---------- | --------- | -------- | ---------- |
  | 1 | 0 | 0 | 1 | 0 |
  | 2 | 0 | 1 | 0 | 0 |

### 2. Model Training and Evaluation

This section describes how the machine learning models were selected, trained, validated, and evaluated for Titanic survival prediction. It summarizes the modeling decisions, compares Logistic Regression and Random Forest performance, and explains why the final deployed model was chosen.

#### 2.1 Model Selection (why Logistic Regression or Random Forest) 
  - **Problem Definition**

    The aim is to predict whether a passenger survived the Titanic disaster. This is a binary classification task using the Titanic dataset, which contains passenger information such as age, sex, passenger class, and other relevant features.
  - **Baseline Model: Logistic Regression (RL)**  
    **Why Chosen** 
    
    Logistic Regression is chosen as the baseline because it is a simple and widely used model for binary classification tasks. LR  assumes a linear relationship between input features and log-odds of the target outcomes, providing a clear and interpretable reference point for comparing more complex models.

    **Prediction Pipeline**
    1. **Feature Preparation:**
        - Engineer additional features:
          - **AgeBin:** Convert `Age` into categorical age groups (e.g., Child, Adult, Senior)
          - **Title:** Extract titles from passenger names (e.g., Mr, Mrs, Miss, Master, Rare) and encode as categorical
          - **FamilySize:** Compute total family size `SibSp` + `parch`
  
        - Encode categorical features `Sex`,`AgeBin`, `Embarked`, `Title`,`Pclass` using one-hot encoding with baseline.
        - Keep numerical features `Fare`, `FamilySize` as is.
    2. **Probability Computation:**
        - Linear Weighted Sum of the Features:
        $$z = \beta_0 + \beta_1 \text{Sex} + \beta_2 \text{Pclass} + \beta_3 \text{Fare} + \beta_4 \text{AgeBin} + \beta_5 \text{Title} + \dots$$
        - The Predicted Probability of Survival:
  
            $$P(\text{Survived}=1) = \frac{1}{1 + e^ {- z}}$$

    3. **Prediction**

      Assign class based on probability threshold (commonly 0.5):
        - P>0.5⇒Survived
        - P≤0.5⇒Did not survive

  - **Candidate Model 1: Random Forest (RF)**  
    **Why Chosen** 
    
    Random Forest is a supervised ensemble ML method that uses many decision trees trained on random subsets of data and features. Each tree makes a prediction,      and the final output is determined by majority voting. Using this model allows us to compare a nonlinear, tree-based approach to feature handling and
    prediction with the linear, weight-based approach used in Logistic Regression.

    **Prediction Pipeline**

    1.  **Feature Preparation:**
        - Engineer additional features:
          - **CabinDeck:** Extract letters from `Cabin` into categorical groups (e.g., `['Unknown', 'C', 'E', 'G', 'D', 'A', 'B', 'F', 'T']`).
        - Encode categorical features `Sex`,`Embarked`, `Title`,`CabinDeck` as integer labels. **Note:** one-hot encoding is **NOT** applied for the **RF** model.
        - Keep numerical features `Fare`, `SibSP`, `parch`,`Pclass`, `Age` as is.
    2. **Build Decision Trees**
        - **Bootstrap sampling** of the training data
        - Random subset of features
    3. **Prediction**
        - Each tree predicts survival (Survived / Not Survived) independently.
        - Final prediction is determined by majority vote across all trees.

  - **Key Comparisons**

  | Aspect                        | Logistic Regression                                                    | Random Forest                                      |
  | ----------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------- |
  | **Categorical Features**      | Must be one-hot encoded; baseline category dropped (`drop_first=True`) | Can be integer-mapped or one-hot encoding |
  | **Prediction**                | Linear weighted sum passed trough Sigmoid                              | Majority vote across all trees |
  | **Strength**                  | Low computational cost compare to ensemble model like Random Forest    | Captures non-linear relationships and interactions |
  | **Limitation**                | Cannot automatically capture interactions or non-linear effects        | Predicted survival via majority vote of trees      |

  
#### 2.2 Validation Strategy

- **Train, Test and Validation Datasets**

  The Titanic dataset has 891 rows, which is relatively small. A 0.1 test split gives more training data, but the test set would only have 89 rows, making the metrics less stable. A 0.3 test split provides a larger test set but reduces the training data, which could slightly hurt model performance.

  Therefore, We split data with `test_size=0.2` (80% train / 20% test), balancing enough training data with a sufficiently large test set for stable evaluation.
  - Training dataset = 713 rows → enough to train logistic regression
  - Test dataset = 178 rows →enough to get stable f1 scores

  We use **Stratified K-Fold Cross-Validation** :

    The Titanic dataset has 891 rows, which is relatively small. A 0.1 test split gives more training data, but the test set would only have 89 rows, making the metrics less stable. A 0.3 test split provides a larger test set but reduces the training data, which could slightly hurt model performance. 
    
    Therefore, We split data with `test_size=0.2` (80% train / 20% test), balancing enough training data with a sufficiently large test set for stable evaluation.
    - Training dataset = 713 rows → enough to train logistic regression
    - Test dataset = 178 rows →enough to get stable f1 scores
  Split training data into k folds, train on k-1 folds and validate on the remaining fold and repeat k times. The class distribution in each fold is fixed

  ```python
  cv = StratifiedKFold(n_splits=5, shuffle=True,random_state=42)
  f1_scores = cross_val_score(model, X_train, y_train, cv=cv, scoring='f1')
  ```

#### 2.3 Evaluation Metrics

The Titanic Dataset is slightly imbalanced as shown below:

| Class            | Count | Percentage |
| ---------------- | ----- | ---------- |
| 0 (Not survived) | 549   | ~62%       |
| 1 (Survived)     | 342   | ~38%       |

With 62% non-survivors (Majority Class) and 38% survivors (Minority Class). The accuracy is biased towards to non-survivors, therefore we focus on `f1` for the survivors (minority class).
And Use `stratify=y` in `train_test_split` so that so that **the class distribution in train and test sets matches the original distribution of y**.

- **Logistic Regression Model Overall Performance**

  The model performs well at distinguishing between survivors and non-survivors, correctly identifying most passengers. It occasionally overestimates survival, but overall the confusion matrix shows that the model makes relatively few misclassifications and captures the patterns in the data effectively.

  ![confusion matrix](web/static/images/confusion_matrix.jpg)

  | Class               | Precision | Recall | F1-Score  | Support |
  | ------------------- | --------- | ------ | --------- | ------- |
  | **0 – Not Survive** | ✔0.87     | ✔0.80  | ✔0.83     | 105     |
  | **1 – Survived**    | •0.74     | ✔0.82  | •**0.78** | 74      |
  | **Accuracy**        |           |        | ✔**0.81** | 179     |
  | **Macro Avg**       | 0.80      | 0.81   | 0.81      | 179     |
  | **Weighted Avg**    | 0.82      | 0.81   | 0.81      | 179     |

  Cross validation gives Mean F1-score = 0.7566 which indicate that our Logistic Regression model performs generally well as well.

- **Random Forest Model Overall Performance**

  Cross validation gives Mean F1-score = 0.7660 which indicate that our RF model performs generally well.

  | Class | Precision | Recall | F1-score | Support |
  |-------|-----------|--------|----------|---------|
  | **0 – Not Survived** |✔0.82 |✔0.88 | ✔0.85 | 110 |
  | **1 – Survived**     |✔0.79 | •**0.70**| •**0.74** | 69  |
  | **Accuracy**         |      |      | **0.81** | 179 |
  | **Macro Avg**        | 0.80 | 0.79 | 0.79 | 179 |
  | **Weighted Avg**     | 0.81 | 0.81 | 0.81 | 179 |

- **Comparison of prediction performance: LR vs RF**
  - **Accuracy** : both models give high accuracy

    | Model               | Accuracy |
    | ------------------- | -------- |
    | Random Forest       | ~81%     |
    | Logistic Regression | ~81%     |
  
  - **Recall on survivors** : LR is **much better at detecting survivors**, and RF misses more survivors.


    | Model | Recall (Survived) |
    | ----- | ----------------- |
    | RF    | 0.70              |
    | LR    | 0.82              |

  - **Precision on survivors** : RF is slightly more precise at prediction on survivor. 

    | Model | Precision (Survived) |
    | ----- | -------------------- |
    | RF    | 0.79                 |
    |  LR    | 0.74                 |


Both Logistic Regression and Random Forest achieved similar overall accuracy (~81%). However, Logistic Regression is more balanced and Random Forest is slightly biased toward predicting non-survival. 
  


### 3. Django Integration

The trained machine learning model is deployed inside the Django web application to provide real-time survival predictions. The integration consists of model loading, form handling and validation, preprocessing of user input, prediction generation, and displaying results.

**3.1 Model Loading**
The trained model is saved as a serialized file (titanic_model.pkl) using Python's pickle module(ml_model.py) and loaded inside the Django application. - The model is loaded in the machine learning module:

      BASE_DIR = os.path.dirname(os.path.abspath(**file**))
      MODEL_PATH = os.path.join(BASE_DIR, "titanic_model.pkl")

      with open(MODEL_PATH, "rb") as f:
      model = pickle.load(f)

This implementation ensures:

- The model is loaded from a fixed path inside the project
- The trained model can be reused without retraining
- The web application can perform predictions efficiently
- The prediction function is then imported and used inside the Django view:

      from .ml_model import prediction

- When the user submits the form, Django calls:

      prediction_result, prediction_probability = prediction(input_data)

**3.2 Form Design and Validation**

- User input is collected using Django's built-in form system defined in:

      forms.py

- The form collects the following passenger features: - Title - Passenger class - Gender - Age - Number of siblings or spouses - Number of parents or children - Ticket fare - Embark location

  Example field definition:

        age = forms.IntegerField(
        min_value=0,
        max_value=100
        )

Automatic Validation

- Django automatically validates user input before making predictions.

Validation includes:

- Range validation

  Examples:
  - Age must be between 0 and 100
  - Fare must be between 0 and 500
  - Family counts must be ≥ 0

- Choice validation
  Users must select valid predefined values for:
  - Title
  - Passenger class
  - Gender
  - Embark location

- Type validation
  Django ensures:
  - Integer fields contain integers
  - Float fields contain valid numbers

- After validation, Django provides clean and safe input data:

      input_data = prediction_form.cleaned_data

- This prevents invalid or unsafe data from reaching the machine learning model.

**3.3 Preprocessing Applied to User Input**

- Before prediction, the user input undergoes the same preprocessing steps used during model training. This ensures consistency between training data and prediction data.
- This preprocessing is implemented in:

  ml_model.py

- Age Bin Encoding
  - Age is converted into categorical age groups:

    Age Range Category
    0–12 Child
    13–19 Teen
    20–39 Adult
    40–59 Middle Aged
    60+ Senior

  - These categories are then converted into one-hot encoded features.

    Example:
    ```python
    agebin_dict = {
                  "AgeBin_Teen": 0,
                  "AgeBin_Adult": 1,
                  "AgeBin_Middle Aged": 0,
                  "AgeBin_Senior": 0
                  }

  - Child is used as the baseline category.

- Embarked Encoding
  - Embark location is converted into one-hot encoded features:
    ```python
    embarked_dict = {"Embarked_C": 1, "Embarked_Q": 0}

  - Southampton is used as the baseline.

- Title Encoding
  - Passenger title is converted into binary features:
    ```python
    title_dict = {
                  "Title_Miss": 0,
                  "Title_Mrs": 1,
                  "Title_Mr": 0,
                  "Title_Rare": 0
                  }

  - Master is used as the baseline category.

- Family Size Feature Engineering
  - A new feature called FamilySize is created:

    ```python
    FamilySize = siblings_or_spouses + parch +1

  - This represents total family members onboard.

- Final Data Conversion
  - All features are combined and converted into a Pandas DataFrame:

    ```python
    df = pd.DataFrame([data])

  - This ensures compatibility with the trained model.

**3.4 Prediction Generation**

- After preprocessing, the model generates predictions using:
  ```python
  prediction_result = model.predict(X)[0]
  probability = model.predict_proba(X)[0][1]

- The model returns:

  Prediction result:
  ```text
    0 → Did Not Survive
    1 → Survived
  ```
  
  - Prediction probability: Probability of survival between 0 and 1

**3.5 Saving Predictions to the Database**

- The prediction and input data are saved in the Django database:
  ```django
  prediction_obj = Prediction.objects.create(
                input_data=input_data,
                prediction_result=prediction_result,
                prediction_probability=prediction_probability,)

- This allows the application to store prediction history.

**3.6 Displaying Prediction Results**

- After prediction, the user is redirected to the result page: `result.html`

- The page displays:

      Prediction outcome:

      Example:
      They would survive! 🎉 or They would not survive

      Prediction probability:

      Example:
      Probability: 78.45%

- The probability is formatted as a percentage for easier interpretation.

**3.7 Prediction History Feature**

- All predictions are stored and displayed in the History page.
- The history page shows:
  - Passenger input data
  - Prediction result
  - Prediction probability
  - Timestamp

**3.8 Complete Django Prediction Workflow**

The full system workflow is:

- User opens prediction form
- User enters passenger information
- Django validates input
- Input is sent to ML module
- Data is preprocessed
- Model generates prediction
- Prediction is saved in database
- Result is displayed to user
- Prediction is stored in history

Go back to [Contents](#contents).
