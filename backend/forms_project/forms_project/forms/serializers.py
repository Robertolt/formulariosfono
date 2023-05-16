

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

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class QuestionnaireSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Questionnaire
        fields = '__all__'

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Question
        fields = '__all__'

class ResponseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Response
        fields = '__all__'

class QuestionOptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = QuestionOption
        fields = '__all__'

class SelectedOptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = SelectedOption
        fields = '__all__'

class WrittenAnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = WrittenAnswer
        fields = '__all__'
