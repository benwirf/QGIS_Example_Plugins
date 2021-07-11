
def classFactory(iface):
    from .my_plugin import MyPlugin
    return MyPlugin(iface)