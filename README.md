# QGIS_Example_Plugins
Examples of working Python plugin structures for QGIS 3

The PluginBuilder plugin for QGIS is a great tool which makes it really easy for new users to get started building their own plugins.
However, many new users also get confused about the plugin structure- especially which files and methods to modify to add their own logic and functionality. I have created this repository to show various examples of simple working plugins with different structures not created with PluginBuilder, to hopefully demystify some of the problem areas for those new to plugin development- especially the event handling (connecting UI buttons etc. to custom methods) which give the plugins functionality.

To try out a plugin, just copy the folder into your local plugins folder located (on Windows) here:

C:\Users\Username\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins

Then restart QGIS. You should see a new "Action" button in the Plugins Toolbar.

# Tips for new plugin developers

1. Consider writing a processing script instead- most tasks can be accomplished with a script which can be added to the processing toolbox. The advantages are: in most cases faster and simpler to develop than a plugin; can be used as part of a processing model in the graphical modeller.

2. Study and become familiar with the PyQt5 library. Create small programs in the QGIS Python console using PyQt. Experiment with using different widgets, layouts, signals, slots etc. Once you are comfortable with Qt, writing plugins will be a breeze!

3. Instead of using a generic QComboBox to allow the user to select layers and fields, use the custom QGIS widgets QgsMapLayerComboBox() and QgsFieldComboBox() instead.

TBC...
