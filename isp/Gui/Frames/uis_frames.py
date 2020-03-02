# Add new ui designers here. The *.ui files must be placed inside resources/designer_uis
from isp.Gui.Utils.pyqt_utils import load_ui_designers

# Add the new UiFrame to the imports at Frames.__init__
UiMainFrame = load_ui_designers("MainFrame.ui")
UiTimeFrequencyFrame = load_ui_designers("TimeFrequencyFrame.ui")
UiTimeAnalysisWidget = load_ui_designers("TimeAnalysisWidget.ui")
UiEarthquakeAnalysisFrame = load_ui_designers("EarthquakeAnalysisFrame.ui")
UiEarthquake3CFrame = load_ui_designers("Earthquake3CFrame.ui")
UiEarthquakeLocationFrame = load_ui_designers("EarthquakeLocationFrame.ui")
UiPaginationWidget = load_ui_designers("PaginationWidget.ui")
UiFilterDockWidget = load_ui_designers("FilterDockWidget.ui")
UiTimeSelectorDockWidget = load_ui_designers("TimeSelectorDockWidget.ui")
UiSpectrumDockWidget = load_ui_designers("SpectrumDockWidget.ui")
UiEventInfoDockWidget = load_ui_designers("EventInfoDockWidget.ui")
UiStationInfoDockWidget = load_ui_designers("StationInfoDockWidget.ui")
UiArrayAnalysisFrame = load_ui_designers("ArrayAnalysisFrame.ui")
UitestFrame = load_ui_designers("test.ui")
UiParametersFrame = load_ui_designers("parameters.ui")
UiAdditionalParameters = load_ui_designers("additionalParameters.ui")
UiMomentTensor = load_ui_designers("MomentTensor.ui")



