from isp.Gui import pw, pyc
from isp.Gui.Frames.uis_frames import UiHelp
#from isp import HELP_PATH

class HelpDoc(pw.QFrame, UiHelp):

    def __init__(self):
        super(HelpDoc, self).__init__()
        self.setupUi(self)
        url = "https://rcabdia.github.io/ISP_tutorial.github.io/"
        #path = os.path.join(HELP_PATH,"Responsive HTML5","index.htm")
        url = pyc.QUrl(url)
        #url = pyc.QUrl.fromLocalFile(path)
        self.widget.load(url)

