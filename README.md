# ML--Health-Insurance-Cost-Prediction
📊 Dataset

This project uses a dataset containing 50,000 records with various demographic, medical, and financial attributes to predict health insurance premium costs.
Features:

    Age: Age of the individual (years)
    Gender: Male or Female
    Region: Geographic region (Northwest, Southeast, Northeast, etc.)
    Marital_status: Marital status (Married/Unmarried)
    Number Of Dependants: Number of dependents
    BMI_Category: Categorized Body Mass Index (Normal, Overweight, Obesity)
    Smoking_Status: Smoking frequency (No Smoking, Occasional, Regular)
    Employment_Status: Employment type (Salaried, Self-Employed, etc.)
    Income_Level: Income range classification (<10L, 10L - 25L, >40L, etc.)
    Income_Lakhs: Annual income in lakhs
    Medical History: Medical conditions (Diabetes, High Blood Pressure, etc.)
    Insurance_Plan: Type of insurance plan (Bronze, Silver, Gold)
    Annual_Premium_Amount: The actual premium amount (target variable)

This dataset provides a rich set of features to analyze the factors affecting insurance premium pricing.

🚀 Project Steps
1️⃣ Data Preprocessing & EDA

    Cleaned the dataset by handling missing values and outliers.
    Performed statistical analysis and visualizations to understand the impact of various factors on insurance costs.
    Key findings:
        Smokers tend to have significantly higher insurance premiums.
        Higher BMI is associated with increased premium costs.
        Age and number of dependents influence premium calculations.

2️⃣ Feature Engineering

    Encoded categorical variables (sex, smoker, region) using One-Hot Encoding and Label Encoding.
    Standardized numerical features like bmi and age using StandardScaler.
    Created interaction features between age, smoker status, and BMI to enhance model performance.

3️⃣ Model Training

Built and evaluated different machine learning models:

    Linear Regression
    Random Forest Regressor
    XGBoost Regressor (Best-performing model)

4️⃣ Performance Evaluation

Used the following metrics to assess model performance:

    Mean Absolute Error (MAE)
    Mean Squared Error (MSE)
    Root Mean Squared Error (RMSE)
    R² Score

XGBoost achieved the best performance with the lowest RMSE and highest R² score.
🛠️ Tools and Libraries

    Python
    pandas, numpy (Data manipulation)
    matplotlib, seaborn (Visualization)
    scikit-learn, XGBoost (Machine learning & evaluation)
    joblib (Model saving)
    streamlit (Deployment)

📈 Results

    Explored the impact of age, BMI, and smoking status on insurance costs.
    XGBoost model showed the best accuracy in premium cost predictions.

🌍 Deployment

The model is deployed using Streamlit on the cloud, allowing users to input their details and receive a predicted premium cost.
📂 Repository Structure

📂 health-insurance-premium-prediction  
│── 📂 notebooks/        # Jupyter Notebooks for EDA & modeling  
│── 📂 data/            # Dataset used for training  
│── 📂 results/         # Evaluation metrics and plots  
│── app.py             # Streamlit application  
│── requirements.txt   # Dependencies  
│── README.md          # Project documentation  

🏗️ Installation & Setup

Clone the repository:

    git clone https://github.com/yourusername/health-insurance-premium-prediction.git
    cd health-insurance-premium-prediction

Install dependencies:
    pip install -r requirements.txt

Run the application:
    streamlit run app.py

🔥 Future Improvements

    Improve model accuracy with additional demographic and medical history features.
    Enhance UI for better user interaction.
    Integrate a database to store user inputs and predictions.

📜 License

This project is open-source under the Apache 2.0 License.
