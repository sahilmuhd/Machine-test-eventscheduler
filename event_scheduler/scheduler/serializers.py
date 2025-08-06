from rest_framework import serializers
from .models import Event, Session, Speaker

class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = '__all__'

class SessionSerializer(serializers.ModelSerializer):
    speaker = SpeakerSerializer(read_only=True)
    speaker_id = serializers.PrimaryKeyRelatedField(
        queryset=Speaker.objects.all(), source='speaker', write_only=True
    )

    class Meta:
        model = Session
        fields = ['id', 'title', 'start_time', 'end_time', 'speaker', 'speaker_id']

class EventSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'location', 'sessions']
