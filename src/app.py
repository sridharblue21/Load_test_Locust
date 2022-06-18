from fastapi import FastAPI
import uvicorn
from textblob import TextBlob


app = FastAPI()

@app.get('/')
async def index():
    return {"text": "hello world"}

@app.get('/sentiment/{text}')
async def get_sentiment(text):
    blob = TextBlob(text).sentiment
    return { "text" : text, "polarity": blob.polarity, "subjectivity": blob.subjectivity}



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)