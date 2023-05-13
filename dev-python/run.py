from __future__ import absolute_import
from importlib import reload
import sys
from config import app_config, app_active
from app import create_app

config = app_config[app_active]
config.APP = create_app()

if __name__ == '__main__':
    config.APP.run(host=config.IP_HOST, port=config.PORT_HOST)
    reload(sys)
