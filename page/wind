import leafmap.foliumap as leafmap
import streamlit as st

st.header('Test')

filename = 'test-leafmap/wind_global.nc'
geojson = 'https://github.com/opengeos/leafmap/raw/master/examples/data/countries.geojson'
m = leafmap.Map(layers_control=True)
m.add_basemap('CartoDB.DarkMatter')
m.add_velocity(filename, zonal_speed='u_wind', meridional_speed='v_wind')
m.to_streamlit()
