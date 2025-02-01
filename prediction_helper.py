import pandas as pd
from joblib import load
from numpy.array_api import astype



model_rest = load("artifacts/model_rest.joblib")
model_young = load("artifacts/model_young.joblib")

scaler_rest = load("artifacts/scaler_rest.joblib")
scaler_young = load("artifacts/scaler_young.joblib")

def calculate_risk_score(medical_history):
    risk_scores = {
        "diabetes": 6,
        "heart disease": 8,
        "high blood pressure": 6,
        "thyroid": 5,
        "no disease": 0,
        "none": 0
    }
    diseases = medical_history.lower().split(" & ")

    total_risk_score = sum(risk_scores.get(disease,0) for disease in diseases)

    max_score = 14
    min_score = 0

    normalized_risk_score = (total_risk_score - min_score) / (max_score - min_score)

    return normalized_risk_score



def hot_encoding(df):

    required_columns = [
        'gender_Male', 'region_Northwest', 'region_Southeast', 'region_Southwest',
        'marital_status_Unmarried', 'bmi_category_Obesity', 'bmi_category_Overweight',
        'bmi_category_Underweight', 'smoking_status_Occasional', 'smoking_status_Regular',
        'employment_status_Salaried', 'employment_status_Self-Employed'
    ]

    # Initialize new columns with 0
    for col in required_columns:
        df[col] = 0

    # Apply one-hot encoding manually
    df['gender_Male'] = (df['gender'] == 'Male').astype(int)
    df['region_Northwest'] = (df['region'] == 'Northwest').astype(int)
    df['region_Southeast'] = (df['region'] == 'Southeast').astype(int)
    df['region_Southwest'] = (df['region'] == 'Southwest').astype(int)
    df['marital_status_Unmarried'] = (df['marital_status'] == 'Unmarried').astype(int)
    df['bmi_category_Obesity'] = (df['bmi_category'] == 'Obesity').astype(int)
    df['bmi_category_Overweight'] = (df['bmi_category'] == 'Overweight').astype(int)
    df['bmi_category_Underweight'] = (df['bmi_category'] == 'Underweight').astype(int)
    df['smoking_status_Occasional'] = (df['smoking_status'] == 'Occasional').astype(int)
    df['smoking_status_Regular'] = (df['smoking_status'] == 'Regular').astype(int)
    df['employment_status_Salaried'] = (df['employment_status'] == 'Salaried').astype(int)
    df['employment_status_Self-Employed'] = (df['employment_status'] == 'Self-Employed').astype(int)

    # Drop the original categorical columns
    df.drop(['gender', 'region', 'marital_status', 'bmi_category', 'smoking_status', 'employment_status'], axis=1,
            inplace=True)


    return df


def preprocess_input(input_dict):
    df = pd.DataFrame([input_dict])

    # medical_risk_score
    df["normalized_risk_score"] = calculate_risk_score(input_dict['medical_history'])

    # map insurance_plan
    df["insurance_plan"] = df["insurance_plan"].map({'Bronze': 1, 'Silver': 2, 'Gold': 3})

    # One-hot encoding
    df_encoded = hot_encoding(df)

    # Scale the input
    df_final = handle_scaling(input_dict['age'], df_encoded)

    df_final.drop('medical_history', axis=1, inplace=True)
    return df_final




def handle_scaling(age , df):
    if age <= 25:
        scaler_object = scaler_young
    else:
        scaler_object = scaler_rest

    cols_to_scale = scaler_object['cols_to_scale']
    scaler = scaler_object['scaler']
    df['income_level'] = None
    df[cols_to_scale] = scaler.transform(df[cols_to_scale])
    df.drop('income_level', axis=1, inplace=True)
    return df





def predict(input_dict):
    input_df = preprocess_input(input_dict)
    if(input_dict['age'] <= 25):
        prediction = model_young.predict(input_df)
    else:
        prediction = model_rest.predict(input_df)

    return int(prediction)


