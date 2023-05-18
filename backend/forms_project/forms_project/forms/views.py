
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from forms_project.forms.models import (
    Questionnaire,
    Question,
    Response,
    QuestionOption,
    SelectedOption,
    WrittenAnswer,
)

from forms_project.forms.serializers import (
    UserSerializer, 
    GroupSerializer,
    QuestionnaireSerializer,
    QuestionSerializer,
    ResponseSerializer,
    QuestionOptionSerializer,
    SelectedOptionSerializer,
    WrittenAnswerSerializer,
)

"""
permissions.IsAuthenticated
permissions.IsAdminUser
"""

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]
    
class QuestionnaireViewSet(viewsets.ModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    permission_classes = [permissions.AllowAny]

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.AllowAny]

class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = [permissions.AllowAny]

class QuestionOptionViewSet(viewsets.ModelViewSet):
    queryset = QuestionOption.objects.all()
    serializer_class = QuestionOptionSerializer
    permission_classes = [permissions.AllowAny]

class SelectedOptionViewSet(viewsets.ModelViewSet):
    queryset = SelectedOption.objects.all()
    serializer_class = SelectedOptionSerializer
    permission_classes = [permissions.AllowAny]

class WrittenAnswerViewSet(viewsets.ModelViewSet):
    queryset = WrittenAnswer.objects.all()
    serializer_class = WrittenAnswerSerializer
    permission_classes = [permissions.AllowAny]

