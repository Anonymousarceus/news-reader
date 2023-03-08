import requests
import json
import pyttsx3
engine = pyttsx3.init()
r=requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=615b9073eb25486f8453f71bb2f1c000")
data=json.loads(r.content)
for i in range(20):
    news = data['articles'][i]['title']
    print('news',i+1,':',news)
    engine.say(news)
    engine.runAndWait()

