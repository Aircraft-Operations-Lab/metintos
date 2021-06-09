import unittest
import xarray as xr
import metintos
import metintos.io
import numpy as np
import os


class TestDatasetHandler(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up data for the whole TestCase
        cwd = os.path.dirname(__file__)
        files_path = os.path.join(cwd, 'samples')
        file = os.path.join(files_path, 'forecast_xy_no_ensemble.nc')
        cls.ds = xr.open_mfdataset(file, engine='h5netcdf')

        # create DasetHandler object
        cls.dsh = metintos.io.DatasetHandler(cls.ds)

        # create CoordinateGenerator object and new step axi
        mn = np.timedelta64(1, 'm').astype('timedelta64[ns]')
        s0 = 0 * mn
        sf = 15 * 20.1 * mn  # this is 5 hours
        ss = mn * 5
        cls.cg = metintos.io.CoordinateGenerator()
        # cg.add_axis_lims_n_points('latitude', 30, 70, 32)
        # cg.add_axis_lims_n_points('longitude', -10, 40, 32)
        cls.cg.add_axis_lims_resolution('step', s0, sf, ss)

        # produce new dataset with optical flow
        cls.dsn = cls.dsh.get_optical_flow_interpolated_dataset(cls.cg.axes, ['tp'])

    def test_dataset(self):
        # check ds
        list_variables = list(self.ds.variables.keys())
        self.assertEqual(len(list_variables), 9, 'Variables ds from xr.open_mfdataset are not equal')
        list_coords = list(self.ds.coords.keys())
        self.assertEqual(len(list_coords), 7, 'Coordinates ds from xr.open_mfdataset are not equal')
        list_dims = list(self.ds.dims.keys())
        self.assertEqual(len(list_dims), 3, 'Dimensions ds from xr.open_mfdataset are not equal')

    def test_datasetHandler(self):
        # check ds_copied is like ds
        ds_copied = self.dsh.ds
        list_variables = list(ds_copied.variables.keys())
        self.assertEqual(len(list_variables), 9, 'Variables ds in dsh from xr.open_mfdataset are not equal')
        list_coords = list(ds_copied.coords.keys())
        self.assertEqual(len(list_coords), 7, 'Coordinates ds in dsh  from xr.open_mfdataset are not equal')
        list_dims = list(ds_copied.dims.keys())
        self.assertEqual(len(list_dims), 3, 'Dimensions ds in dsh  from xr.open_mfdataset are not equal')

        # check default_dims
        default_dims = self.dsh.default_dims
        self.assertEqual(len(default_dims), 3, 'default dims in dsh are not equal')

        # check time_dim
        time_dim = self.dsh.time_dim
        self.assertEqual(time_dim, 'step', 'time dims in dsh are not equal')

    def test_coordinates_change(self):
        list_steps = self.cg.axes['step']
        self.assertEqual(len(list_steps), 61, 'New Steps axes to compute the optical flow are not equal')

    def test_optical_flow(self):
        list_variables = list(self.dsn.variables.keys())
        self.assertEqual(len(list_variables), 7, 'Variables dsn from xr.open_mfdataset are not equal')
        list_coords = list(self.dsn.coords.keys())
        self.assertEqual(len(list_coords), 6, 'Coordinates dsn from xr.open_mfdataset are not equal')
        list_dims = list(self.dsn.dims.keys())
        self.assertEqual(len(list_dims), 3, 'Dimensions dsn from xr.open_mfdataset are not equal')

        steps_of = self.dsn['step'].values
        self.assertEqual(len(steps_of), 61, 'Number of Optical flow steps are not the expected ones')
        self.assertEqual(min(steps_of).astype(int), 0, 'Min of Optical flow step is not 0')
        self.assertEqual(max(steps_of).astype(int), 18000000000000, 'Max of Optical flow step is not equal')

        example_of = self.dsn.tp.values[1, 2, 5]
        self.assertEqual(round(float(example_of), 9), 0.131055206,
                         'value for the member=0, step=15min, latitude=XX, and longitude=XXX')


if __name__ == '__main__':
    unittest.main()
