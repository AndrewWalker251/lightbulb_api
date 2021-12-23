from fastapi import FastAPI, File, UploadFile

from image_classifier.predictor import ImagePredictor

app = FastAPI()

predictor = ImagePredictor()

@app.post("/scorefile/")
def create_upload_file(file: UploadFile = File(...)):
    return predictor.simple_model()
