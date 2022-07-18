import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.lib.jobs as jobs

from ckanext.cdmx.lib import date_formats, extract_from_key, update_frequencies, chart_types, humanize_date, get_package_categories


class CdmxPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IDatasetForm)
    plugins.implements(plugins.IConfigurable)
    plugins.implements(plugins.ITemplateHelpers)
    # plugins.implements(plugins.IResourceController)

    # ITemplateHelpers

    def get_helpers(self):
        return {
            'date_formats': date_formats,
            'update_frequencies': update_frequencies,
            'chart_types': chart_types,
            'humanize_date': humanize_date,
            'get_package_categories': get_package_categories,
            'extract_from_key': extract_from_key
        }

    # IConfigurable

    def configure(self, config):
        """ Reference file """
        # config['licenses_group_url'] = 'file://' + path.dirname(__file__) + '/public/licenses.json'
        """ Reference url """
        config['licenses_group_url'] = 'https://raw.githubusercontent.com/datosabiertoscdmx/licencias-portal/main/licencias-portal-cdmx.json'
        config['ckan.locale_default'] = 'es'

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_resource('assets', 'cdmx_assets')

    # IDatasetForm

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
            'resource_priority_date': [toolkit.get_validator('ignore_missing')],
            'update_frequency': [toolkit.get_validator('ignore_missing')],
            'chart_type': [toolkit.get_validator('ignore_missing')],
            'date_format': [toolkit.get_validator('ignore_missing')],
        })
        return schema

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
            'resource_priority_date': [toolkit.get_validator('ignore_missing')],
            'update_frequency': [toolkit.get_validator('ignore_missing')],
            'chart_type': [toolkit.get_validator('ignore_missing')],
            'date_format': [toolkit.get_validator('ignore_missing')]
        })
        return schema

    # IResourceController

    # def before_create(self, context, resource):
    #     return

    # def after_create(self, context, resource):
    #     if resource['format'] == 'SHP':
    #         jobs.enqueue(shp2geojson, [resource['id']])
    #     print(resource)
    #     print('........')
    #     return

    # def before_update(self, context, current, resource):
    #     return

    # def after_update(self, context, resource):
    #     return

    # def before_delete(self, context, resource, resources):
    #     return

    # def after_delete(self, context, resources):
    #     return

    # def before_show(self, resource_dict):
    #     return resource_dict
