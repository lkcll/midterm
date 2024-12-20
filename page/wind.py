import leafmap.foliumap as leafmap
import streamlit as st
import os
import subprocess

# Check and install netCDF4
try:
    import netCDF4 as nc
except ModuleNotFoundError:
    st.warning("netCDF4 is not installed. Attempting to install it...")
    subprocess.check_call([os.sys.executable, "-m", "pip", "install", "netCDF4"])
    import netCDF4 as nc  # Re-import after installation
st.header('Test')

filename = 'test-leafmap/wind_global.nc'
geojson = 'https://github.com/opengeos/leafmap/raw/master/examples/data/countries.geojson'
m = leafmap.Map(layers_control=True)
m.add_basemap('CartoDB.DarkMatter')
m.add_velocity(filename, zonal_speed='u_wind', meridional_speed='v_wind')
m.to_streamlit()
