import os
from groq import Groq
from dotenv import load_dotenv


os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY") 
def generate_response(user_input):
    client = Groq()
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ],
        model="llama3-70b-8192",
        temperature=0.5,
        max_tokens=1024,
        top_p=1
    )

    completion = response.choices[0].message.content
    return completion
