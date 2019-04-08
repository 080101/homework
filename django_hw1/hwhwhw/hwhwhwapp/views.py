# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

#counting words
dic = {}
def result(request):
    given_sentence = request.GET['fulltext']
    splited_sentence = given_sentence.split()
    length = len(splited_sentence)

    for i in splited_sentence:
        if i in dic:
            #dic에 splited_sentence[i]의 value 값 + 1
            dic[i] += 1
        else:
            #dic에 splited_sentence[i]에 key & value 쌍 추가
            dic[i] = 1
            return render(request, 'result.html', {
                'length': length,
                'text': given_sentence,
                'result': dic
            })


