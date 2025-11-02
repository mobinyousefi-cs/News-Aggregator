#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: News Aggregator
File: core/models.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
Data models for sources and articles.

Usage:
`python manage.py makemigrations && python manage.py migrate`

Notes:
- content_hash used to prevent duplicates.

===============================================================================================================
"""
from __future__ import annotations
from django.db import models
from django.utils import timezone
import hashlib


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Source(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    homepage = models.URLField()
    parser_name = models.CharField(max_length=50, help_text="Scraper module name in core.scraper.*")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.name


class Article(TimeStampedModel):
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name="articles")
    title = models.CharField(max_length=500)
    url = models.URLField(unique=True)
    image_url = models.URLField(blank=True)
    published_at = models.DateTimeField(default=timezone.now)
    content_hash = models.CharField(max_length=64, unique=True, editable=False)

    class Meta:
        ordering = ["-published_at", "-created_at"]
        indexes = [
            models.Index(fields=["published_at"]),
            models.Index(fields=["source", "published_at"]),
        ]

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if not self.content_hash:
            base = f"{self.title}|{self.url}|{self.source_id}"
            self.content_hash = hashlib.sha256(base.encode("utf-8")).hexdigest()
        super().save(*args, **kwargs)