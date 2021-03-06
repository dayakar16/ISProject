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
1. You need to install all things in the requirements file: <br>
    <b> cd to project directory </b> <br>
    <b> pip install -r requirements.txt </b> <br>
2. You need to download punkt and stopwords package from nltk: <br>
      Go to terminal <br>
     <b> python </b> <br>
     <b> import nltk </b> <br>
     <b> nltk.download('punkt') </b> <br>
     <b> nltk.download('stopwords') </b> <br>
     <b> exit() </b> <br>
3. Run this command to start the uvicorn server in terminal: <br>
      <b>  uvicorn api:app --reload </b> <br>

## Output
### Examples of messages: 
#### Spam messages: 

congratulations you won 1000 dollars call on this number to get your prize
<br>
You could be entitled up to $5000 in compensation from mis-sold PPI on a credit card or Loan. Please reply PPI for in for STOP to opt out. 
<br>
A Loan for $3000 is approved for you if you receive this sms. 1 min verification & cash in 1 hr at ww.[redacted].co.uk to opt out reply stop 
<br>

#### Ham Messages: 

Did you see the match ? It was insane. 
<br>
I am dayakar, please call me back. 
<br>
Do you want to go to football match ? 
<br>

### Spam message: 
#### Request: 
{"message":"Congratulations!! you have won 1000 call on this number to get your prize"}
#### Response: 
{
    "Response": "Spam Message"
}
<br>
<img src="Images/Spam_message.JPG" alt="Spam Message">

### Ham message: 
#### Request: 
{"message":"I am dayakar, Please call me back"}
#### Response: 
{
    "Response": "Ham Message"
}
<br>
<img src="Images/Ham_message.JPG" alt="Ham Message">

