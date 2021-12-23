import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
import ast
import torch
import torchvision
from torchvision.models.detection.faster_rcnn import FasterRCNN
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
import albumentations as A
from albumentations.pytorch.transforms import ToTensorV2
from torch.utils.data import DataLoader, Dataset

class ImagePredictor:
    def __init__(self):
        self.model_name = 'testing_one'

    @classmethod
    def simple_model(self):
        return {"message": 'ha'}


