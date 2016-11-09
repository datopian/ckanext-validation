import ckan.plugins as p


class ValidationController(p.toolkit.BaseController):
    controller = 'ckanext.validation.controller:ValidationController'

    def schemas_show(self):

        return p.toolkit.render('schemas_list.html')

    def schemas_edit(self, schema=None):

        return p.toolkit.render('schemas_edit.html')