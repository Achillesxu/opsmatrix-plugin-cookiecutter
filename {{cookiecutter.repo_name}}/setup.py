import os
from distutils.command.build import build

from django.core import management
from setuptools import setup, find_packages


try:
    with open(os.path.join(os.path.dirname(__file__), 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = ''


class CustomBuild(build):
    def run(self):
        """
        add some special django command if you need before build.run() function
        :return:
        """
        build.run(self)


cmdclass = {
    'build': CustomBuild
}


setup(
    name='{{cookiecutter.repo_name}}',
    version='1.0.0',
    description='{{cookiecutter.short_description}}',
    long_description=long_description,
    url='{{cookiecutter.repo_url}}',
    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.author_email}}',
    license='Apache Software License',

    install_requires=[],
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    cmdclass=cmdclass,
    entry_points="""
[opsmatrix.plugin]
{{cookiecutter.module_name}}={{cookiecutter.module_name}}:OpsMatrixPluginMeta
""",
)
