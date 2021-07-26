import re
import challenges
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no Meat for a month in jan !",
    "february": "Walk at least 10k everyday in feb !",
    "march": "Learn Django for 20 mins in mar!",
    "april": "Eat no Meat for a month in apr!",
    "may": "Walk at least 10k everyday in may!",
    "june": "Learn Django for 20 mins  in jun!",
    "july": "Eat no Meat for a month in jul!",
    "august": "Walk at least 10k everyday in aug!",
    "september": "Learn Django for 20 mins in sep !",
    "october": "Eat no Meat for a month in oct !",
    "november": "Walk at least 10k everyday in nov!",
    "december": "Learn Django for 20 mins in dec!"
}

# Create your views here.

def index(reqeust):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\"> {capitalized_month}</a></li>"
    
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month - 1]
    redirect_path= reverse("month-challenge", args=[redirect_month]) #/challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported<h1>")