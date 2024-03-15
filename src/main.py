from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

static_route = '/static'
static_directory = './src/static'

app.mount(static_route, StaticFiles(directory = static_directory), name = "static")

templates_directory = './src/templates'
templates = Jinja2Templates(directory = templates_directory)


@app.get("/", response_class = HTMLResponse)
def root(request: Request):
  return templates.TemplateResponse(
    request = request, name = 'index.html', context = {}
  )
