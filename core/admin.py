#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: News Aggregator
File: core/admin.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
Admin registrations for Source and Article models.

Usage:
Accessible at /admin/.

Notes:
- Includes list_display and search optimization.

===============================================================================================================
"""
from django.contrib import admin
from .models import Source, Article


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ("name", "homepage", "parser_name", "is_active", "created_at")
    search_fields = ("name", "homepage", "parser_name")
    list_filter = ("is_active",)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "source", "published_at", "created_at")
    search_fields = ("title", "url")
    list_filter = ("source", "published_at")
    readonly_fields = ("content_hash",)