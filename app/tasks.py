from celery import shared_task
from app.models import Article

import requests

from datetime import datetime, timedelta, time


@shared_task
def hello():
    print("Hello there!")


@shared_task
def getArticlesForDBInsert():

	newsSources = getNewsSources()

	for newsSource in newsSources:
		response = requests.get('http://newsapi.org/v2/top-headlines?sources=' + newsSource + '&apiKey=98ca432fa8434f888c48a3bd40fb7b6e')
		jsonData = response.json()
		articles = jsonData['articles']

		for article in articles:
			Article.objects.get_or_create(
				source=article['source']['name'],
				title=article['title'],
				author=article['author'],
				description=article['description'],
				publication_date=article['publishedAt'],
				url=article['url'],
				urlToImage=article['urlToImage'])



def getNewsSources():

	bbcNews = 'bbc-news'
	assocPress = 'associated-press'
	cbsNews = 'cbs-news'
	bloomberg = 'bloomberg'
	abcNews = 'abc-news'
	alJazeera = 'al-jazeera-english'
	axios = 'axios'
	cnn = 'cnn'
	msnbc = 'msnbc'
	foxNews = 'fox-news'
	nbcNews = 'nbc-news'
	newsweek = 'newsweek'
	natReview = 'national-review'
	politico = 'politico'
	reuters = 'reuters'
	time = 'time'
	guardian = 'the-guardian-uk'
	huffpo = 'the-huffington-post'
	nyTimes = 'the-new-york-times'
	wsj = 'the-wall-street-journal'
	washPost = 'the-washington-post'
	theHill = 'the-hill'
	usaToday = 'usa-today'

	newsSources = [bbcNews, assocPress, cbsNews, bloomberg, abcNews, alJazeera, axios, cnn, msnbc, foxNews, nbcNews, newsweek, natReview, politico, reuters, time, guardian, huffpo, nyTimes, wsj, washPost, theHill, usaToday]

	return newsSources



