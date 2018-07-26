from flask import Flask, Blueprint
app = Flask(__name__)

from RoboCtrl.views import views
from RoboCtrl.driller_views import driller_views
from RoboCtrl.welder_views import welder_views

app.register_blueprint(views)
app.register_blueprint(driller_views)
app.register_blueprint(welder_views)
