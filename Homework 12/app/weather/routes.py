from app.weather import views


def setup_routes(app):
   app.router.add_get("/", views.index)