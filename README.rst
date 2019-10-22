opsmatrix-plugin-cookiecutter
==========================

A simple `cookiecutter`_ template to bootstrap a opsmatrix plugin.

Usage
-----

Let's pretend you want to create a opsmatrix plugin called "superplugin".
First, create a virtual environment and install the ``cookiecutter``
package using pip. Next, use it to bootstrap your project folder::

    $ cd <your-project-folder-parent>
    $ cookiecutter https://github.com/Achillesxu/opsmatrix-plugin-cookiecutter


You'll be prompted for some questions. Answer them, and you will find a
project folder created for you::

    repo_name [opsmatrix-superplugin]: opsmatrix-superplugin
    repo_url [GitHub repository URL]: https://github.com/myuser/opsmatrix-superplugin
    module_name [opsmatrix_superplugin]: opsmatrix_superplugin
    human_name [The opsmatrix super plugin]: Super Plugin
    author_name [Your name]: J Random Developer
    author_email [Your email]: jrandom@example.org
    year [Current year]: 2019
    short_description [Short description]: The best plugin

Now, change to the newly created directory::

    $ cd opsmatrix-superplugin


.. _cookiecutter: https://github.com/audreyr/cookiecutter
