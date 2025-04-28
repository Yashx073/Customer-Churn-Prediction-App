# Customer-Churn-Prediction-App

## Overview

The **Customer Churn Prediction App** is a machine learning-driven web application built using **Streamlit**. This app helps businesses predict whether a customer is likely to churn (discontinue a subscription-based service) based on their profile. By leveraging historical customer data, the model identifies at-risk customers and suggests retention strategies.

## Features

- **Customer Churn Prediction**: Predicts whether a customer will churn or stay based on their profile data.
- **Visualization**: Displays a pie chart showing the probability of churn vs stay and a feature comparison bar graph.
- **Retention Strategy**: Provides a retention strategy based on the churn probability.
- **Download Results**: Users can download the prediction results as a **CSV** or **PDF**.
- **Animated Feedback**: When a customer is likely to stay, animated balloons pop up as a visual confirmation.

## Key Sections of the App

1. **Customer Profile Input**: Users enter customer details such as:
   - Credit Score
   - Age
   - Tenure (Years with Company)
   - Account Balance
   - Number of Products
   - Estimated Salary

2. **Customer Membership Details**: Includes whether the customer has a credit card and is an active member.

3. **Geographical & Gender Info**: User selects the customer's geography (France, Germany, Spain) and gender.

4. **Prediction**: The app predicts whether the customer is likely to churn or stay and displays the churn probability in graphical formats.

5. **Retention Strategy Suggestion**: Based on the churn probability, suggestions for customer retention are provided.

## Installation

### Clone the repository
```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```
### Install dependencies
```
pip install -r requirements.txt
```

### Run the app
```
streamlit run app.py
```
##How to Use
Enter the customer details in the input fields in the sidebar.

Click on the "Predict Churn" button to get the prediction.

View the churn probability, feature comparison, and retention strategy suggestion.

Download the prediction results in CSV or PDF format.

##Model Explanation
The model used for churn prediction is a machine learning model, specifically a Random Forest Classifier. The model was trained on historical customer data, considering features such as customer age, tenure with the company, balance, and geographical location.

##Future Improvements
Model Improvement: Implementing hyperparameter tuning for better accuracy.

Feature Engineering: Adding additional features like customer feedback, transaction history, and more.

Real-time Predictions: Integrating the app with real-time data streams for live customer predictions.

##Contributing
Feel free to fork this repository and submit a pull request if you want to contribute to the project.

##License
This project is licensed under the MIT License - see the LICENSE file for details.

##Acknowledgments
Streamlit for building a simple and powerful framework for creating web applications.

scikit-learn for providing machine learning tools for classification.

Plotly for helping create beautiful, interactive visualizations.
