import logging
import ckan.plugins.toolkit as toolkit
import geopandas
import os


def log(msg, level=logging.INFO):
    logger = logging.getLogger(u'ckan')
    logger.log(level, msg)


def shp2geojson(resource_id):
    log('shp2geojson')
    log(os.environ.get('USERNAME'))
    user = toolkit.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    resource = toolkit.get_action('resource_show')(
        context, {'id': resource_id})
    res_name = resource['name']
    package_id = resource['package_id']
    outfile = '/var/tmp/{}'.format(res_name)
    log('Write access to /var/tmp')
    log(os.access('/var/tmp', os.W_OK))
    gdf = geopandas.read_file(resource['url'])
    log(gdf)
    gdf.to_file(outfile, driver='GeoJSON')
    toolkit.get_action('resource_create')(context, {
        'package_id': package_id,
        'name': res_name,
        'format': 'CSV',
        'url': 'https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv',
    })
    log('.........')
