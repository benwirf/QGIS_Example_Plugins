
def classFactory(iface):
    from .test_plugin import TestPlugin
    return TestPlugin(iface)