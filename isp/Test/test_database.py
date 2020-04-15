import os
import unittest

from obspy.core.event import Origin

from isp.Utils import ObspyUtil
from isp.db import db
from isp.earthquakeAnalisysis import PickerManager

dir_path = os.path.dirname(os.path.abspath(__file__))
db.set_db_url("sqlite:///{}/isp_test.db".format(dir_path))
db.start()

from isp.db.models import FirstPolarityModel, MomentTensorModel, EventArrayModel, PhaseInfoModel,\
    EventLocationModel, ArrayAnalysisModel


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # create all tables into db.
        db.create_all()

    @classmethod
    def tearDownClass(cls) -> None:
        # remove db file when test is done.
        db.remove_sqlite_db()

    def test_event_location(self):
        print("run test")
        print(EventLocationModel.get_all())
        print(FirstPolarityModel.get_all())
        print(MomentTensorModel.get_all())
        print(ArrayAnalysisModel.get_all())
        print(EventArrayModel.get_all())
        print(PhaseInfoModel.get_all())


    def test_event_location_insert(self):
        from isp.earthquakeAnalisysis import  NllManager
        nll_manager=NllManager(PickerManager.get_default_output_path(), None)
        origin = nll_manager.get_NLL_info()
        print(origin)

    def test_insert(self):
        hyp_file = os.path.join(dir_path, "test_data", "last.hyp")
        origin: Origin = ObspyUtil.reads_hyp_to_origin(hyp_file)
        event_model = EventLocationModel.create_from_origin(origin)
        event_model.save()
        event_model: EventLocationModel = EventLocationModel.find_by_id(event_model.id)
        print(event_model)
        # moment_dict = {"id": generate_id(16), "event_info_id": event_model.id, ....}
        # mt_model = MomentTensorModel.from_dict(moment_dict)
        # mt_model.save()


if __name__ == '__main__':
    unittest.main()

