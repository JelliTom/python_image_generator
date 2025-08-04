from datetime import datetime
import time
import os
import uuid
from PIL import Image
import requests

class ImageGenerator:
    def __init__(self, api_url, dir_out="images", timeout=60):
        self.api_url = api_url
        self.dir_out = dir_out
        self.timeout = timeout

    def generate_image(self, prompt, prompt_file=False, force_new_img=False, open_on_done=False):

        raw_prompt = prompt

        if prompt_file:
            print(f"Attempting to open prompt file  {prompt}")
            try:
                with open(prompt, 'r') as file:
                    prompt = file.read().strip()
            except FileNotFoundError:
                print(f"Prompt file {prompt} not found. Please try again with a valid file.")
                return None

        prompt = prompt.replace(" ", "-")
        if force_new_img:
            unique_id = str(uuid.uuid4())
            prompt += unique_id

        request_url = f"{self.api_url}/{prompt}"

        start_time = time.time()
        time_now = time.time()

        while (time_now - start_time) < self.timeout:
            time_now = time.time()
            try:
                response = requests.get(request_url)
                if response.status_code == 200:
                    save_path_img = f"{self.dir_out}/{prompt}.png"
                    save_path_prompt = f"{self.dir_out}/{prompt}.txt"
                    os.makedirs(os.path.dirname(save_path_img), exist_ok=True)
                    try:
                        with open(save_path_img, 'wb') as f:
                            f.write(response.content)
                    except OSError as e:
                        current_time = datetime.now().strftime("%Y-%m-%d-T%H-%M-%S-%f")
                        save_path_img = f"{self.dir_out}/{current_time}.png"
                        save_path_prompt = f"{self.dir_out}/{current_time}.txt"
                        with open(save_path_img, 'wb') as f:
                            f.write(response.content)
                    # Crop watermark/artifacts (adjust as needed)
                    image = Image.open(save_path_img)
                    image = image.crop((0, 0, image.width, image.height - 48))
                    cropped_image = image.crop((0, 0, image.width, image.height - 100))
                    cropped_image.save(save_path_img)

                    ## Save your prompt as well
                    with open(f"{save_path_prompt}", 'w') as f:
                        f.write(raw_prompt)
                    if open_on_done:
                        im = Image.open(save_path_img)
                        im.show()
                    return save_path_img
                else:
                    print(f"Status code: {response.status_code}")
                    print(f"Response text: {response.text}")
                    print("Retrying...")
            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}. Retrying in 5 seconds...")
            time.sleep(5)  # Wait before retrying