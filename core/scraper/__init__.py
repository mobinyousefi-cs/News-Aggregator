#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: News Aggregator
File: core/scraper/__init__.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
Scraper registry utilities.

Usage:
`get_scraper("onion")` returns an instance of OnionScraper.

Notes:
- Add new scrapers here for discovery.

===============================================================================================================
"""
from .base import BaseScraper
from .onion import OnionScraper


SCRAPERS = {
    "onion": OnionScraper,
}


def get_scraper(name: str) -> BaseScraper:
    try:
        cls = SCRAPERS[name]
    except KeyError as exc:  # pragma: no cover - defensive
        raise ValueError(f"Unknown scraper: {name}") from exc
    return cls()