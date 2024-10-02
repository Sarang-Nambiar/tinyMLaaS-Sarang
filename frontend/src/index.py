import streamlit as st

import requests

import time 

import pandas as pd

# defining helper functions

def extract_predictions(output):
    output = output.strip().split() # removing leading and trailing whitespaces and splitting the string
    return [float(i) for i in output]

# function to get the prediction number
def get_prediction_number(probabilities):
    return probabilities.index(max(probabilities))

# Defining Constants

BASE_URL = "http://host.docker.internal:8000"

# setting page configuration
st.set_page_config(
    page_title="TinyMLaas",
    page_icon="⚛️",
)

st.markdown("""
            # Welcome to my Streamlit App
            This is a simple application which would predict the number in the image uploaded. \n
            Please upload an image to get started
""")

predicted = False

input_file = st.file_uploader("Upload an Image", type="jpg", accept_multiple_files=False)

#checking if the file is uploaded
if input_file is not None:
    col1, col2 = st.columns((7, 1))
    if col2.button("Predict"):

        file_bytes = input_file.getvalue()

        with st.spinner("Uploading..."):

            file_upload = requests.post(f"{BASE_URL}/upload", 
                                    files={"file": (input_file.name, file_bytes, "image/jpg")})
        start_time = time.time()
        
        response = file_upload.json()
        # st.write(response) # for debugging purposes
        if response:
            if "prediction" in response:
                with st.spinner("Predicting..."):
                    col1, col2 = st.columns((1, 3)) # defining the layout
                    col1.markdown("**Uploaded Image**")
                    col1.image(input_file, caption="Uploaded Image", use_column_width=True)

                    col2.markdown("**Prediction Bar Chart**")
                    output = response["prediction"]

                    probabilities = extract_predictions(output)
                    predictions = {
                        "Number": [i for i in range(10)],
                        "Probability": probabilities
                    }
                    predictions = pd.DataFrame(predictions)
                    col2.bar_chart(predictions,x="Number", y="Probability", use_container_width=True)
                    st.write("According to the model, the number in the image is: ", get_prediction_number(probabilities))
                    st.write("Time taken: ", time.time() - start_time)
                    predicted = True
            elif "error" in response:
                st.error(f"Error: {response['error']}. Please try again with a different image")
        else:
            st.error("Error: Network Error! No response from the server")