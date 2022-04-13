#!/usr/bin/env python
from utils import app_handler as app

app.UtilityRoutes()

if __name__ == '__main__':
    app.APP.run(debug=True) #go to http://utilities-tracker.herokuapp.com/ to view the APP.