from streamlit.testing.v1 import AppTest
import requests

# Test 1: Test if exception occurs

def test_exception():
    at = AppTest.from_file("frontend/src/index.py").run()
    assert not at.exception

# Test 2: Test if prediction is made correctly

# def test_prediction_graph():
#     at = AppTest.from_file("frontend/src/index.py").run()

#     # Getting the image in bytes
#     with open("test_image.jpg", "rb") as f:
#         file_bytes = f.read()
    
#     # Mocking the response
#     response = requests.post("http://host.docker.internal:8000/upload", files={"file": ("test_image.jpg", file_bytes, "image/jpg")})
#     response = response.json()

#     
    
    
    