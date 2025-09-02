# natureShare
An app for sharing organisms you find in nature — what they are, where you found them, and useful context like ecosystem and weather.

## Why
This started as a way for us to keep track of edible mushrooms and other foraged foods around the PNW. It grew into a simple social logbook: upload a photo, capture some details, and find things later.

## Features
- Upload photos with metadata: name, edibility, ecosystem, weather, date, and location (with a map picker)
- Browse all organisms; edit/delete only your own
- Search by ecosystem type
- User accounts: register, login, logout
- Share a detail view to Twitter (title + link)

## Screenshots
- Desktop: ![natureShare Desktop View](wireframe/natureShare.PNG)
- Mobile: ![natureShare Mobile View](wireframe/natureShareMobile.PNG)

## Tech Stack
- Backend: Django 3.1, SQLite (dev)
- Frontend: Django templates, vanilla JS, jQuery
- Maps: `django-location-field` with Google Maps
- Static files: WhiteNoise
- Deploy: Heroku (Procfile + runtime.txt)

## Requirements
- Python 3.8+
- A Google Maps API key (optional for basic usage; required for location picker)

## Quick Start
1) Create a virtualenv and install deps
```
pip install -r natureShare/requirements.txt
```

2) Configure environment
```
cp natureShare/.env.example natureShare/.env
```
Set the following in `natureShare/.env`:
- `DJANGO_SECRET_KEY` — generate one:
  ```
  python -c "from django.core.management.utils import get_random_secret_key as g; print(g())"
  ```
- `DJANGO_DEBUG` — `True` for local dev
- `DJANGO_ALLOWED_HOSTS` — `127.0.0.1,localhost` for local dev
- `GOOGLE_API_KEY` — if you want the map picker

3) Initialize the database
```
python natureShare/manage.py migrate
python natureShare/manage.py createsuperuser
```

4) Run the app
```
python natureShare/manage.py runserver
```

Open http://127.0.0.1:8000 and register or login.

## Using the App
- Home: upload an organism photo and details; the location widget lets you drop a pin
- Images: view all uploaded organisms (everyone’s)
- Detail: see one organism, with map and actions to share
- My Organisms: quick list of only your uploads, with edit/delete
- Search: filter by ecosystem type

## Configuration Notes
- `ALLOWED_HOSTS` is configurable via `DJANGO_ALLOWED_HOSTS` (comma‑separated)
- Static files are served by WhiteNoise in production (`CompressedManifestStaticFilesStorage`)
- Media uploads (user images) are stored at `natureShare/media/` in development and are not tracked by Git
- The map widget scripts are injected by `{{ form.media }}` on the home page. Keep jQuery and the Google Maps API loading before those injected scripts. If the map breaks, check script order and your `GOOGLE_API_KEY` first.

## Development
- Migrations
  ```
  python natureShare/manage.py makemigrations
  python natureShare/manage.py migrate
  ```
- Running tests (placeholder tests included)
  ```
  python natureShare/manage.py test
  ```
- Admin
  ```
  python natureShare/manage.py createsuperuser
  ```

## Deployment (Heroku)
This repo includes `Procfile`, `runtime.txt`, `requirements.txt`, and uses WhiteNoise.

Configure config vars:
- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG=False`
- `DJANGO_ALLOWED_HOSTS=your-domain.com`
- `GOOGLE_API_KEY` (optional, enables map widget)

Then:
```
python natureShare/manage.py collectstatic --noinput
```
Heroku’s deploy pipeline will run collectstatic automatically if configured; WhiteNoise will serve static files.

## Troubleshooting
- Map not loading
  - Ensure `GOOGLE_API_KEY` is set and valid
  - Confirm jQuery and Google Maps load before `{{ form.media }}` on the home page
- Images not appearing in dev
  - Ensure `DEBUG=True` so media is served by Django
  - Files are saved under `natureShare/media/`
- CSRF errors on form submit
  - Make sure templates include `{% csrf_token %}` and you’re using the correct domain under `ALLOWED_HOSTS`

## Reference Links
- Uploading images in Django: https://www.geeksforgeeks.org/python-uploading-images-in-django/
- Search with Django: https://learndjango.com/tutorials/django-search-tutorial
- Google Maps JS API: https://developers.google.com/maps/documentation/javascript/adding-a-google-map

## Acknowledgements
Thanks to the open‑source community and the resources linked above that helped shape this project.

