# ML--Health-Insurance-Cost-Prediction
Health Insurance Premium Cost Prediction
Project Overview

This project aims to predict health insurance premium costs based on various features such as age, BMI, smoking status, and other relevant factors. The model is built using machine learning techniques and deployed using Streamlit on the cloud.
Features Used

    Age
    BMI (Body Mass Index)
    Smoking Status
    Region
    Number of Dependents
    Other relevant factors

Tools & Technologies

    Programming Languages: Python
    Libraries:
        pandas==2.2.3
        numpy
        xgboost
        scikit-learn
        joblib
        streamlit
    Development Environment:
        PyCharm
        Jupyter Notebook

Model Training

The model is trained using XGBoost and Scikit-Learn techniques. The trained model is saved using joblib for easy deployment.
Deployment

The trained model is deployed using Streamlit on the cloud, allowing users to input their details and get a predicted insurance premium.
Installation & Setup

    Clone the repository:

git clone https://github.com/yourusername/health-insurance-premium-prediction.git
cd health-insurance-premium-prediction

Install dependencies:

pip install -r requirements.txt

Run the application:

    streamlit run app.py

Usage

    Users can enter their details via the Streamlit web interface.
    The trained model predicts the insurance premium cost based on input features.

Future Improvements

    Improve model accuracy with additional features.
    Enhance UI/UX for better user interaction.
    Deploy as a standalone web application with a database for user input history.
