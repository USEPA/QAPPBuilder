# apps.py (qapp_builder)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov

"""
Application configuration objects store metadata for an application.

Some attributes can be configured in AppConfig subclasses. Others are
set by Django and read-only. This file is created to include any application
configuration for the app. Using this, you can configure some of the attributes
of the application.

Available functions:
It is the recommended best practice to place your application configuration
in the apps.py. This feature has been in Django since version 1.7, but to
promote its use and enable easier configuration, the apps.py file has been
added to the default app template.
"""

# Note: DOCUMENTING MODULES. (Top-level file info and docstring): all .py
# files to include the header above (modified for each docstring as
# appropriate) example: lines# 1 thru 18. Reference: Slatkin, Brett,
# "Effective Python, 59 Specific Ways to Write Better Python," Addison-
# Wesley: New York, 2015. ISBN-13: 978-0-13-403428-7. p. 17.

from django.apps import AppConfig


class QappBuilderConfig(AppConfig):
    """qapp_builder configuration."""

    name = 'qapp_builder'
    verbose_name = 'qapp_builder'
    default_app_config = 'qapp_builder.apps.QappBuilderConfig'
