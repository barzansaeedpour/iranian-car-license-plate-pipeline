from ultralytics import YOLO
import gdown

# file_id = '1A2B3C4D5E6F7G8H9I0J'
output_file = 'my_downloaded_file.pt'  # Change the extension as needed
# gdown_url = f'https://drive.google.com/uc?id={file_id}'
gdown_url = 'https://drive.google.com/file/d/1dpeNxaWAGFca9MmAGg3V9gtFAzUXsmHi/view?usp=drive_link'
gdown.download(gdown_url, output_file, quiet=False)


# model = YOLO("./models/character-detector.pt")

# results = model.predict(source='./data/videos/test.mp4',  conf = 0.2, save=True, show = False, save_txt = False, device='cpu')











