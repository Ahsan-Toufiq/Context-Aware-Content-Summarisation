# ContentGenerator.py
import google.generativeai as genai

class ContentGenerator:
    """Generates content using Google's Generative AI model."""

    # Initialize the Gemini AI model
    def __init__(self, api_key):
        genai.configure(api_key="AIzaSyBUG_6Y27wVVMLLTE7LFAD3Fs6NTGje2z0")
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def generate_content(self, text):
        """Generates content based on the provided text."""
        return self.model.generate_content(text)
