import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
from fpdf import FPDF

model = joblib.load('churn_model.pkl')

feature_names = ['Credit Score', 'Age', 'Tenure', 'Balance', 'Num of Products', 
                 'Has Credit Card', 'Is Active Member', 'Estimated Salary', 
                 'Geo: France', 'Geo: Germany', 'Gender: Female']

st.set_page_config(page_title="Customer Churn Prediction", page_icon="🔮", layout="wide")

st.title("🔮 Customer Churn Prediction App")
st.markdown("Use this tool to predict whether a customer is likely to churn based on their profile.")

with st.sidebar:
    st.header("Input Customer Details")
    
    with st.expander("Customer Profile Input", expanded=True):
        credit_score = st.number_input('Credit Score', min_value=300, max_value=850, value=None, step=1)
        age = st.number_input('Age', min_value=18, max_value=100, value=None, step=1)
        tenure = st.number_input('Tenure (Years with Company)', min_value=0, max_value=10, value=None, step=1)
        balance = st.number_input('Account Balance', value=None, step=100.0)
        num_of_products = st.selectbox('Number of Products', [1, 2, 3, 4], index=None)
        estimated_salary = st.number_input('Estimated Salary', value=None, step=100.0) 
        
    with st.expander("Customer Membership Details", expanded=False):
        has_cr_card_input = st.selectbox('Has Credit Card?', ['Yes', 'No'], index=None)

        is_active_member_input = st.selectbox('Is Active Member?', ['Yes', 'No'], index=None)

    with st.expander("Geographical & Gender Info", expanded=False):
        geography = st.selectbox('Geography', ['France', 'Germany', 'Spain'], index=None)
        gender = st.selectbox('Gender', ['Female', 'Male'], index=None)

predict_btn = st.button('🚀 Predict Churn')

if predict_btn:
    if None in [credit_score, age, tenure, balance, num_of_products, estimated_salary, geography, gender] \
       or has_cr_card_input is None or is_active_member_input is None:
        st.error('⚠️ Please fill out all the fields before prediction.')
    else:
        has_cr_card = 1 if has_cr_card_input == 'Yes' else 0
        is_active_member = 1 if is_active_member_input == 'Yes' else 0

        with st.spinner('Analyzing the customer profile...'):
            geo_france = 1 if geography == 'France' else 0
            geo_germany = 1 if geography == 'Germany' else 0
            geo_spain = 1 if geography == 'Spain' else 0
            gender_female = 1 if gender == 'Female' else 0

            features = np.array([[credit_score, age, tenure, balance, num_of_products,
                                  has_cr_card, is_active_member, estimated_salary,
                                  geo_france, geo_germany, gender_female]])

            prediction = model.predict(features)
            churn_prob = model.predict_proba(features)[0][1]
            stay_prob = 1 - churn_prob

        if prediction[0] == 1:
            st.error('🔴 Customer is likely to churn!')
        else:
            st.success('🟢 Customer is likely to stay.')
            st.balloons()

        st.subheader("📊 Churn Probability Distribution")
        churn_data = [stay_prob, churn_prob]
        churn_labels = ['Stay', 'Churn']
        pie_fig = px.pie(
            values=churn_data,
            names=churn_labels,
            color_discrete_sequence=['green', 'red'],
            hole=0.4,
            title="Churn vs Stay Probability"
        )
        st.plotly_chart(pie_fig, use_container_width=True)

        st.subheader("📈 Feature Comparison (Customer vs Average)")
        avg_features = [600, 35, 3, 50000, 2, 1, 1, 60000, 0, 0, 0]
        customer_features = [credit_score, age, tenure, balance, num_of_products,
                             has_cr_card, is_active_member, estimated_salary,
                             geo_france, geo_germany, gender_female]

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.barh(feature_names, customer_features, color='royalblue', alpha=0.7, label='Customer')
        ax.barh(feature_names, avg_features, color='lightcoral', alpha=0.5, label='Average Customer')
        ax.set_xlabel('Feature Value')
        ax.set_title('Customer vs Average Features')
        ax.legend()
        st.pyplot(fig)

        st.subheader("💡 Retention Strategy Suggestion")
        if churn_prob > 0.7:
            st.warning("⚠️ Very High Churn Risk! Consider offering special discounts, loyalty rewards, or personalized engagement.")
        elif churn_prob > 0.4:
            st.info("ℹ️ Moderate Churn Risk. Stay connected with regular feedback surveys or exclusive offers.")
        else:
            st.success("✅ Low Churn Risk. Maintain excellent service and keep communication open.")

        result_data = {
            "Credit Score": credit_score,
            "Age": age,
            "Tenure": tenure,
            "Balance": balance,
            "Num of Products": num_of_products,
            "Has Credit Card": has_cr_card_input,
            "Is Active Member": is_active_member_input,
            "Estimated Salary": estimated_salary,
            "Geography": geography,
            "Gender": gender,
            "Churn Probability": churn_prob,
            "Stay Probability": stay_prob,
            "Prediction": "Churn" if prediction[0] == 1 else "Stay"
        }
        result_df = pd.DataFrame([result_data])

        st.download_button(
            label="Download Prediction as CSV",
            data=result_df.to_csv(index=False),
            file_name="customer_churn_prediction.csv",
            mime="text/csv"
        )

        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Customer Churn Prediction Results", ln=True, align="C")
        for key, value in result_data.items():
            pdf.cell(200, 10, txt=f"{key}: {value}", ln=True, align="L")
        pdf_output = pdf.output(dest='S').encode('latin1')
        
        st.download_button(
            label="Download Prediction as PDF",
            data=pdf_output,
            file_name="customer_churn_prediction.pdf",
            mime="application/pdf"
        )

st.markdown("---")
st.markdown("<center>Made by Yash Mohadikar</center>", unsafe_allow_html=True)
st.markdown("[<center>GitHub Repository](https://github.com/yourusername/yourproject)</center>", unsafe_allow_html=True)
