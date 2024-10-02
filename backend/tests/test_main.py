import requests
import subprocess
import os

# Running main.py
os.chdir("../app")
p = subprocess.Popen(["uvicorn", "main:app", "--reload"])

# Testing the startup of API
def test_startup():
    response = requests.get("http://localhost:8000")
    assert response.json() == {"message": "Welcome to TinyMLaaS"}

def test_file_upload():
    os.chdir("../tests")
    with open("test_image.jpg", "rb") as f:
        file_bytes = f.read()
    
    response = requests.post("http://localhost:8000/upload", files={"file": ("test_image.jpg", file_bytes, "image/jpg")})

    assert "prediction" in response.json()

    with open("blank.pdf", "rb") as f:
        file_bytes = f.read()
    # Testing if the model returns an error after passing non image type file
    response = requests.post("http://localhost:8000/upload", files={"file": ("blank.pdf", file_bytes, "application/pdf")})
    assert "error" in response.json()
    p.terminate()
    