

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from forms_project.forms.models import (
    Questionnaire,
    Question,
    Response,
    QuestionOption,
    SelectedOption,
    WrittenAnswer,
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Questionnaire
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Question
        fields = '__all__'

class ResponseSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Response
        fields = '__all__'

class QuestionOptionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = QuestionOption
        fields = '__all__'

class SelectedOptionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = SelectedOption
        fields = '__all__'

class WrittenAnswerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = WrittenAnswer
        fields = '__all__'
