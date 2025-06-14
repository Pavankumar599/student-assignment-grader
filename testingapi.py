from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")




client = OpenAI(api_key=OPENAI_API_KEY)

try:
    models = client.models.list()
    print("✅ API key is valid. Models:")
    for model in models.data[:5]:  # display first 5 models
        print(model.id)
except OpenAI.AuthenticationError:
    print("❌ Invalid API key.")
except Exception as e:
    print(f"⚠️ Something went wrong: {e}")
