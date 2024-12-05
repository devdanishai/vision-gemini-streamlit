#pip install google-generativeai==0.8.3
#pip install Pillow
#pip install python-dotenv

# Import required libraries
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Check if the API key is loaded properly
if not GOOGLE_API_KEY:
    raise ValueError("API key not found. Make sure the .env file contains the key.")

# Configure the API key
genai.configure(api_key=GOOGLE_API_KEY)

# Load images
image1 = Image.open("img.png")  # Replace with your image path
image2 = Image.open("img2.png") # Replace with your image path

# Initialize the model
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

# Create prompt and generate response
prompt = "Generate a list of all the objects contained in both images."
response = model.generate_content([image1, image2, prompt])

# Print the response
print(response.text)
