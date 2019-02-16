from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html') #render는 3개의 인자까지 받을 수 있음(request, templete의 이름, 딕셔너리형 자료형)

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()    #단어들이 담겨있는 List
    word_dictionary = {}

    for word in words:
        if word in word_dictionary :
            #increase
            word_dictionary[word] += 1 #key값을 1 증가
        else :
            #add to dictionary
            word_dictionary[word] = 1   #key값을 1 부여

    return render(request, 'result.html', {'full': text, 'total' : len(words), 'dictionary' : word_dictionary.items()})