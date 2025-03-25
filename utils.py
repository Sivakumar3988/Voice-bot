#import required libraries
import openai
import os
import re
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("API_KEY")

# Predefined questions and responses with keyword matching
PREDEFINED_RESPONSES = {
    "life story": "I had a happy childhood until my father passed away when I was in 6th grade. As a child, it took me years to fully grasp the weight of that loss. Being the eldest, responsibilities gradually fell on me. I once dreamed of starting a food business with my friends, but it didn’t materialize. Later, I moved to Paris for my MBA, where life was tough—balancing part-time jobs with college, often running on just 3–4 hours of sleep. But whenever I had a break, I traveled across Europe, even visiting London. Traveling became my stress buster. However, due to family responsibilities, I had to return to India, putting an end to my travels. Despite everything, I thrive on challenges and keep pushing forward.",
    "superpower": "My #1 superpower is resilience—the ability to adapt, push through challenges, and keep moving forward no matter how tough life gets.",
    "grow": "The top 3 areas I'd like to grow in are: 1) Expanding expertise in AI and deep learning, 2) Enhancing leadership and project management skills, and 3) Mastering advanced cloud computing solutions.",
    "misconception": "A common misconception my coworkers have about me is that I’m always serious and work-focused. In reality, I enjoy having fun, love to travel, and appreciate a good laugh—I just balance it with my responsibilities.",
    "boundaries": "I push my boundaries by taking on challenges that scare me, whether it's moving to a new country, juggling multiple responsibilities, or learning new skills. I believe growth comes from discomfort, so I keep pushing myself to adapt, improve, and never settle."
}
#fetch response from openai
def get_openai_response(prompt):
    """Fetches response based on keywords in the input prompt."""
    for keyword, response in PREDEFINED_RESPONSES.items():
        if re.search(rf"\b{keyword}\b", prompt, re.IGNORECASE):
            return response
    return "I can only answer predefined questions. Please ask one from the list!"


