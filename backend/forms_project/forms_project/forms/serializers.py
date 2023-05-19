

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
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class QuestionnaireSerializer(serializers.ModelSerializer):
    question_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta: 
        model = Questionnaire
        fields = [
            'id', 
            'title', 
            'description', 
            'created_at', 
            'question_set'
        ]

class QuestionSerializer(serializers.ModelSerializer):
    question_option_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta: 
        model = Question
        fields = [
            'id',
            'questionnaire',
            'text',
            'created_at',
            'question_type',
            'question_option_set'
        ]

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
