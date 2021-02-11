import pytest
from terralib import common, core


@pytest.fixture(scope='module')
def terralib_initialize():
	common.TeSingleton.getInstance().initialize()
	core.LoadAll()
	yield
	common.TeSingleton.getInstance().finalize()
