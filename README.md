#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: News Aggregator
File: README.md
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
A production-grade Django web app that aggregates news articles from configured sources.
Includes a simple scraper for *The Onion* (as example), storage, and UI with TailwindCDN.

Usage:
See the Quickstart below.

Notes:
- Uses `requests` + `BeautifulSoup` for scraping; management command `fetch_news` orchestrates pulls.
- Easily extendable: add new scrapers under `core/scraper/` and register in `Source` records.
- CI with GitHub Actions; pytest for basic model tests.

===============================================================================================================
"""

# News Aggregator (Django)

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
cp env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py fetch_news --source onion --limit 30
python manage.py runserver
```
Open: http://127.0.0.1:8000/

## Environment
Create `.env` from `env.example`.

```
DEBUG=true
SECRET_KEY=change-me
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3
TIME_ZONE=America/Chicago
```

## Extend with New Sources
1. Implement a scraper class in `core/scraper/<name>.py` deriving from `BaseScraper`.
2. Register a `Source` row in the admin or via shell:
   ```python
   from core.models import Source
   Source.objects.get_or_create(name="MySite", homepage="https://mysite.com", parser_name="mysite")
   ```
3. Run `python manage.py fetch_news --source mysite`.

## Tests
```bash
pytest -q
```

## Docker (optional)
```bash
docker compose up --build
```

## License
MIT