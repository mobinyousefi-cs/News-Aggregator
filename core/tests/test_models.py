#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: News Aggregator
File: core/tests/test_models.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
Basic tests for Source and Article models.

Usage:
pytest -q

===============================================================================================================
"""
import pytest
from django.utils import timezone
from core.models import Source, Article


@pytest.mark.django_db
def test_article_hash_saved():
    s = Source.objects.create(name="Onion", homepage="https://www.theonion.com", parser_name="onion")
    a = Article.objects.create(
        source=s,
        title="Test Title",
        url="https://www.theonion.com/test-title",
        image_url="",
        published_at=timezone.now(),
    )
    assert a.content_hash
    assert len(a.content_hash) == 64