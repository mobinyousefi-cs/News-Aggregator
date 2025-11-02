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
