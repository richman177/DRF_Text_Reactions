from rest_framework import serializers
from .models import Quote, Reaction
from collections import Counter


class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ['emoji']


class QuoteSerializer(serializers.ModelSerializer):
    reactions = serializers.SerializerMethodField()

    class Meta:
        model = Quote
        fields = ['id', 'text', 'author', 'reactions']

    def get_reactions(self, obj):
        emojis = obj.reactions.values_list('emoji', flat=True)
        return dict(Counter(emojis))
