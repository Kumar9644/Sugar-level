import streamlit as st
from joblib import *
model=load('glucose.h5')
def prediction():
    st.image('logo.png',width=450)
    st.markdown('Please fill the information below')
    age=st.number_input('Enter your age:')
    pregnancy=st.number_input('No of times you have been pregnant:')
    bp=st.number_input('Enter your diastolic blood pressure(diastolic):')
    skin=st.number_input('Enter skin thickness(if you are not sure please select 25):')
    insulin=st.number_input('Insulin level:')
    bmi=st.number_input('Enter your BMI:')
    b=st.button('Check sugar level:')

    if b:
        arr=[[pregnancy,bp,skin,insulin,bmi,age]]
        y_pred=model.predict(arr)[0]
        if y_pred>=90 and y_pred<=150:
            st.write(y_pred)
            st.write('Normal sugar level')
        elif y_pred>150 and y_pred <=240:
            st.write(y_pred)
            st.write('You have high sugar level.Please reduce sugar intake.')
        elif y_pred>240:
            st.write(y_pred)
            st.write('Your sugar level is exceptionally high. Please consult a doc.')

if __name__ == '__main__':
    prediction()