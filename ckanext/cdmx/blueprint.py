from flask import Blueprint

from ckan.plugins.toolkit import render
import ckan.lib.helpers as h


validate = Blueprint(u'visualizador', __name__)


@validate.route(u'/visualizador')
def index():
    extra_vars = {
    }

    return render(u'visualizador.html', extra_vars)
