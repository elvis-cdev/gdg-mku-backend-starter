# gdg mku backend starter

Starter repo for the GDG MKU backend journey. It's a tiny events API built with FastAPI. Nothing fancy. The point is that you can run it, read it, break it and fix it.

## Run it (3 steps)

Easiest way is Codespaces, no installs needed.

1. Click the green **Code** button, go to **Codespaces**, then **Create codespace**
2. Wait for it to finish setting up
3. In the terminal run `uvicorn main:app --reload`

A popup will show up for port 8000. Open it and add `/docs` at the end of the link. That page lets you click "Try it out" and send real requests to the API.

## Run it on your own laptop

You need Python 3.10 or newer.

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

On Windows use `venv\Scripts\activate` instead of the source line.

## What's in here

- `main.py` is the whole app for now
- `requirements.txt` has the packages
- `.devcontainer/` is what makes Codespaces just work

## Things to try at the kickoff

- Hit `GET /events` and see what comes back
- Add an event with `POST /events`
- Ask for an event that doesn't exist. What status code do you get? Is that the right one?
- Change one small thing and try to predict what will break before you run it

## Heads up

Events are stored in a plain list, so they disappear every time the server restarts. We move to a real database in session 2.

## Who

Elvis, backend lead at GDG MKU. Got a question? Ask in the group.
