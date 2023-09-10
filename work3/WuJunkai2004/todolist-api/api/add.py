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
        detail = {
            "title": safe_get(data, 'title'),
            "content": safe_get(data, "content"),
            "deadline": safe_get(data, "deadline"),
            "is-complete": safe_get(data, "is-complete")
        }

        if(not detail['title'] or not detail['deadline']):
            self.send_code(200)
            self.send_text(json.dumps({
                "code":406,
                "msg":"title and deadline is required",
                "id":-1
            }))
            return

        db = SQL.SQL("todolist.db")
        try:
            db['todo'].create('title', 'content', 'is-complete', 'add-time', 'deadline')
        except:
            pass
        db['todo'].insert(detail['title'], detail['content'], detail['is-complete'], time.time(), detail['deadline'])

        self.send_code(200)
        self.send_text(json.dumps({
            "code":200,
            "msg":"success",
            "id":db['todo']['oid'][-1]
        }))