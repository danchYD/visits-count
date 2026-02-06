from fastapi import FastAPI

app = FastAPI()
visits_count: int = 0
name_visits: dict[str, int] = {}


@app.get('/')
async def main_page():
    """
    Returning hello message and total visits for main page
    """
    global visits_count
    visits_count += 1

    return {
        'message': 'Hello! You are on a main page!',
        'visits_count': visits_count
    }


@app.get('/visits')
async def get_visits(reset: bool = False):
    """
    Returning visits count for main page

    :param reset: resets visits counter for main page
    :type reset: bool
    """
    global visits_count

    if reset:
        visits_count = 0

    return {
        'visits_count': visits_count
    }


@app.get('/greet/{name}')
async def greet_name(name: str):
    """
    Returning greetings message and greetings count for current user

    :param name: user name to greet
    :type name: str
    """
    global name_visits

    name_visits[name] = name_visits.get(name, 0) + 1

    return {
        'message': f'Hello, {name}!',
        'greetings_count': name_visits[name]
    }
