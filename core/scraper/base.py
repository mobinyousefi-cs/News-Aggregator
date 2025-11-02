#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: News Aggregator
File: core/scraper/base.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
Abstract base scraper definition.

Usage:
Subclass and implement `fetch` to return list of {title, url, image_url, published_at} dicts.

Notes:
- Network timeouts tuned for reliability.

===============================================================================================================
"""
from __future__ import annotations
from typing import List, Dict
from datetime import datetime
import requests
from bs4 import BeautifulSoup


class BaseScraper:
    timeout = 10
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome Safari",
        "Accept-Language": "en-US,en;q=0.9",
    }

    def fetch(self, limit: int = 30) -> List[Dict]:  # pragma: no cover - abstract
        raise NotImplementedError

    @staticmethod
    def _parse_datetime(text: str) -> datetime | None:
        # Best-effort parser; sites vary. Keep simple to avoid heavyweight deps.
        try:
            return datetime.fromisoformat(text.replace("Z", "+00:00"))
        except Exception:
            return None

    @staticmethod
    def _safe_abs(url: str, base: str) -> str:
        if url.startswith("http://") or url.startswith("https://"):
            return url
        return base.rstrip("/") + "/" + url.lstrip("/")