# fastapi tag exploration

Playing with fastapi tags

## Run the app

`uv run uvicorn main:app --reload`

## What's going on?

This repo is exploring what is we go full python with fastapi, using the fastapi-tags danny created.  This means:

1. We have templates in python.  Instead of `index.html` or `about.html` jinja templates, we have `index.py` and `about.py` python templates.
2. `main.py` uses those templates to render pages
3. Instead of `styles.css` we have `styles.py` which defines dataclasses that we can set reusable styles with

## Is this a good idea?

🤷‍♂️ - i'm just goofing around having fun with an idea at this point.