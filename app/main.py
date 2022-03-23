from typing import Optional
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, Response
from fastapi.middleware.cors import CORSMiddleware
from to_ics import get_icals
from os import environ
from notion.client import NotionClient


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def convertN2ICS(password: Optional[str] = None, calendar_url: Optional[str] = None, categories_property: Optional[str] = "tag", categories_list: Optional[str] = "Other,", show_others: Optional[bool] = True):
    if password != environ["SECRET_PW"] or calendar_url == None:
        return HTMLResponse(r"For api description please consult the <a href='/docs'>docs</a>")
    elif password == environ["SECRET_PW"] or calendar_url != None:
        print(f"calurl: {calendar_url}")
        categories_list = categories_list.split(",")
        client = NotionClient(token_v2=environ["NOTION_TOKEN"], monitor=False)
        cals = get_icals(client, calendar_url, categories_property, categories_list, show_others)
        for cal in cals:
            ical = cals[cal].to_ical()
        return Response(content=ical,media_type="text/calendar")