# Add new ui designers here. The *.ui files must be placed inside resources/designer_uis
from isp.Gui.Utils.pyqt_utils import load_ui_designers

# Add the new UiFrame to the imports at Frames.__init__
UiMainFrame = load_ui_designers("MainFrame.ui")
UiTimeFrequencyFrame = load_ui_designers("TimeFrequencyFrame.ui")
UiEarthquakeAnalysisFrame = load_ui_designers("EarthquakeAnalysisFrame.ui")
UiEarthquake3CFrame = load_ui_designers("Earthquake3CFrame.ui")
UiEarthquakeLocationFrame = load_ui_designers("EarthquakeLocationFrame.ui")
UiPaginationWidget = load_ui_designers("PaginationWidget.ui")
UiFilterGroupBox = load_ui_designers("FilterDockWidget.ui")
UiEventInfoGroupBox = load_ui_designers("EventInfoGroupBox.ui")



