try:
    from opsmatrix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use opsmatrix 0.0.1 or above to run this plugin!")


class PluginApp(PluginConfig):
    name = '{{cookiecutter.module_name}}'
    verbose_name = '{{cookiecutter.human_name}}'

    class OpsMatrixPluginMeta:
        name = '{{cookiecutter.human_name}}'
        author = '{{cookiecutter.author_name}}'
        description = '{{cookiecutter.short_description}}'
        visible = True
        version = '1.0.0'
        compatibility = "opsmatrix>={{cookiecutter.min_basever}}"

    def ready(self):
        from . import signals  # NOQA


default_app_config = '{{cookiecutter.module_name}}.PluginApp'
