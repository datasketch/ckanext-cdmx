import logging
import os
import ckanapi
import requests
from uuid import uuid4
from shutil import copyfileobj
from geopandas import read_file


def date_formats():
    choices = [
        {'value': '', 'text': 'Seleccione una opción'},
        {'value': 'd/m/a', 'text': 'd/m/a'},
        {'value': 'a/m/d', 'text': 'a/m/d'},
        {'value': 'd/m/a HH:MM', 'text': 'd/m/a HH:MM'},
        {'value': 'a/m/d HH:MM', 'text': 'a/m/d HH:MM'},
    ]
    return choices


def update_frequencies():
    choices = [
        {'value': '', 'text': 'Seleccione una opción'},
        {'value': 'Diario', 'text': 'Diario'},
        {'value': 'Semanal', 'text': 'Semanal'},
        {'value': 'Quincenal', 'text': 'Quincenal'},
        {'value': 'Mensual', 'text': 'Mensual'},
        {'value': 'Bimestral', 'text': 'Bimestral'},
        {'value': 'Trimestral', 'text': 'Trimestral'},
        {'value': 'Semestral', 'text': 'Semestral'},
        {'value': 'Anual', 'text': 'Anual'},
        {'value': 'Histórico', 'text': 'Histórico'},
        {'value': 'No aplica', 'text': 'No aplica'},
    ]
    return choices


def chart_types():
    choices = [
        {'value': '', 'text': 'Seleccione una opción'},
        {'value': 'map', 'text': 'Mapa coroplético'},
        {'value': 'bar', 'text': 'Barras'},
        {'value': 'line', 'text': 'Líneas'},
        {'value': 'treemap', 'text': 'Treemap'},
        {'value': 'scatter', 'text': 'Dispersión'},
        {'value': 'table', 'text': 'Tabla'},
        {'value': 'map_bubble', 'text': 'Mapa de puntos'},
        {'value': 'map_heat', 'text': 'Mapa de calor'},
    ]
    return choices

def log(msg, level=logging.INFO, logger=u'ckan'):
    logger = logging.getLogger(logger)
    logger.log(level, msg)


def shp2json(resource_id, site_url, apikey):
    ckan = ckanapi.RemoteCKAN(site_url, apikey=apikey)
    resource = ckan.action.resource_show(id=resource_id)
    resource_url = resource['url']
    response = requests.get(resource_url)

    if response.status_code != 200:
        raise Exception("{0} could not be downloaded".format(resource_url))

    tmp_file_name = "{}.{}".format(uuid4(), 'shp.zip')

    with open(os.path.join('/tmp', tmp_file_name), 'wb') as out_file:
        copyfileobj(response.raw, out_file)

    log(tmp_file_name)
    log('*** --- ***')


