import os, sys
app_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, app_path)

from leapbusiness import create_app
application = create_app()