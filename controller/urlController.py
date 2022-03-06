from flask import render_template, flash
from werkzeug.utils import redirect
from model.link import Link
from model.db import db
import base64

# print(app.host)
class UrlController():
    
    def addUrl(self, urladd):
        domain2="https://me9.eu/"
        print(urladd)
        if ((db.session.query(Link).filter_by(url=urladd).first()) is not None):
            idurl = db.session.query(Link).filter_by(url=urladd).first().id
            base64_id = base64.b64encode(str(idurl).encode()).decode()
            data =domain2.strip() +base64_id.strip()
            return render_template("result.html", data=data)
        else:
            link = Link(url=urladd)
            db.session.add(link)   
            db.session.commit()
            id_url = link.id
            base64_id = base64.b64encode(str(id_url).encode()).decode()
            data =domain2.strip() +base64_id.strip()
            return render_template("result.html", data=data)

    def addNewUrl(self, urladd):
        domain2="https://me9.eu/"
        print(urladd)
        if ((db.session.query(Link).filter_by(url=urladd).first()) is not None):
            idurl = db.session.query(Link).filter_by(url=urladd).first().id
            base64_id = base64.b64encode(str(idurl).encode()).decode()
            data =domain2.strip() +base64_id.strip()
            return(data)
        else:
            link = Link(url=urladd)
            db.session.add(link)   
            db.session.commit()
            id_url = link.id
            base64_id = base64.b64encode(str(id_url).encode()).decode()
            data =domain2.strip() +base64_id.strip()
            return(data)
    
    def redirectUrl(self, id64):
        print(id64)
        id_bytes = id64.encode()
        try:
            id = base64.b64decode(id_bytes).decode()
        except:
            flash("This is not a valid URL")
            return redirect("/")
        if ((db.session.query(Link).filter(Link.id==id).first()) is not None):
            url = db.session.query(Link).filter(Link.id==id).first().url
            return redirect(url)
        else:
            flash("This is not a valid URL")
            return redirect("/")
    