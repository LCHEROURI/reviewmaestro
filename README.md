# ReviewMaestro

AI-Powered Restaurant Review Management SaaS Platform

## Overview

ReviewMaestro is a Flask and React prototype for helping restaurant owners monitor reviews, analyze sentiment, and draft professional responses. It is useful as a demo foundation, but it should be hardened before storing real customer or restaurant data.

## Live Demo

Production demo: [https://kkh7ikc7z7pz.manus.space](https://kkh7ikc7z7pz.manus.space)

## Key Features

- Centralized review management dashboard
- AI-powered sentiment analysis
- AI-assisted response drafting
- Review priority and urgency tracking
- Restaurant-level analytics
- Multi-restaurant data model

## Technology Stack

Backend:

- Flask
- Flask-SQLAlchemy
- OpenAI API
- SQLite for local development; configurable `DATABASE_URL` for production-style databases

Frontend:

- React build served from Flask static files
- Tailwind CSS
- Chart.js

## Project Structure

```text
reviewmaestro/
├── src/
│   ├── main.py
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── database/
│   └── static/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Quick Start

1. Clone the repository.

```bash
git clone https://github.com/LCHEROURI/reviewmaestro.git
cd reviewmaestro
```

2. Create and activate a virtual environment.

```bash
python -m venv venv
source venv/bin/activate
```

3. Install Python dependencies.

```bash
pip install -r requirements.txt
```

4. Create local environment variables.

```bash
cp .env.example .env
```

Then edit `.env` and add your own OpenAI key if you want AI features.

5. Start the app.

```bash
python src/main.py
```

Open [http://localhost:5000](http://localhost:5000).

## Important Production Notes

Before using ReviewMaestro with real restaurant/customer data, add:

- real authentication and tenant-level authorization
- protected admin/user routes
- locked-down CORS origins
- a strong `SECRET_KEY` set through the hosting platform
- a managed production database
- request validation and rate limiting
- audit logging for AI-generated responses and posted replies
- review-platform API integrations with proper permissions

The current app should be treated as a prototype/demo, not a production SaaS system.

## Environment Variables

See `.env.example` for the supported settings.

Required for AI features:

```bash
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_API_BASE=https://api.openai.com/v1
```

Required for production-style deployment:

```bash
SECRET_KEY=replace_with_a_long_random_secret
FLASK_ENV=production
FLASK_DEBUG=false
CORS_ORIGINS=https://your-domain.example
DATABASE_URL=your_database_url
```

## API Examples

```bash
GET /api/reviews?restaurant_id=1
POST /api/reviews/1/analyze
POST /api/reviews/1/generate-response
GET /api/restaurants/1/stats
```

## Roadmap

- Add authentication and organization/workspace access control
- Replace demo/sample data patterns with tenant-scoped data flows
- Add first-party review provider integrations
- Add production deployment configuration
- Add test coverage and CI checks
- Add audit history for generated responses

