"""flask-calibrestekje module."""

from flask_calibrestekje.flask_calibrestekje import CalibreStekje  # noqa

try:
    import pkg_resources
except ImportError:
    pass


try:
    __version__ = pkg_resources.get_distribution("flask-calibrestekje").version
except Exception:
    __version__ = "unknown"
