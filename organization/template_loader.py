from jinja2 import Environment, BaseLoader, TemplateNotFound
from os.path import getmtime
from os import path


def get_new_custom_env(db_loader):
    env = Environment(loader=db_loader)
    return env


class TemplateSource(object):
    def __init__(self, env):
        self.env = env

    def render_template(self, email_template_source):
        template = self.env.get_template(email_template_source)
        return template.render()


class CustomLoader(object):

    def get_source(self, environment, email_template_source):
        if email_template_source:
            return email_template_source, '', lambda: getmtime(path)
        else:
            raise TemplateNotFound