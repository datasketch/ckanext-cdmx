from datetime import datetime
from babel.dates import format_date
import ckan.plugins.toolkit as toolkit


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


def humanize_date(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
    return format_date(date_obj, "d 'de' MMMM yyyy", locale="es")


def get_package_categories(package):
    return ", ".join([item['title'] for item in package['groups']])


def extract_from_key(list, key):
    return [item[key] for item in list]
