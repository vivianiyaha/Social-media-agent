import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_content():
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "user",
                    "content": "Write a short engaging social media post about tech innovation with emojis"
                }
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print("AI failed, using fallback:", e)
        return "🚀 Stay ahead with innovation! #Tech #AI"
