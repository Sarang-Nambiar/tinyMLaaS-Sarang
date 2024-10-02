import os
from fastapi import FastAPI, UploadFile, File
import subprocess

app = FastAPI()

# Comment this out when running for testing
os.chdir("app") # changing the directory to the model directory

@app.get("/")
def root():
    return {"message": "Welcome to TinyMLaaS"}

# Running the model on the uploaded image
@app.post("/upload")
async def get_uploaded_image(file: UploadFile = File(...)):
    try:
        if not file:
            return {"error": "File not found"}
        
        if file.content_type != "image/jpg":
            return {"error": "File is not an image"}
        
        # Save the file
        with open(os.path.join(os.getcwd(), "uploaded_image.jpg"), "wb") as buffer:
            contents = await file.read()
            buffer.write(contents)

        # Run the model
        try:
            output = subprocess.run(["./run", "uploaded_image.jpg"], capture_output=True, text=True, timeout=15) # add wsl if running on windows
            
            # Usually related to model being unable to read the image
            if output.stderr:
                return {"error": output.stderr}
            
            return {"prediction": output.stdout}
        except subprocess.TimeoutExpired:
            return {"error": "Model took too long to respond"}
    except Exception as e:
        return {"error": str(e)}