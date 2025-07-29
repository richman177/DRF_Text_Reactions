from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Quote, Reaction
from .serializers import QuoteSerializer, ReactionSerializer
from django.shortcuts import get_object_or_404


class QuoteListCreateView(APIView):
    def get(self, request):
        quotes = Quote.objects.all()
        serializer = QuoteSerializer(quotes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuoteSerializer(data=request.data)
        if serializer.is_valid():
            quote = Quote.objects.create(
                text=serializer.validated_data['text'],
                author=serializer.validated_data['author']
            )
            return Response(QuoteSerializer(quote).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddReactionView(APIView):
    def post(self, request, pk):
        quote = get_object_or_404(Quote, pk=pk)
        serializer = ReactionSerializer(data=request.data)
        if serializer.is_valid():
            Reaction.objects.create(quote=quote, emoji=serializer.validated_data['emoji'])
            return Response({"message": "Reaction added!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
