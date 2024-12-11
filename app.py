import streamlit as st
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
    st.error("API key not found. Make sure the .env file contains the key.")
else:
    # Configure the API key
    genai.configure(api_key=GOOGLE_API_KEY)

    # Streamlit app
    st.title("Image Analyzer")

    # Sidebar with use cases
    st.sidebar.title("Use Cases")
    use_cases = [
        "Object Detection and Recognition",
        "Image Classification",
        "Facial Recognition and Analysis",
        "Scene Understanding",
        "Anomaly Detection",
        "Content Moderation",
        "Image Search and Retrieval",
        "Medical Imaging Analysis",
        "Augmented Reality Integration",
        "Quality Control in Manufacturing",
        "Environmental Monitoring",
        "Optical Character Recognition (OCR)",
        "Traffic Monitoring and Analysis",
        "Product Recommendation Systems",
        "Sentiment Analysis through Images",
    ]
    for use_case in use_cases:
        st.sidebar.write(f"- {use_case}")

    # File uploader for one image
    uploaded_image = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

    # Analyze image button
    if uploaded_image:
        # Display the uploaded image
        st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)

        # Analyze button
        if st.button("Analyze Image"):
            # Convert uploaded file to a PIL Image
            image = Image.open(uploaded_image)

            # Initialize the model
            model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

            # Create prompt and generate response
            prompt = "Generate a list of all the objects contained in this image."
            response = model.generate_content([image, prompt])

            # Display the analysis result
            st.subheader("Analysis Result:")
            st.write(response.text)
