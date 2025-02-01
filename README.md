# 🚑 ML - Health Insurance Cost Prediction  

## 📊 Dataset  
This project uses a dataset containing **50,000** records with various demographic, medical, and financial attributes to predict **health insurance premium costs**.  

### Features:  
- **Age**: Age of the individual (years)  
- **Gender**: Male or Female  
- **Region**: Geographic region (Northwest, Southeast, Northeast, etc.)  
- **Marital Status**: Married or Unmarried  
- **Number of Dependents**: Number of dependents in the household  
- **BMI Category**: Categorized Body Mass Index (Normal, Overweight, Obesity)  
- **Smoking Status**: Smoking frequency (No Smoking, Occasional, Regular)  
- **Employment Status**: Employment type (Salaried, Self-Employed, etc.)  
- **Income Level**: Income range classification (<10L, 10L - 25L, >40L, etc.)  
- **Income in Lakhs**: Annual income in lakhs  
- **Medical History**: Medical conditions (Diabetes, High Blood Pressure, etc.)  
- **Insurance Plan**: Type of insurance plan (Bronze, Silver, Gold)  
- **Annual Premium Amount**: The actual premium amount (Target Variable)  

This dataset provides a rich set of features to analyze the factors affecting **insurance premium pricing**.  

---

## 🚀 Project Steps  

### 1️⃣ Data Preprocessing & EDA  
- Cleaned the dataset by handling missing values and outliers.  
- Performed **statistical analysis** and **visualizations** to understand the impact of various factors on insurance costs.  
- **Key findings:**  
  - Smokers tend to have significantly higher insurance premiums.  
  - Higher BMI is associated with increased premium costs.  
  - Age and number of dependents influence premium calculations.  

### 2️⃣ Feature Engineering  
- Encoded categorical variables (`Gender`, `Smoking Status`, `Region`) using **One-Hot Encoding** and **Label Encoding**.  
- Standardized numerical features like `BMI` and `Age` using **StandardScaler**.  
- Created interaction features between **Age, Smoking Status, and BMI** to enhance model performance.  

### 3️⃣ Model Training  
Built and evaluated different machine learning models:  
- **Linear Regression**  
- **Random Forest Regressor**  
- **XGBoost Regressor** (Best-performing model)  

### 4️⃣ Performance Evaluation  
Used the following metrics to assess model performance:  
- **Mean Absolute Error (MAE)**  
- **Mean Squared Error (MSE)**  
- **Root Mean Squared Error (RMSE)**  
- **R² Score**  

XGBoost achieved the best performance with the **lowest RMSE** and **highest R² score**.  

## 🛠️ Tools and Libraries  
- **Python**  
- **pandas, numpy** (Data manipulation)  
- **matplotlib, seaborn** (Visualization)  
- **scikit-learn, XGBoost** (Machine learning & evaluation)  
- **joblib** (Model saving)  
- **streamlit** (Deployment)  

## 📈 Results  
- Explored the impact of **Age, BMI, and Smoking Status** on insurance costs.  
- **XGBoost model** showed the best accuracy in premium cost predictions.  

## 🌍 Deployment  
The model is deployed using **Streamlit** on the cloud, allowing users to input their details and receive a predicted premium cost.  

## 📂 Repository Structure  
```
📂 health-insurance-premium-prediction  
│── 📂 notebooks/        # Jupyter Notebooks for EDA & modeling  
│── 📂 data/            # Dataset used for training  
│── 📂 results/         # Evaluation metrics and plots  
│── app.py             # Streamlit application  
│── requirements.txt   # Dependencies  
│── README.md          # Project documentation  
```  

## 🏗️ Installation & Setup  
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/health-insurance-premium-prediction.git
   cd health-insurance-premium-prediction
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:  
   ```bash
   streamlit run app.py
   ```  

## 🔥 Future Improvements  
- Improve model accuracy with additional demographic and medical history features.  
- Enhance UI for better user interaction.  
- Integrate a database to store user inputs and predictions.  

## 📜 License  
This project is open-source under the **Apache 2.0 License**.  
