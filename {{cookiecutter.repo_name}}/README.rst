{{cookiecutter.human_name}}
==============================================

This is a plugin for opsmatrix.

Development setup
-----------------

1. Make sure that you have a working opsmatrix development setup.

2. Clone this repository, eg to ``local/{{ cookiecutter.repo_name }}``.

3. Activate the virtual environment you use for opsmatrix development.

4. Execute ``python setup.py develop`` within this directory to register this application with opsmatrix's plugin registry.

5. Restart your local opsmatrix server. You can now use the plugin from this repository for your events by enabling it in
   the 'plugins' tab in the settings.


License
-------

{% if cookiecutter.license == "Apache" %}
Copyright {{cookiecutter.year}} {{cookiecutter.author_name}}

Released under the terms of the Apache License 2.0
{% elif cookiecutter.license == "NuoNuo Enterprise" %}
Copyright {{cookiecutter.year}}

Released under the terms of the proprietary NuoNuo Enterprise license.
{% endif %}
