from os import path
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


# TODO: update vocabulary
def create_date_formats():
    user = toolkit.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    try:
        data = {'id': 'date_formats'}
        toolkit.get_action('vocabulary_show')(context, data)
    except toolkit.ObjectNotFound:
        data = {'name': 'date_formats'}
        vocab = toolkit.get_action('vocabulary_create')(context, data)
        # By definition, the name for the new tag must be a string between 2 and 100 characters long containing only alphanumeric characters and -, _ and . See https://docs.ckan.org/en/2.9/api/index.html?highlight=tag_create#ckan.logic.action.create.tag_create
        # Update the readable value of each tag in readable_date_formats helper function
        for tag in (u'd_m_a', u'a_m_d', u'd_m_a HH.MM', u'a_m_d HH.MM'):
            data = {'name': tag, 'vocabulary_id': vocab['id']}
            toolkit.get_action('tag_create')(context, data)


def date_formats():
    create_date_formats()
    try:
        tag_list = toolkit.get_action('tag_list')
        date_formats = tag_list({}, {'vocabulary_id': 'date_formats'})
        return date_formats
    except toolkit.ObjectNotFound:
        return None


def readable_date_formats():
    return {'d_m_a': 'd/m/a', 'a_m_d': 'a/m/d', 'd_m_a HH.MM': 'd/m/a HH:MM', 'a_m_d HH.MM': 'a/m/d HH:MM'}


# TODO: update vocabulary
def create_update_frequencies():
    user = toolkit.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    try:
        data = {'id': 'update_frequencies'}
        toolkit.get_action('vocabulary_show')(context, data)
    except toolkit.ObjectNotFound:
        data = {'name': 'update_frequencies'}
        vocab = toolkit.get_action('vocabulary_create')(context, data)
        for tag in (u'Diario', u'Semanal', u'Quincenal', u'Mensual', u'Bimestral', u'Trimestral', u'Semestral', u'Anual', u'Histórico', u'No aplica'):
            data = {'name': tag, 'vocabulary_id': vocab['id']}
            toolkit.get_action('tag_create')(context, data)


def update_frequencies():
    create_update_frequencies()
    try:
        tag_list = toolkit.get_action('tag_list')
        update_frequencies = tag_list(
            {}, {'vocabulary_id': 'update_frequencies'})
        return update_frequencies
    except toolkit.ObjectNotFound:
        return None


# TODO: update vocabulary
def create_chart_types():
    user = toolkit.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    try:
        data = {'id': 'chart_types'}
        toolkit.get_action('vocabulary_show')(context, data)
    except toolkit.ObjectNotFound:
        data = {'name': 'chart_types'}
        vocab = toolkit.get_action('vocabulary_create')(context, data)
        for tag in (u'map', u'bar', u'line', u'treemap', u'scatter', u'table', u'map_bubble', u'map_heat'):
            data = {'name': tag, 'vocabulary_id': vocab['id']}
            toolkit.get_action('tag_create')(context, data)


def chart_types():
    create_chart_types()
    try:
        tag_list = toolkit.get_action('tag_list')
        chart_types = tag_list({}, {'vocabulary_id': 'chart_types'})
        return chart_types
    except toolkit.ObjectNotFound:
        return None


def readable_chart_types():
    return {
        'map': 'Mapa coroplético',
        'bar': 'Barras',
        'line': 'Líneas',
        'treemap': 'Treemap',
        'scatter': 'Dispersión',
        'table': 'Tabla',
        'map_bubble': 'Mapa de puntos',
        'map_heat': 'Mapa de calor'
    }


class CdmxPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IDatasetForm)
    plugins.implements(plugins.IConfigurable)
    plugins.implements(plugins.ITemplateHelpers)

    # ITemplateHelpers

    def get_helpers(self):
        return {
            'date_formats': date_formats,
            'readable_date_formats': readable_date_formats,
            'update_frequencies': update_frequencies,
            'chart_types': chart_types,
            'readable_chart_types': readable_chart_types
        }

    # IConfigurer

    def configure(self, config):
        """ Reference file """
        # config['licenses_group_url'] = 'file://' + path.dirname(__file__) + '/public/licenses.json'
        """ Reference url """
        # config['licenses_group_url'] = 'https://github.com/datosabiertoscdmx/licencias-portal/blob/main/licencias-portal-cdmx.json'
        config['ckan.locale_default'] = 'es'

    def update_config(self, config_):
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_resource('assets', 'cdmx_assets')

    def is_fallback(self):
        return True

    def package_types(self):
        return []

    def _modify_package_schema(self, schema):
        schema['resources'].update({
            'resource_filters': [toolkit.get_validator('ignore_missing')],
            'resource_subtitle': [toolkit.get_validator('ignore_missing')],
            'resource_default_var': [toolkit.get_validator('ignore_missing')],
            'resource_disaggregate': [toolkit.get_validator('ignore_missing')],
            'resource_viz': [toolkit.get_validator('ignore_missing')],
            'resource_priority_date': [toolkit.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'date_format': [
                toolkit.get_validator('ignore_missing'),
                toolkit.get_converter('convert_to_tags')('date_formats')
            ],
            'update_frequency': [
                toolkit.get_validator('ignore_missing'),
                toolkit.get_converter('convert_to_tags')('update_frequencies')
            ],
            'chart_type': [
                toolkit.get_validator('ignore_missing'),
                toolkit.get_converter('convert_to_tags')('chart_types')
            ]
        })
        return schema

    def create_package_schema(self):
        schema = super(CdmxPlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema = super(CdmxPlugin, self).update_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def show_package_schema(self):
        schema = super(CdmxPlugin, self).show_package_schema()
        schema['tags']['__extras'].append(
            toolkit.get_converter('free_tags_only'))
        schema['resources'].update({
            'resource_filters': [toolkit.get_validator('ignore_missing')],
            'resource_subtitle': [toolkit.get_validator('ignore_missing')],
            'resource_default_var': [toolkit.get_validator('ignore_missing')],
            'resource_disaggregate': [toolkit.get_validator('ignore_missing')],
            'resource_viz': [toolkit.get_validator('ignore_missing')],
            'resource_priority_date': [toolkit.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'date_format': [
                toolkit.get_converter('convert_from_tags')('date_formats'),
                toolkit.get_validator('ignore_missing')
            ],
            'update_frequency': [
                toolkit.get_converter('convert_from_tags')(
                    'update_frequencies'),
                toolkit.get_validator('ignore_missing')
            ],
            'chart_type': [
                toolkit.get_converter('convert_from_tags')(
                    'chart_types'),
                toolkit.get_validator('ignore_missing')
            ]
        })
        return schema
