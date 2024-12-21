def create_app():
    app="hello-flask"

    from . import db
    db.init_app(app)

    return app