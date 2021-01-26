# serializers.py (accounts)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# py-lint: disable=R0903

"""
Serializer for users and profile information.

Available functions:
- Serialized for users
"""

from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serialized for users."""

    class Meta:
        """Meta data for the User Serializer."""

        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
