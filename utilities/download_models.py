import gdown
import os


def download_models():
    os.makedirs('./models/', exist_ok=True)

    
    # if os.path.exists('./models/plate-detector.pt'):
    #     print("plate-detector.pt exists.")
    # else:
    #     print("plate-detector.pt does not exist.")
    #     print("downloading ...")
    #     file_id = '1dpeNxaWAGFca9MmAGg3V9gtFAzUXsmHi'
    #     output_file = './models/plate-detector.pt'  # Change the extension as needed
    #     gdown_url = f'https://drive.google.com/uc?id={file_id}'
    #     gdown.download(gdown_url, output_file, quiet=False)
    
    if os.path.exists('./models/character-detector.pt'):
        print("character-detector.pt exists.")
    else:
        print("character-detector.pt does not exist.")
        print("downloading ...")
        file_id = '1SO4BeW8KCfftOf_JL1C073XLSNz3K6Hr'
        output_file = './models/character-detector.pt'  # Change the extension as needed
        gdown_url = f'https://drive.google.com/uc?id={file_id}'
        gdown.download(gdown_url, output_file, quiet=False)
