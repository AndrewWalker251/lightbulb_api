import os.path
import yaml
from fastapi import FastAPI, File, UploadFile
import wget
import time

from image_classifier.predictor import ImagePredictor

app = FastAPI()

predictor_config_path = 'config.yaml'
with open(predictor_config_path, "r") as f:
    config = yaml.load(f, yaml.SafeLoader)

# download the weights if the weights aren't already there.
local_file = 'lightbulb_app/image_classifier/weights/model_weights_4.pth'
print(os.getcwd())
print([x[0] for x in os.walk(os.getcwd())])
if os.path.exists(local_file):
    print('Weights already exist')
else:
    # Create weights folder
    print('Downloading weights')
    # Define the remote file to retrieve
    remote_url = "https://github.com/AndrewWalker251/lightbulb_app/releases/download/v0.0.1/model_weights_4.pth"
    # Test finding the location that's got
    # Make http request for remote file data

    import urllib.request
    urllib.request.urlretrieve(remote_url, local_file)


    #wget.download(remote_url, local_file)

while 'model_weights_4.pth' not in os.listdir('lightbulb_app/image_classifier/weights/'):
    print(os.listdir(''))
    print('waiting')
    time.sleep(20)

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

