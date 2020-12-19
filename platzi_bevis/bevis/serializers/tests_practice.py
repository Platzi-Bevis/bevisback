"""Test serializers"""
from rest_framework import serializers

from bevis.models.practice_tests import Practice_tests


class TestPracticeModelSerializer(serializers.ModelSerializer):
    """Tests model serializer"""

    class Meta:
        """Meta Class"""

        model = Practice_tests
        fields = (
            "title",
            "case_tests",
            "description",
            "boilerplate",
        )
