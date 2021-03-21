from django.forms import ModelForm

from .models import PollsList, PollDetail

class CreatePollForm(ModelForm):
    class Meta:
        model = PollsList
        fields = ['question']

class CreatePoll2Form(ModelForm):
    class Meta:
        model = PollDetail
        fields = '__all__'
