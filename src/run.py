"""
run module for URL Shortening

Author : Amir Mofakhar <pangan@gmail.com>
"""
from app.keystone import app
from app import _settings

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=_settings.SERVER_PORT, debug=False)
