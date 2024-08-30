import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import streamlit as st
import numpy as np

# Mock data generation
np.random.seed(42)
data_size = 100

mock_data = {
    'AnimalAge': np.random.randint(1, 10, data_size),
    'Weight': np.random.uniform(2, 50, data_size),
    'BodyTemperature': np.random.uniform(37, 40, data_size),
    'LastClinicVisitMonthDue': np.random.randint(1, 12, data_size),
    'BowlFrequency': np.random.randint(1, 5, data_size),
    'FoodIntakeFrequency': np.random.randint(1, 4, data_size),
    'VisitClinic': np.random.choice([0, 1], data_size)
}

df = pd.DataFrame(mock_data)

# Split the data into features (X) and target variable (y)
X = df.drop('VisitClinic', axis=1)
y = df['VisitClinic']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a random forest classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Display accuracy on the test set
accuracy = accuracy_score(y_test, y_pred)
st.write(f"Model Accuracy: {accuracy * 100:.2f}%")

# Streamlit app
st.title("Animal Clinic Visit Prediction")

# Sidebar with user input
st.sidebar.header("Enter Animal Information")
animal_age = st.sidebar.slider("Animal Age", 1, 10, 5)
weight = st.sidebar.slider("Weight", 2.0, 50.0, 25.0)
body_temperature = st.sidebar.slider("Body Temperature", 37.0, 40.0, 38.5)
last_clinic_visit_month_due = st.sidebar.slider("Last Clinic Visit Month Due", 1, 12, 6)
bowl_frequency = st.sidebar.slider("Bowl Frequency", 1, 5, 3)
food_intake_frequency = st.sidebar.slider("Food Intake Frequency", 1, 4, 2)

# Predict whether to visit the clinic or not
input_data = {
    'AnimalAge': animal_age,
    'Weight': weight,
    'BodyTemperature': body_temperature,
    'LastClinicVisitMonthDue': last_clinic_visit_month_due,
    'BowlFrequency': bowl_frequency,
    'FoodIntakeFrequency': food_intake_frequency
}

input_df = pd.DataFrame([input_data])
prediction = clf.predict(input_df)

# Display the prediction result
st.header("Prediction:")
if prediction[0] == 1:
    st.write("Visit the clinic.")
    st.subheader("Find Nearest Clinics Near You")
    st.write("https://my.atlist.com/map/dc48ced5-f3ef-481d-bbc7-2634da55800a?share=true")
else:
    st.write("No need to visit the clinic.")
