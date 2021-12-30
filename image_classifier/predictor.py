import torch
import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
import yaml
import cv2
import numpy as np
import albumentations as A
from albumentations.pytorch.transforms import ToTensorV2

class ImagePredictor:
    def __init__(self, model_path):
        self.model_name = 'testing_one'
        self.model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=False)
        self.num_classes = 4
        self.in_features = self.model.roi_heads.box_predictor.cls_score.in_features
        self.model.roi_heads.box_predictor = FastRCNNPredictor(self.in_features, self.num_classes)
        self.model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))

    @classmethod
    def init_model(cls, config_path):
        with open(config_path, "r") as f:
            config = yaml.load(f, yaml.SafeLoader)
        predictor = cls(model_path = config["model_path"])
        return predictor

    def load_image_from_file(self, file_object):
        image = cv2.imread(file_object, cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB).astype(np.float32)
        image /= 255.0
        # Albumentations library for transfors.
        def get_transforms():
            '''
            Uses the albulmentations library to transform images.
            Same transforms used for train and test
            Only uses resize.
            '''
            return A.Compose([
                A.Resize(200, 300),
                ToTensorV2(p=1.0)], bbox_params={'format': 'pascal_voc', 'label_fields': ['labels']})

        sample = {
            'image': image,
            'bboxes': [],
            'labels': []
        }
        transforms = get_transforms()
        sample = transforms(**sample)
        image = sample['image']
        return image

    def predict_image(self, image):
        device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        classes = {'b22': 1, 'gu10': 2, 'e27': 3}
        self.model.eval()
        outputs = self.model([image])

        # Case when no objects detected
        if len(outputs[0]['scores']) > 0:
            outputs = [{k: v.to(device) for k, v in t.items()} for t in outputs]

            for key, value in classes.items():
                if value == outputs[0]['labels'].cpu().numpy()[0]:
                    class_label = key

            prob = outputs[0]['scores'].cpu().detach().numpy()[0]
            output = {'type' : class_label,
                      'probability' : str(prob)}
            return output
        else:
            return {'message': 'No bulbs found'}
