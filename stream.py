import streamlit as st
import pywhatkit as kit
from datetime import datetime
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
df = pd.read_csv('diabetes.csv')

# Define the Streamlit app
def main():
    # HEADINGS
    st.title('Diabetes Checkup')
    st.sidebar.header('Patient Data')
    st.subheader('Training Data Stats')
    st.write(df.describe())

    # X AND Y DATA
    x = df.drop(['Outcome'], axis=1)
    y = df['Outcome']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    # FUNCTION
    def user_report():
        pregnancies = st.sidebar.slider('Pregnancies', 0, 17, 3)
        glucose = st.sidebar.slider('Glucose', 0, 200, 120)
        bp = st.sidebar.slider('Blood Pressure', 0, 122, 70)
        skinthickness = st.sidebar.slider('Skin Thickness', 0, 100, 20)
        insulin = st.sidebar.slider('Insulin', 0, 846, 79)
        bmi = st.sidebar.slider('BMI', 0, 67, 20)
        dpf = st.sidebar.slider('Diabetes Pedigree Function', 0.0, 2.4, 0.47)
        age = st.sidebar.slider('Age', 21, 88, 33)

        user_report_data = {
            'Pregnancies': pregnancies,
            'Glucose': glucose,
            'BloodPressure': bp,
            'SkinThickness': skinthickness,
            'Insulin': insulin,
            'BMI': bmi,
            'DiabetesPedigreeFunction': dpf,
            'Age': age
        }
        report_data = pd.DataFrame(user_report_data, index=[0])
        return report_data

    # PATIENT DATA
    user_data = user_report()
    st.subheader('Patient Data')
    st.write(user_data)

    # MODEL
    rf = RandomForestClassifier()
    rf.fit(x_train, y_train)
    user_result = rf.predict(user_data)

    # VISUALISATIONS
    st.title('Visualised Patient Report')

    # COLOR FUNCTION
    color = 'blue' if user_result[0] == 0 else 'red'

    # Age vs Pregnancies
    st.header('Pregnancy count Graph (Others vs Yours)')
    fig_preg = plt.figure()
    sns.scatterplot(x='Age', y='Pregnancies', data=df, hue='Outcome', palette='Greens')
    sns.scatterplot(x=user_data['Age'], y=user_data['Pregnancies'], s=150, color=color)
    plt.xticks(np.arange(10, 100, 5))
    plt.yticks(np.arange(0, 20, 2))
    plt.title('0 - Healthy & 1 - Unhealthy')
    st.pyplot(fig_preg)

    # Age vs Glucose
    st.header('Glucose Value Graph (Others vs Yours)')
    fig_glucose = plt.figure()
    sns.scatterplot(x='Age', y='Glucose', data=df, hue='Outcome', palette='magma')
    sns.scatterplot(x=user_data['Age'], y=user_data['Glucose'], s=150, color=color)
    plt.xticks(np.arange(10, 100, 5))
    plt.yticks(np.arange(0, 220, 10))
    plt.title('0 - Healthy & 1 - Unhealthy')
    st.pyplot(fig_glucose)

    # Age vs Blood Pressure
    st.header('Blood Pressure Value Graph (Others vs Yours)')
    fig_bp = plt.figure()
    sns.scatterplot(x='Age', y='BloodPressure', data=df, hue='Outcome', palette='Reds')
    sns.scatterplot(x=user_data['Age'], y=user_data['BloodPressure'], s=150, color=color)
    plt.xticks(np.arange(10, 100, 5))
    plt.yticks(np.arange(0, 130, 10))
    plt.title('0 - Healthy & 1 - Unhealthy')
    st.pyplot(fig_bp)

    # Age vs Skin Thickness
    st.header('Skin Thickness Value Graph (Others vs Yours)')
    fig_st = plt.figure()
    sns.scatterplot(x='Age', y='SkinThickness', data=df, hue='Outcome', palette='Blues')
    sns.scatterplot(x=user_data['Age'], y=user_data['SkinThickness'], s=150, color=color)
    plt.xticks(np.arange(10, 100, 5))
    plt.yticks(np.arange(0, 110, 10))
    plt.title('0 - Healthy & 1 - Unhealthy')
    st.pyplot(fig_st)

    # Age vs Insulin
    st.header('Insulin Value Graph (Others vs Yours)')
    fig_i = plt.figure()
    sns.scatterplot(x='Age', y='Insulin', data=df, hue='Outcome', palette='rocket')
    sns.scatterplot(x=user_data['Age'], y=user_data['Insulin'], s=150, color=color)
    plt.xticks(np.arange(10, 100, 5))
    plt.yticks(np.arange(0, 900, 50))
    plt.title('0 - Healthy & 1 - Unhealthy')
    st.pyplot(fig_i)

    # Age vs BMI
    st.header('BMI Value Graph (Others vs Yours)')
    fig_bmi = plt.figure()
    sns.scatterplot(x='Age', y='BMI', data=df, hue='Outcome', palette='rainbow')
    sns.scatterplot(x=user_data['Age'], y=user_data['BMI'], s=150, color=color)
    plt.xticks(np.arange(10, 100, 5))
    plt.yticks(np.arange(0, 70, 5))
    plt.title('0 - Healthy & 1 - Unhealthy')
    st.pyplot(fig_bmi)

    # Age vs DPF
    st.header('DPF Value Graph (Others vs Yours)')
    fig_dpf = plt.figure()
    sns.scatterplot(x='Age', y='DiabetesPedigreeFunction', data=df, hue='Outcome', palette='YlOrBr')
    sns.scatterplot(x=user_data['Age'], y=user_data['DiabetesPedigreeFunction'], s=150, color=color)
    plt.xticks(np.arange(10, 100, 5))
    plt.yticks(np.arange(0, 3, 0.2))
    plt.title('0 - Healthy & 1 - Unhealthy')
    st.pyplot(fig_dpf)

    # OUTPUT
    st.subheader('Your Report:')
    output = 'You are not Diabetic' if user_result[0] == 0 else 'You are Diabetic'
    st.title(output)
    st.subheader('Accuracy:')
    accuracy = accuracy_score(y_test, rf.predict(x_test)) * 100
    st.write(f'{accuracy:.2f}%')

    # Streamlit UI for user input
    st.subheader('Send WhatsApp Report')
    user_name = st.text_input('Your Name')
    user_number = st.text_input('Your Phone Number (with country code)')

    if st.button('Send WhatsApp Report'):
        if user_name and user_number:
            send_whatsapp_report(user_name, user_number, user_result, accuracy)
        else:
            st.error('Please enter your name and phone number.')

# Function to send WhatsApp message report
def send_whatsapp_report(user_name, user_number, user_result, accuracy):
    import pywhatkit as kit
    from datetime import datetime

    # Message content
    if user_result[0] == 0:
        result = 'You are not Diabetic'
    else:
        result = 'You are Diabetic'
    message_body = f"Diabetes Checkup Report for {user_name}:\nResult: {result}\nAccuracy: {accuracy:.2f}%"
    
    # Current time
    now = datetime.now()
    hour = now.hour
    minute = now.minute + 2  # send message 2 minutes from now to give time for login

    # Sending the message
    kit.sendwhatmsg(f"+{user_number}", message_body, hour, minute)
    st.success('WhatsApp message scheduled successfully!')

if __name__ == "__main__":
    main()
