# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.http import HttpResponse, JsonResponse

from .serializers import PollSerializer, DetailSerializer

# from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from rest_framework.decorators import api_view


# Create your views here.


from .forms import CreatePollForm, CreatePoll2Form
from .models import PollsList, PollDetail

class Poll():
    def poll_list(request):

            polls = PollsList.objects.all()
            context = {'polls' : polls}
            return render(request, 'poll/home.html', context)

    def vote(request, poll_id):
            poll = PollsList.objects.get(pk=poll_id)
            poll2 = PollDetail.objects.get(poll_id=poll_id)
            if request.method == 'POST':
                selected_option = request.POST['poll']
                if selected_option == 'option1':
                    poll2.option_one_count += 1
                elif selected_option == 'option2':
                    poll2.option_two_count += 1
                elif selected_option == 'option3':
                    poll2.option_three_count += 1
                else:
                    return HttpResponse(400, 'Invalid form')
                #print(request.POST['poll'])

                poll2.save()

                return redirect('results', poll_id)
            context = {
            'poll2' : poll2,
            'poll' : poll
            }
            return render(request, 'poll/vote.html', context)


    def poll_detail(request, poll_id):
            poll = PollsList.objects.get(pk=poll_id)
            poll2 = PollDetail.objects.get(poll_id=poll_id)
            context = {
            'poll' : poll,
            'poll2' : poll2
            }
            return render(request, 'poll/results.html', context)

class Poll_json():
    @api_view(('GET',))

    def home_json(request):
            polls = PollsList.objects.all()
            serializer_obj = PollSerializer(polls, many=True)

            return Response(serializer_obj.data)


    @api_view(('GET',))
    def results_json(request, poll_id):

            poll2 = PollDetail.objects.get(poll_id=poll_id)

            serializer_obj = DetailSerializer(poll2)
            return Response(serializer_obj.data)

             # # Creating another pole option attempt 
    # def create(request):
    #         if request.method == "POST":
    #             poll = CreatePollForm(request.POST)
    #             form = CreatePoll2Form(request.POST)
    #             if form.is_valid() and poll_q.is_valid():
    #                 form.save()
    #                 poll.save()
    #                 return redirect('home')
    #                 #test
    #                 # print(form.cleaned_data['question'])
    #         else:
    #             form = CreatePoll2Form()
    #             poll = CreatePollForm()
            #
            # context = {
            # 'form' :  form,
            # 'poll' : poll
            # }
            # return render(request, 'poll/create.html', context)
