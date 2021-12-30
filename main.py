import yaml
from fastapi import FastAPI, File, UploadFile

from image_classifier.predictor import ImagePredictor

app = FastAPI()

predictor_config_path = 'config.yaml'
with open(predictor_config_path, "r") as f:
    config = yaml.load(f, yaml.SafeLoader)

predictor = ImagePredictor.init_model(predictor_config_path)

# image = predictor.load_image_from_file(config['image_to_test_path'])
# output = predictor.predict_image(image)
# print(output)

@app.post("/predictbulb/")
def create_upload_file(file: UploadFile = File(...)):
    image = predictor.load_image_from_file(config['image_to_test_path'])
    output = predictor.predict_image(image)
    return output

