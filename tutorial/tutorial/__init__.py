"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

app.config.from_pyfile('config_default.py')

import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
#logger.info(app.config)
import tutorial.views
