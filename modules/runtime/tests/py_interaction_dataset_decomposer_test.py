# Copyright (c) 2020 fortiss GmbH
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import unittest
from modules.runtime.commons.parameters import ParameterServer
from modules.runtime.scenario.dataset_decomposer.dataset_decomposer import DatasetDecomposer
import os

class DatasetDecomposerTest(unittest.TestCase):
    #@unittest.skip
    def test_decompose_dataset(self):

        map_filename = "../interaction_dataset_fortiss_internal/DR_DEU_Merging_MT/map/DR_DEU_Merging_MT_shifted.xodr"
        track_filename = "../interaction_dataset_fortiss_internal/DR_DEU_Merging_MT/tracks/vehicle_tracks_013.csv"

        dataset_decomposer = DatasetDecomposer(
            map_filename=map_filename, track_filename=track_filename)

        dataset_decomposer.decompose()



if __name__ == '__main__':
    unittest.main()

