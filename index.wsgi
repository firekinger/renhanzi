#!/usr/bin/env python
# coding: utf-8
import sae
import web
import urls

app = web.application(urls.renhanzi, globals())

application = sae.create_wsgi_app(app)

