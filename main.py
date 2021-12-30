import os.path
import yaml
from fastapi import FastAPI, File, UploadFile
import wget

from image_classifier.predictor import ImagePredictor

app = FastAPI()

predictor_config_path = 'config.yaml'
with open(predictor_config_path, "r") as f:
    config = yaml.load(f, yaml.SafeLoader)

# download the weights if the weights aren't already there.
local_file = 'image_classifier/weights/model_weights_4.pth'

if os.path.exists(local_file):
    print('File already exists')
else:
    # Define the remote file to retrieve
    remote_url = "https://github.com/AndrewWalker251/lightbulb_app/releases/download/v0.0.1/model_weights_4.pth"
    # Make http request for remote file data
    wget.download(remote_url, local_file)

# Create the predictor instance.
predictor = ImagePredictor.init_model(predictor_config_path)

# image = predictor.load_image_from_file(config['image_to_test_path'])
# output = predictor.predict_image(image)
# print(output)

@app.post("/predictbulb/")
def create_upload_file(file: UploadFile = File(...)):
    image = predictor.load_image_from_file(config['image_to_test_path'])
    output = predictor.predict_image(image)
    return output

