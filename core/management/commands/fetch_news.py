#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: News Aggregator
File: core/management/commands/fetch_news.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
Management command to fetch and persist articles from a given source scraper.

Usage:
python manage.py fetch_news --source onion --limit 30

Notes:
- Idempotent via Article.content_hash and unique URL.

===============================================================================================================
"""
from __future__ import annotations
from django.core.management.base import BaseCommand
from django.utils import timezone
from core.models import Source, Article
from core.scraper import get_scraper


class Command(BaseCommand):
    help = "Fetches news from a configured source and stores new articles"

    def add_arguments(self, parser):
        parser.add_argument("--source", required=True, help="Source parser name, e.g., onion")
        parser.add_argument("--limit", type=int, default=30)

    def handle(self, *args, **opts):
        name = opts["source"].strip()
        limit = int(opts["limit"]) or 30
        scraper = get_scraper(name)

        source, _ = Source.objects.get_or_create(
            name=name.capitalize(),
            defaults={"homepage": "https://www.theonion.com/" if name == "onion" else "https://example.com/",
                      "parser_name": name, "is_active": True},
        )

        created = 0
        for item in scraper.fetch(limit=limit):
            art, was_created = Article.objects.get_or_create(
                url=item["url"],
                defaults={
                    "source": source,
                    "title": item.get("title", item["url"])[:500],
                    "image_url": item.get("image_url", ""),
                    "published_at": item.get("published_at", timezone.now()),
                },
            )
            if was_created:
                created += 1
        self.stdout.write(self.style.SUCCESS(f"Inserted {created} new articles from '{name}'."))