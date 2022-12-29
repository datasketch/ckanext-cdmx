from datetime import datetime
from babel.dates import format_date
import ckan.plugins.toolkit as toolkit
from ckan.lib.formatters import localised_filesize


def date_formats():
    choices = [
        {"value": "", "text": "Seleccione una opción"},
        {"value": "d/m/a", "text": "d/m/a"},
        {"value": "a/m/d", "text": "a/m/d"},
        {"value": "d/m/a HH:MM", "text": "d/m/a HH:MM"},
        {"value": "a/m/d HH:MM", "text": "a/m/d HH:MM"},
    ]
    return choices


def update_frequencies():
    choices = [
        {"value": "", "text": "Seleccione una opción"},
        {"value": "Diario", "text": "Diario"},
        {"value": "Semanal", "text": "Semanal"},
        {"value": "Quincenal", "text": "Quincenal"},
        {"value": "Mensual", "text": "Mensual"},
        {"value": "Bimestral", "text": "Bimestral"},
        {"value": "Trimestral", "text": "Trimestral"},
        {"value": "Semestral", "text": "Semestral"},
        {"value": "Anual", "text": "Anual"},
        {"value": "Histórico", "text": "Histórico"},
        {"value": "No aplica", "text": "No aplica"},
    ]
    return choices


def chart_types():
    choices = [
        {"value": "", "text": "Seleccione una opción"},
        {"value": "map", "text": "Mapa coroplético"},
        {"value": "bar", "text": "Barras"},
        {"value": "line", "text": "Líneas"},
        {"value": "treemap", "text": "Treemap"},
        {"value": "scatter", "text": "Dispersión"},
        {"value": "table", "text": "Tabla"},
        {"value": "map_bubble", "text": "Mapa de puntos"},
        {"value": "map_heat", "text": "Mapa de calor"},
    ]
    return choices


def dashboard_types():
    choices = [
        {"value": "default", "text": "Visor por defecto"},
        {"value": "pdf", "text": "Visor PDF"},
        {"value": "shp", "text": "Visor Shapefile"},
        {"value": "table", "text": "Visor tabla"},
    ]
    return choices


def humanize_date(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return format_date(date_obj, "d 'de' MMMM yyyy", locale="es")


def get_package_categories(package):
    return ", ".join([item["title"] for item in package["groups"]])


def extract_from_key(list, key):
    return [item[key] for item in list]


def get_popular_datasets():
    data_dict = {"sort": "views_total desc", "rows": 3}
    datasets = toolkit.get_action("package_search")(context=None, data_dict=data_dict)
    return datasets


def get_format_color(format):
    default_color = "#B6C9C9"
    if not format:
        return default_color

    colors = {
        "csv": "#ccc41c",
        "xlsx": "#71b365",
        "shp": "#c9bf9c",
        "zip": "#696da9",
        "pdf": "#e0051e",
        "geojson": "#8b3d08",
        "json": "#ce5858",
        "doc": "#3e9fcc",
        "docx": "#3e9fcc",
    }

    format_ = format.lower()

    if format_.startswith("."):
        format_ = format_[1:]

    return colors.get(format_, default_color)


def get_site_url():
    site_url = toolkit.config.get("ckan.site_url", "")
    return site_url


def humanize_filesize(value):
    return localised_filesize(int(value))
