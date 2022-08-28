from setuptools import setup
from setuptools.command.build import build


# Override build command
class BuildCommand(build):
    def initialize_options(self):
        build.initialize_options(self)
        self.build_base = "/tmp"


setup(
    name="cb_{{cookiecutter.pkg_name}}",
    version="0.1",
    packages=["{{cookiecutter.pkg_name}}"],
    install_requires=[],
    cmdclass={"build": BuildCommand},
)