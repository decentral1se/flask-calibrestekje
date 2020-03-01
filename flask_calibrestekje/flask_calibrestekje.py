from calibrestekje import init_session
from flask import _app_ctx_stack, current_app


class CalibreStekje(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault("CALIBRESTEKJE_SQLITE_URL", ":memory:")
        app.teardown_appcontext(self.teardown)

    def connect(self):
        return init_session(current_app.config["CALIBRESTEKJE_SQLITE_URL"])

    def teardown(self, exception):
        ctx = _app_ctx_stack.top
        if hasattr(ctx, "calibrestekje_session"):
            ctx.calibrestekje_session.close()

    @property
    def session(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, "calibrestekje_session"):
                ctx.calibrestekje_session = self.connect()
            return ctx.calibrestekje_session
