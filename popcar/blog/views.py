from django.shortcuts import render
import requests
from django.http import JsonResponse
import json
from operator import attrgetter

def home(request):
	params = (
    	('q', 'topic:php'),
	)
	rr = respo(params)
	return JsonResponse(rr, safe=False)

def stars(request):
	params = (
    	('q', 'topic:php'),
    	('sorted', 'stars'),
	)
	rr = respo(params)
	return JsonResponse(rr, safe=False)

def updated(request):
	params = (
    	('q', 'topic:php'),
    	('sorted', 'updated'),
	)
	rr = respo(params)
	return JsonResponse(rr, safe=False)

#def sortt(package):
	#return package['stars']

def respo(paramz):
	r1 = requests.get('https://api.github.com/search/repositories', params=paramz).json()
	#r2 = r1.sorted(key=attrgetter('stars'))
	return r1