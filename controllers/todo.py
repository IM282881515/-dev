#!/usr/bin/env python
# coding: utf-8
import web
from config import settings 

render = settings.render

class Index:
    def GET(self):
        return "Hello world!"