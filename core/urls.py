#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: News Aggregator
File: core/urls.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
URL routes for core views.

Usage:
Included from config.urls.

Notes:
- Namespaced as 'core'.

===============================================================================================================
"""
from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("sources/", views.sources, name="sources"),
    path("article/<int:pk>/", views.article_detail, name="article_detail"),
]