#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: News Aggregator
File: core/scraper/onion.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
Scraper for The Onion homepage listing to demonstrate aggregation.

Usage:
Used via management command `fetch_news --source onion`.

Notes:
- HTML structure may change; logic is defensive and looks for common patterns.

===============================================================================================================
"""
from __future__ import annotations
from typing import List, Dict
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from .base import BaseScraper


class OnionScraper(BaseScraper):
    base_url = "https://www.theonion.com/"

    def fetch(self, limit: int = 30) -> List[Dict]:
        resp = requests.get(self.base_url, headers=self.headers, timeout=self.timeout)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        items: List[Dict] = []
        # Try to find article cards
        for art in soup.find_all("article"):
            a = art.find("a", href=True)
            if not a:
                continue
            title = (a.get("aria-label") or a.get_text(" ")).strip()
            url = self._safe_abs(a["href"], self.base_url)

            # image
            img = art.find("img")
            image_url = ""
            if img and img.get("src"):
                image_url = self._safe_abs(img["src"], self.base_url)

            # published time if present
            pub = None
            time_tag = art.find("time")
            if time_tag:
                dt = time_tag.get("datetime") or time_tag.get_text().strip()
                pub = self._parse_datetime(dt)

            items.append({
                "title": title or url,
                "url": url,
                "image_url": image_url,
                "published_at": pub or datetime.utcnow(),
            })
            if len(items) >= limit:
                break
        return items