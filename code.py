import openai
import os
from PIL import Image
import requests
from io import BytesIO

def generate_image(prompt, output_path="generated_image.png"):
    """
    Generates an image from text using OpenAI's DALL·E API.
    """
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        
        image_url = response["data"][0]["url"]
        img_data = requests.get(image_url).content
        
        with open(output_path, "wb") as img_file:
            img_file.write(img_data)
        
        print(f"Image saved as {output_path}")
        
        return output_path
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    user_prompt = input("Enter a description for the image: ")
    img_path = generate_image(user_prompt)
    
    if img_path:
        img = Image.open(img_path)
        img.show()
