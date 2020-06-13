
import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st

POWER_PLANT_URL = (
    "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-streamlit/master/"
    "gallery/global_power_plant_database/global_power_plant_database.csv"
)

LOCATIONS = {
    "Orsted Copenhagen HQ": {"latitude": 55.676098, "longitude": 12.568337},
    "Orsted Boston": {"latitude": 2.361145, "longitude": -71.057083},
}
ORSTED_CPH_HQ = LOCATIONS["Orsted Copenhagen HQ"]


class ViewStateComponent:
    def __init__(self):
        self.latitude = ORSTED_CPH_HQ["latitude"]
        self.longitude = ORSTED_CPH_HQ["longitude"]
        self.zoom = 3
        self.pitch = 40.0

    def edit_view(self):
        location = st.sidebar.selectbox("Location", options=list(LOCATIONS.keys()), index=0)
        self.latitude = LOCATIONS[location]["latitude"]
        self.longitude = LOCATIONS[location]["longitude"]

        self.zoom = st.sidebar.slider("Zoom", min_value=0, max_value=11, value=self.zoom)
        self.pitch = st.sidebar.slider(
            "Pitch", min_value=0.0, max_value=100.0, value=self.pitch, step=10.0
        )

    @property
    def view_state(self) -> pdk.ViewState:
        return pdk.ViewState(
            longitude=self.longitude,
            latitude=self.latitude,
            zoom=self.zoom,
            min_zoom=1,
            max_zoom=15,
            pitch=self.pitch,
            # bearing=-27.36,
        )


class GlobalPowerPlantDatabaseApp:
    def __init__(self):
        self.view_state_component = ViewStateComponent()
        self.data = self.get_data()

    @staticmethod
    @st.cache
    def get_data():
        data = pd.read_csv(POWER_PLANT_URL)

        return data[["latitude", "longitude"]].dropna()

    def _scatter_plotter_layer(self):
        return pdk.Layer(
            "ScatterplotLayer",
            data=self.data,
            get_position=["longitude", "latitude"],
            extruded=True,
            get_radius=5000,
            pickable=True,
            opacity=0.8,
            stroked=False,
            filled=True,
            wireframe=True,
        )

    def view(self):
        self.view_state_component.edit_view()  # Does not work

        st.pydeck_chart(
            pdk.Deck(
                map_style="mapbox://styles/mapbox/light-v9",
                initial_view_state=self.view_state_component.view_state,
                layers=[self._scatter_plotter_layer()],
            )
        )


app = GlobalPowerPlantDatabaseApp()
app.view()
