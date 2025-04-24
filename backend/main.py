from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

# Set your OpenAI API Key
openai.api_key = "your_openai_api_key"  # Replace this with your actual key

app = FastAPI()

class Question(BaseModel):
    query: str

@app.post("/ask")
async def ask(question: Question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question.query}
        ]
    )
    answer = response.choices[0].message.content
    return {"question": question.query, "answer": answer}
