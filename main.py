from fastapi import FastAPI
from dotenv import load_dotenv
from google import genai  # o: import google.generativeai as genai

app = FastAPI()
load_dotenv()

client = genai.Client()

@app.get("/llm/{prompt}")
async def read_root(prompt):
	response = client.models.generate_content(
		model="gemini-3-flash-preview",
		contents=prompt
	)
	print(response.text)
	return {"Respuesta": response.text}