from email import message
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

class Item(BaseModel):
    message: str

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))


app = FastAPI()


@app.get("/")
async def root():
    return {"Welcome to spam Filtering Api, Please provide your content in http post request method in body message attribute to determine whether it is spam or ham"}

@app.post("/")
async def create_item(item: Item):
    item_dict = item.dict()
    print(item_dict)
    input_sms = item_dict['message'] 
     # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    print(vector_input)
    result = model.predict(vector_input)[0]
    # 4. Display
    print(result)
    if result == 1: 
        return {"Response":"Spam Message"}
    else:
        return {"Response": "Ham Message"}