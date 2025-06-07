from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
import fastapi_tags as ft
from templates import index, about

app = FastAPI()

tasks = []

@app.get("/", response_class=ft.FTResponse)
async def home(request: Request):
    """Render the task manager page using the index template."""
    return index.render(tasks)

@app.post("/add-task", response_class=ft.FTResponse)
async def add_task(task: str = Form(...)):
    tasks.append(task)
    return index.create_task_li(task, len(tasks)-1)

@app.delete("/delete-task/{task_id}")
async def delete_task(task_id: int):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)

@app.get("/about", response_class=ft.FTResponse)
async def about_page():
    """Render the about page."""
    return about.render()
