#
# Flask-SRI
#
# Copyright (C) 2017 Boris Raicheff
# All rights reserved
#


import json
import warnings


class SRI(object):
    """
    Flask-SRI

    Documentation:
    https://flask-sri.readthedocs.io

    For use with the Gulp-SRI plug-in:
    https://github.com/mathisonian/gulp-sri

    :param app: Flask app to initialize with. Defaults to `None`
    """

    manifest = None

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        try:
            with app.open_resource(app.config.get('SRI_MANIFEST'), mode='r') as fp:
                self.manifest = json.load(fp)
        except IOError:
            warnings.warn('SRI_MANIFEST not set', RuntimeWarning, stacklevel=2)
            self.manifest = {}
        app.jinja_env.globals.update(sri_hash=self.sri_hash)

    def sri_hash(self, resource):
        return self.manifest.get(resource, '')


# EOF
