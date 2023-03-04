from rest_framework.response import Response
from rest_framework import viewsets
from django.db import IntegrityError
from .serializers import *


class ProfileAPIViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, args, kwargs)
        except IntegrityError as e:
            if 'UNIQUE constraint failed: api_profile.user_id' in e.args:
                return Response({'error': 'current user already has the profile'})
            else:
                return Response({'error': e.args})


class QuestionAPIViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerAPIViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class QuizAPIViewSet(viewsets.ModelViewSet):
    queryset = Quizz.objects.all()
    serializer_class = QuizzSerializer
