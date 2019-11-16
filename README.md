# QGIS_Example_Plugins
Examples of working Python plugin structures for QGIS 3

The PluginBuilder plugin for QGIS is a great tool which makes it really easy for new users to get started building their own plugins.
However, many new users also get confused about the plugin structure- especially which files and methods to modify to add their own logic and functionality. I have created this repository to show various examples of simple working plugins with different structures not created with PluginBuilder, to hopefully demystify some of the problem areas for those new to plugin development- especially the event handling (connecting UI buttons etc. to custom methods) which give the plugins functionality.

To try out a plugin, just copy the folder into your local plugins folder located (on Windows) here:
C:\Users\Username\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins
Then restart QGIS.
