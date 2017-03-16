"""
run module for URL Shortening

Author : Amir Mofakhar <pangan@gmail.com>
"""
from app.models import db
from app.url_shortening import app
from app import _settings

if __name__ == "__main__":
    db.app = app
    db.init_app(app)
    db.create_all()
    app.run(host='0.0.0.0', port=_settings.SERVER_PORT, debug=False)
