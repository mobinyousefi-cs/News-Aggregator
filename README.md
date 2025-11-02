# 📰 Django News Aggregator

A powerful, elegant, and modular **news aggregation web app** built with **Python Django**. This project collects the latest articles from your favorite sites (starting with *The Onion* as an example) and presents them in a unified, minimalist dashboard.

## 🚀 Features
- **Real-Time News Fetching** — Scrapes live articles using BeautifulSoup.
- **Modular Architecture** — Add new scrapers by simply dropping files into `core/scraper/`.
- **Admin Dashboard** — Manage sources and inspect fetched articles.
- **Responsive UI** — Built with TailwindCSS for a clean, modern look.
- **Database-Driven Storage** — Saves all articles to the database (SQLite by default).
- **Optimized CI/CD** — Preconfigured GitHub Actions workflow.
- **Tests Included** — Basic model validation using pytest.

---

## ⚙️ Quickstart Guide

```bash
# 1️⃣ Create and activate a virtual environment
python -m venv .venv && source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Configure environment
cp env.example .env

# 4️⃣ Initialize the database
python manage.py migrate
python manage.py createsuperuser

# 5️⃣ Fetch news (example: The Onion)
python manage.py fetch_news --source onion --limit 30

# 6️⃣ Run the server
python manage.py runserver
```

Visit → [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧩 Adding a New News Source

1. Create a new scraper file inside `core/scraper/`:
   ```bash
   touch core/scraper/techcrunch.py
   ```
2. Inherit from `BaseScraper` and implement the `fetch()` method.
3. Register your scraper in `core/scraper/__init__.py` under `SCRAPERS`.
4. Add a `Source` record in the Django admin or shell:
   ```python
   from core.models import Source
   Source.objects.create(
       name="TechCrunch",
       homepage="https://techcrunch.com/",
       parser_name="techcrunch"
   )
   ```
5. Run:
   ```bash
   python manage.py fetch_news --source techcrunch
   ```

Your new articles will appear instantly on the homepage!

---

## 🧪 Testing

Run unit tests easily with:
```bash
pytest -q
```

---

## 🐳 Docker Support

For quick deployment:
```bash
docker compose up --build
```

This spins up a fully functional environment with all dependencies preconfigured.

---

## 🧠 Tech Stack
- **Backend:** Django 5.x
- **Frontend:** TailwindCSS (CDN)
- **Scraping:** BeautifulSoup4 + Requests
- **Database:** SQLite / PostgreSQL
- **CI/CD:** GitHub Actions + pytest
- **Environment:** python-dotenv + django-environ

---

## 📂 Project Structure
```
news_aggregator/
├── config/               # Django configuration
├── core/                 # Main application logic
│   ├── scraper/          # Modular web scrapers
│   ├── templates/        # HTML templates (Tailwind)
│   ├── static/           # Static assets
│   └── tests/            # Unit tests
├── manage.py             # Django entrypoint
├── requirements.txt      # Dependencies
├── Dockerfile            # Docker build file
├── docker-compose.yml    # Container orchestration
└── README.md             # Project documentation
```

---

## 🧾 License
This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author
**Mobin Yousefi** — [GitHub Profile](https://github.com/mobinyousefi-cs)

> "Information is power — automate its flow with intelligence." — *Mobin Yousefi*

