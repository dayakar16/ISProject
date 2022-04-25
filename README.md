## Spam Filtering Api 
This is a spam filtering api to detect whether the given message is spam or not. We found the good performing algorthims such as multinomial Navie Bayes, Logistic Regression, Support vector clasifier to compare the accuracy and precision and to find the better algorithm to detect the content whether it is spam or not. Later, we observed that Multinomial Naive Bayes gave 97% accuracy and 1.0 precision for this particular data sets. Hence, we can say clearly for the spam message containing words in this particular data set. it detects 97% of them. Therefore, we selected Multinomial Naive Bayes algorithm to predict it. 

This api consists of only two request: 
### Get request. 
This is like hompage request for this api and it shows the welocming message as below in json format. 
#### Response : 
["Welcome to spam Filtering Api, Please provide your content in post request body message attribute to determine whether it is spam or ham"]
### Post Request. 
This is the request where user sends his message or context to check whether it is spam or not. The user must sends his message in the json format and in the message attribute and in the post request body. 
as below: 
#### Request body: 
{"message":"Congratulations!! you have won 1000 call on this number to get your prize"}

#### Response: 
{
    "Response": "Spam Message"
}

## Setup 
1. You should have pip and python installed in your system and python interpreter should be selected based on your virtual environment or whatever the version you have installed it.  
2. Visual studio or Py charm or any other text editors should be installed. 
3. Postman should be installed to test this application . 

## Execution
1. You need to install all things in the requirements file:
    <b> cd to project directory </b>
    <b> pip install -r requirements.txt </b>
2. You need to download punkt and stopwords package from nltk: 
      Go to terminal 
     <b> python </b>
     <b> import nltk </b>
     <b> nltk.download('punkt') </b>
     <b> nltk.download('stopwords') </b>
     <b> exit() </b>
3. Run this command to start the uvicorn server in terminal:
      <b>  uvicorn api:app --reload </b>

## Output
### Spam message: 
#### Request: 
{"message":"Congratulations!! you have won 1000 call on this number to get your prize"}
#### Response: 
{
    "Response": "Spam Message"
}
<img src="Images/Spam_message.jpg" alt="Spam Message">

### Ham message: 
#### Request: 
{"message":"I am dayakar, Please call me back"}
#### Response: 
{
    "Response": "Ham Message"
}
<img src="Images/Ham_message.jpg" alt="Ham Message">

