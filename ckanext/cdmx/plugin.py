from json import tool
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class CdmxPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IDatasetForm)
    plugins.implements(plugins.IConfigurable)

    # IConfigurer

    def configure(self, config):
        config['licenses_group_url'] = 'https://licenses.opendefinition.org/licenses/groups/od.json'
        config['ckan.locale_default'] = 'es'

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')

    def is_fallback(self):
        return True

    def package_types(self):
        return []

    def _modify_package_schema(self, schema):
        schema['resources'].update({
            'resource_filters': [toolkit.get_validator('ignore_missing')],
            'resourse_stat_text': [toolkit.get_validator('ignore_missing')]
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
        schema['resources'].update({
            'resource_filters': [toolkit.get_validator('ignore_missing')],
            'resourse_stat_text': [toolkit.get_validator('ignore_missing')]
        })
        return schema
