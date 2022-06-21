from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from comment import models
from comment.serializers import CommentSerializer, CommentListSerializer, NotificationsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect
from django.contrib.auth import logout


class CommentListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CommentListSerializer(data=request.data)
        if serializer.is_valid():
            all_data = models.Comment.objects.filter(course=serializer.validated_data['course'],
                                                     plan=serializer.validated_data['plan'])
            ser_data = CommentSerializer(all_data, many=True)
            return Response(ser_data.data)
        else:
            return Response(serializer.errors)


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


class NotificationsListAPIView(generics.ListAPIView):
    queryset = models.Notifications.objects.all()
    serializer_class = NotificationsSerializer
    permission_classes = [IsAuthenticated]


def logout_view(request):
    logout(request)
    return redirect('/')