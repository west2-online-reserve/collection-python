import vercel
import json
import SQL
import time


def safe_get(dict, name):
    try:
        return dict[name]
    except:
        return ''


class handler(vercel.API):
    def vercel(self, url, data, headers):
        vercel.ErrorStatu(self, 503)