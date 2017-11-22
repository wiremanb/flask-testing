#!/usr/bin/python
import sys, logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/WiremanITSolutions/")

from WiremanITSolutions import app as application
application.secret_key = 'Add your secrey key'
