from ultralytics import YOLO
from utilities.download_models import download_models


download_models()

# model = YOLO("runs/detect/train10/weights/best.pt")
model = YOLO("./models/character-detector.pt")

# To Test on CPU:
results = model.predict(source='./data/images/test.jpg',  conf = 0.3, save=True, show = False, save_txt = False, device='cpu')








