from pybuilder.core import use_plugin, init
from pybuilder.vcs import VCSRevision

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin('python.integrationtest')
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.pylint")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin('copy_resources')
use_plugin('filter_resources')

name = "antiwerbung"
summary = 'Verwalten von unerwünschten Werbeeinwürfen'
url = 'https://github.com/5nafu/antiwerbung'
version = '{0}'.format(VCSRevision().count)

default_task = ["analyze", "publish"]


@init
def set_properties(project):
    #project.build_depends_on("mock")
    #project.depends_on("docopt")
    project.set_property("verbose", False)
    project.set_property("integrationtest_always_verbose", True)
    project.set_property('dir_dist_scripts', 'scripts')
    project.set_property('flake8_include_test_sources', True)
    project.set_property('flake8_break_build', True)
    project.set_property("integrationtest_inherit_environment", True)
    project.set_property("integrationtest_parallel", True)
