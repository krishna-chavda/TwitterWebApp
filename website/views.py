from django.shortcuts import render, redirect
from TwitterAPI import TwitterAPI, TwitterPager
from django.core.paginator import Paginator

import tweepy


def welcome(req):
    consumer_key="dtx8kK5htaHuwgj1ZWPmjXs9f"
    consumer_secret="dkAdmTPeOmdGvmT6g7cM7pkjwuikWmDMZZDkBa4YWEcQDkbbjX"
    access_token="1511235937572847616-D5tQamjCIAp6qvuHSN5sIqk5KKRMfs"
    access_token_secret="1BUVdHOR3JhdLZeOfoMKB5hlG4M9KRdjYV1jP51gpV10U"
# authorization of consumer key and consumer secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret
    auth.set_access_token(access_token, access_token_secret)

# calling the api
    api = tweepy.API(auth)

# the ID of the user
    _id = 1515719702395645954

# fetching the user
    user = api.get_user(userid=_id)

# fetching the followers_count
    followers_count = user.followers_count

    print("The number of followers of the user are : " + str(followers_count))
    return render(req, 'welcome.html')


def recent_tweets(req):
    a1 = []
    if req.method == 'POST':
        data = req.POST.get('word', False)

        api = TwitterAPI(

            consumer_key="dtx8kK5htaHuwgj1ZWPmjXs9f",
            consumer_secret="dkAdmTPeOmdGvmT6g7cM7pkjwuikWmDMZZDkBa4YWEcQDkbbjX",
            access_token_key="1511235937572847616-D5tQamjCIAp6qvuHSN5sIqk5KKRMfs",
            access_token_secret="1BUVdHOR3JhdLZeOfoMKB5hlG4M9KRdjYV1jP51gpV10U",
            api_version='2')
        r = api.request('tweets/search/recent', {
            'query': data,
            'tweet.fields': 'author_id',
            'expansions': 'author_id'})

        for item in r:
            f = item
            a1.append(f)
    #    print(a1)

    return render(req, 'recent_tweets.html', {'a1': a1})


def search_tweets(req):
    a1 = []
    if req.method == 'POST':
        data = req.POST.get('tweet')
        api = TwitterAPI(

            consumer_key="dtx8kK5htaHuwgj1ZWPmjXs9f",
            consumer_secret="dkAdmTPeOmdGvmT6g7cM7pkjwuikWmDMZZDkBa4YWEcQDkbbjX",
            access_token_key="1511235937572847616-D5tQamjCIAp6qvuHSN5sIqk5KKRMfs",
            access_token_secret="1BUVdHOR3JhdLZeOfoMKB5hlG4M9KRdjYV1jP51gpV10U",
            api_version='2')
        r = api.request(f'tweets/:{data}')

        for item in r:
            f = item
            a1.append(f)

    return render(req, 'search_tweets.html', {'a1': a1})


def find(req):
    a1 = []
    if req.method == 'POST':

        data = req.POST.get('uname')
        api = TwitterAPI(

            consumer_key="dtx8kK5htaHuwgj1ZWPmjXs9f",
            consumer_secret="dkAdmTPeOmdGvmT6g7cM7pkjwuikWmDMZZDkBa4YWEcQDkbbjX",
            access_token_key="1511235937572847616-D5tQamjCIAp6qvuHSN5sIqk5KKRMfs",
            access_token_secret="1BUVdHOR3JhdLZeOfoMKB5hlG4M9KRdjYV1jP51gpV10U",
            api_version='2')
        r = api.request(f'users/by/username/:{data}')
        for item in r:
            f = item
            a1.append(f)

    return render(req, 'find.html', {'a1': a1})


def follower(req):
    a1 = []
    if req.method == 'GET':
        USER_ID = req.GET.get('q')
        # USER_ID = '1115566340859813888'
        a1 = []
        api = TwitterAPI(

            consumer_key="dtx8kK5htaHuwgj1ZWPmjXs9f",
            consumer_secret="dkAdmTPeOmdGvmT6g7cM7pkjwuikWmDMZZDkBa4YWEcQDkbbjX",
            access_token_key="1511235937572847616-D5tQamjCIAp6qvuHSN5sIqk5KKRMfs",
            access_token_secret="1BUVdHOR3JhdLZeOfoMKB5hlG4M9KRdjYV1jP51gpV10U",
            api_version='2')
        r = api.request(f'users/:{USER_ID}/followers')
        for item in r:
            f = item
            a1.append(f)

    follower_paginator = Paginator(a1, 10)
    page_num = req.GET.get('page')
    page = follower_paginator.get_page(page_num)
    context = {
        'count': follower_paginator.count,
        'page': page,
        'userid': USER_ID

    }

    return render(req, 'follower.html', context)


def following(req):
    a1 = []
    if req.method == 'GET':
        USER_ID = req.GET.get('q')
        a1 = []
        api = TwitterAPI(

            consumer_key="dtx8kK5htaHuwgj1ZWPmjXs9f",
            consumer_secret="dkAdmTPeOmdGvmT6g7cM7pkjwuikWmDMZZDkBa4YWEcQDkbbjX",
            access_token_key="1511235937572847616-D5tQamjCIAp6qvuHSN5sIqk5KKRMfs",
            access_token_secret="1BUVdHOR3JhdLZeOfoMKB5hlG4M9KRdjYV1jP51gpV10U",
            api_version='2')
        r = api.request(f'users/:{USER_ID}/following')
        for item in r:
            f = item
            a1.append(f)

    follower_paginator = Paginator(a1, 10)
    page_num = req.GET.get('page')
    page = follower_paginator.get_page(page_num)
    context = {
        'count': follower_paginator.count,
        'page': page,
        'userid': USER_ID

    }

    return render(req, 'following.html', context)


def tweets(req):
    a1 = []
    if req.method == 'GET':
        USER_ID = req.GET.get('q')

        api = TwitterAPI(

            consumer_key="dtx8kK5htaHuwgj1ZWPmjXs9f",
            consumer_secret="dkAdmTPeOmdGvmT6g7cM7pkjwuikWmDMZZDkBa4YWEcQDkbbjX",
            access_token_key="1511235937572847616-D5tQamjCIAp6qvuHSN5sIqk5KKRMfs",
            access_token_secret="1BUVdHOR3JhdLZeOfoMKB5hlG4M9KRdjYV1jP51gpV10U",
            api_version='2')
        r = api.request(f'users/:{USER_ID}/tweets')
        for item in r:
            f = item
            a1.append(f)

    return render(req, 'tweets.html', {'a1': a1})


def all(req):
    a1 = []
    if req.method == 'GET':
        USER_ID = req.GET.get('q')
        a1 = []
        api = TwitterAPI(

            consumer_key="dtx8kK5htaHuwgj1ZWPmjXs9f",
            consumer_secret="dkAdmTPeOmdGvmT6g7cM7pkjwuikWmDMZZDkBa4YWEcQDkbbjX",
            access_token_key="1511235937572847616-D5tQamjCIAp6qvuHSN5sIqk5KKRMfs",
            access_token_secret="1BUVdHOR3JhdLZeOfoMKB5hlG4M9KRdjYV1jP51gpV10U",
            api_version='2')
        r = api.request(f'users/:{USER_ID}/following')
        for item in r:
            f = item
            a1.append(f)

    return render(req, 'following.html', {'a1': a1})


def refollowing(req):
    a1 = []
    if req.method == 'GET':

        data = req.GET.get('q')
        api = TwitterAPI(

            consumer_key="dtx8kK5htaHuwgj1ZWPmjXs9f",
            consumer_secret="dkAdmTPeOmdGvmT6g7cM7pkjwuikWmDMZZDkBa4YWEcQDkbbjX",
            access_token_key="1511235937572847616-D5tQamjCIAp6qvuHSN5sIqk5KKRMfs",
            access_token_secret="1BUVdHOR3JhdLZeOfoMKB5hlG4M9KRdjYV1jP51gpV10U",
            api_version='2')
        r = api.request(f'users/by/username/:{data}')
        for item in r:
            f = item
            a1.append(f)

    return render(req, 'refollowing.html', {'a1': a1})


def refollower(req):
    a1 = []
    if req.method == 'GET':

        data = req.GET.get('q')
        api = TwitterAPI(

            consumer_key="dtx8kK5htaHuwgj1ZWPmjXs9f",
            consumer_secret="dkAdmTPeOmdGvmT6g7cM7pkjwuikWmDMZZDkBa4YWEcQDkbbjX",
            access_token_key="1511235937572847616-D5tQamjCIAp6qvuHSN5sIqk5KKRMfs",
            access_token_secret="1BUVdHOR3JhdLZeOfoMKB5hlG4M9KRdjYV1jP51gpV10U",
            api_version='2')
        r = api.request(f'users/by/username/:{data}')
        for item in r:
            f = item
            a1.append(f)

    return render(req, 'refollower.html', {'a1': a1})
