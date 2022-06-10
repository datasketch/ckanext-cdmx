import ckan.plugins.toolkit as toolkit


def create_date_formats():
    # TODO: update vocabulary
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


def create_update_frequencies():
    # TODO: update vocabulary
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
  return [
    {
      'value': 'Diario',
      'text': 'Diario'
    },
    {
      'value': 'Semanal',
      'text': 'Semanal'
    },
    {
      'value': 'Quincenal',
      'text': 'Quincenal'
    },
    {
      'value': 'Mensual',
      'text': 'Mensual'
    },
    {
      'value': 'Bimestral',
      'text': 'Bimestral'
    },
    {
      'value': 'Trimestral',
      'text': 'Trimestral'
    },
    {
      'value': 'Semestral',
      'text': 'Semestral'
    },
    {
      'value': 'Anual',
      'text': 'Anual'
    },
    {
      'value': 'Histórico',
      'text': 'Histórico'
    },
    {
      'value': 'No aplica',
      'text': 'No aplica'
    },
  ]


def create_chart_types():
    # TODO: update vocabulary
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
