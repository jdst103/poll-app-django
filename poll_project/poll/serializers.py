from rest_framework import serializers
#taking model and transfering to other format or share it somwwhere as you cannot save python obljects. in a format you cantrandferr

from .models import PollsList, PollDetail


class PollSerializer(serializers.ModelSerializer):

    class Meta:
        model = PollsList
        fields = ['question']
        # #oraa want to use all model
        # fields = '__all__'

class DetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = PollDetail
        # fields = ['question']
        # #oraa want to use all model
        fields = '__all__'
