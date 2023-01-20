from django.shortcuts import render,HttpResponse
import random

topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ... '},
    {'id':2, 'title':'view', 'body':'view is ... '},
    {'id':3, 'title':'model', 'body':'model is ... '},
]

def HTMLTemplate(articleTag):
    global topics
    ol = '' 
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</li>'
    return f'''
        <html>
        <body>
            <h1><a href="/">Django</a></h1>
            <ol>
                {ol}
            </ol>
            {articleTag}
            <a href="/create/">create</a>
        </body>
        </html>
    '''

def index(request):
    article = '''
        <h2>Welcome</h2>
        Hello, Django 
    '''
    return HttpResponse(HTMLTemplate(article))
    
def read(request,id):
    global topics
    article = ''
    for topic in topics :
        print(type(topic['id']), type(id))
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article)) 

# def index(request):
#     return HttpResponse('<h1>Random</h1>'+str(random.random()))

def create(request):
    article = '''
        <form action="/create/" method="post">
            <p><input type ="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit"></p>
        </form>
    '''
    return HttpResponse(HTMLTemplate(article))
