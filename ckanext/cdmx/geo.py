import ckan.plugins.toolkit as toolkit
import geopandas
import os

TEMPDIR = os.path.join(os.path.dirname(__file__), '..', 'tmp')
OUTDIR = os.path.join(TEMPDIR, 'out')

def shp2geojson(resource_id):
    if not os.path.isdir(OUTDIR):
        os.makedirs(OUTDIR)
    
    user = toolkit.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    resource = toolkit.get_action('resource_show')(context, { 'id': resource_id })
    res_name = resource['name']
    outfile = os.path.join(OUTDIR, res_name)
    gdf = geopandas.read_file(resource['url'])
    gdf.to_file(outfile, driver='GeoJSON')
    toolkit.get_action('resource_create')(context, {
      'package_id': resource['package_id'],
      'format': 'GeoJSON',
      'name': res_name,
      'url': 'any',
      'upload': open(outfile)
    })
    