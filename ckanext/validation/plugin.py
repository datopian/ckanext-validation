from logging import getLogger

import ckan.plugins as p
import ckan.plugins.toolkit as toolkit


log = getLogger(__name__)

class ValidationPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IResourceView, inherit=True)
    p.implements(p.IRoutes, inherit=True)

    # IConfigurer

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'validation')

    def before_map(self, m):
        controller = 'ckanext.validation.controller:ValidationController'

        m.connect('schemas_show', '/schemas}',
                    action='schemas_show', ckan_icon='file', controller=controller)

        m.connect('schemas_edit', '/schemas_edit{schema}',
                    action='schemas_edit', ckan_icon='edit', controller=controller)

        return m
