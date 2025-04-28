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
