# from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from google.cloud import datastore
from pydantic import BaseModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory = './templates')


@app.get("/", response_class = HTMLResponse)
def root(request: Request):
  return templates.TemplateResponse(
    request = request, name = 'index.html', context = {}
  )

database_name = 'registro'
datastore_client = datastore.Client(database = database_name)


class FormData(BaseModel):
  timestamp: str
  string_qr: str


@app.post('/api/send-data')
def send_data(item: FormData):
  create_and_store_entity(item)

  return item


def create_and_store_entity(form_data: FormData):
  kind = FormData.__name__
  form_key = datastore_client.key(kind)

  form_entity = datastore.Entity(key = form_key)
  form_entity.update({
    'timestamp': form_data.timestamp,
    'string_qr': form_data.string_qr,
  })

  datastore_client.put(form_entity)

  return form_data
