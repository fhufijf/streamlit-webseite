import streamlit as st
import streamlit_folium
import folium
import requests
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Wetter",
    page_icon="🌤️",
    layout="wide",
)

st.title("Wetter-App")
st.subheader("Interaktive Wetterkarte mit OpenWeatherMap und NOAA Layern")

st.divider()

# CSV-Datei mit Hauptstädten laden
script_path = Path(__file__).resolve()
repo_root = script_path.parents[1]
csv_path = repo_root / "country-capital-lat-long-population.csv"

hauptstädte = pd.read_csv(csv_path)

# Dictionary für Städte erstellen
stadt_koordinaten = {}
for _, row in hauptstädte.iterrows():
    stadt_name = f"{row['Capital City']}, {row['Country']}"
    stadt_koordinaten[stadt_name] = (row['latitude'], row['longitude'], row['Country'], row['Population'])

with st.echo(code_location="below"):
    # Standort-Auswahl
    col1, col2 = st.columns([2, 1])
    
    with col1:
        stadt = st.selectbox("Wähle eine Hauptstadt:", options=sorted(stadt_koordinaten.keys()))
    
    with col2:
        custom_lat = st.text_input("Breitengrad:", value=str(stadt_koordinaten[stadt][0]))
        custom_lon = st.text_input("Längengrad:", value=str(stadt_koordinaten[stadt][1]))
    
    # Koordinaten validieren
    try:
        lat = float(custom_lat)
        lon = float(custom_lon)
        land = stadt_koordinaten[stadt][2]
        population = stadt_koordinaten[stadt][3]
    except ValueError:
        st.error("Ungültige Koordinaten!")
        lat, lon, land, population = stadt_koordinaten[stadt]
    
    # Wetterdaten von Open-Meteo abrufen
    @st.cache_data(ttl=600)  # Cache für 10 Minuten
    def get_weather_data(lat, lon):
        url = f"https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": True,
            "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m",
            "daily": "temperature_2m_max,temperature_2m_min,weathercode",
            "timezone": "auto"
        }
        response = requests.get(url, params=params)
        return response.json()
    
    # Wetterdaten laden
    with st.spinner("Wetterdaten werden geladen..."):
        weather_data = get_weather_data(lat, lon)
    
    # Aktuelle Wetterdaten anzeigen
    if "current_weather" in weather_data:
        current = weather_data["current_weather"]
        
        st.subheader(f"Aktuelles Wetter für {stadt}")
        st.write(f"🏛️ Hauptstadt von {land} | 👥 Bevölkerung: {population:,}")
        
        met1, met2, met3, met4 = st.columns(4)
        
        with met1:
            st.metric("Temperatur", f"{current['temperature']}°C")
        
        with met2:
            st.metric("Windgeschwindigkeit", f"{current['windspeed']} km/h")
        
        with met3:
            st.metric("Windrichtung", f"{current['winddirection']}°")
        
        with met4:
            # Wetter-Code zu Beschreibung
            weather_codes = {
                0: "Klar", 1: "Überwiegend klar", 2: "Teilweise bewölkt",
                3: "Bewölkt", 45: "Neblig", 48: "Reifneblig",
                51: "Leichter Nieselregen", 53: "Nieselregen", 55: "Starker Nieselregen",
                61: "Leichter Regen", 63: "Regen", 65: "Starker Regen",
                71: "Leichter Schnee", 73: "Schnee", 75: "Starker Schnee",
                80: "Leichte Regenschauer", 81: "Regenschauer", 82: "Starke Regenschauer",
                95: "Gewitter", 96: "Gewitter mit Hagel", 99: "Schweres Gewitter mit Hagel"
            }
            weather_desc = weather_codes.get(current['weathercode'], "Unbekannt")
            st.metric("Wetter", weather_desc)
    
    # Leaflet-Karte mit Wetter-Layern erstellen
    st.subheader("Interaktive Wetterkarte")
    
    m = folium.Map(location=[lat, lon], zoom_start=8, control_scale=True)
    
    # Marker für gewählte Stadt
    folium.Marker(
        location=[lat, lon],
        popup=f"{stadt}<br>Land: {land}<br>Bevölkerung: {population:,}<br>Lat: {lat}, Lon: {lon}",
        tooltip=stadt,
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)
    
    # NOAA/NWS Wetter-Layer (kostenlos)
    noaa_layers = {
        "NOAA Radar": folium.TileLayer(
            tiles="https://mesonet.agron.iastate.edu/cgi-bin/wms/nexrad/n0r.cgi",
            attr="NOAA/NWS",
            name="NOAA Radar",
            overlay=True,
            control=True,
            format="image/png",
            transparent=True
        )
    }
    
    # OpenWeatherMap Wetter-Layer (optional, benötigt API-Key)
    api_key = st.text_input("OpenWeatherMap API-Key (optional für mehr Layer):", type="password")
    
    if api_key:
        openweather_layers = {
            "Temperatur": folium.TileLayer(
                tiles=f"https://tile.openweathermap.org/map/temp_new/{{z}}/{{x}}/{{y}}.png?appid={api_key}",
                attr="OpenWeatherMap",
                name="Temperatur",
                overlay=True,
                control=True
            ),
            "Wolken": folium.TileLayer(
                tiles=f"https://tile.openweathermap.org/map/clouds_new/{{z}}/{{x}}/{{y}}.png?appid={api_key}",
                attr="OpenWeatherMap",
                name="Wolken",
                overlay=True,
                control=True
            ),
            "Niederschlag": folium.TileLayer(
                tiles=f"https://tile.openweathermap.org/map/precipitation_new/{{z}}/{{x}}/{{y}}.png?appid={api_key}",
                attr="OpenWeatherMap",
                name="Niederschlag",
                overlay=True,
                control=True
            ),
            "Wind": folium.TileLayer(
                tiles=f"https://tile.openweathermap.org/map/wind_new/{{z}}/{{x}}/{{y}}.png?appid={api_key}",
                attr="OpenWeatherMap",
                name="Wind",
                overlay=True,
                control=True
            ),
            "Druck": folium.TileLayer(
                tiles=f"https://tile.openweathermap.org/map/pressure_new/{{z}}/{{x}}/{{y}}.png?appid={api_key}",
                attr="OpenWeatherMap",
                name="Luftdruck",
                overlay=True,
                control=True
            )
        }
        
        for layer in openweather_layers.values():
            m.add_child(layer)
    
    # NOAA Layer zur Karte hinzufügen
    for layer in noaa_layers.values():
        m.add_child(layer)
    
    # Layer-Control
    folium.LayerControl(collapsed=False).add_to(m)
    
    # Karte anzeigen
    with st.container(border=True):
        streamlit_folium.st_folium(m, width=1200, height=500)
    
    st.divider()
    
    # Zusätzliche Wetterdaten als Tabelle
    if "hourly" in weather_data:
        st.subheader("Stündliche Vorhersage")
        
        hourly_data = weather_data["hourly"]
        df = pd.DataFrame({
            "Zeit": pd.to_datetime(hourly_data["time"]).strftime("%H:%M"),
            "Temperatur (°C)": hourly_data["temperature_2m"],
            "Luftfeuchtigkeit (%)": hourly_data["relative_humidity_2m"],
            "Wind (km/h)": hourly_data["wind_speed_10m"]
        })
        
        # Nur nächste 24 Stunden zeigen
        df = df.head(24)
        st.dataframe(df, use_container_width=True)
    
    if "daily" in weather_data:
        st.subheader("Tägliche Vorhersage")
        
        daily_data = weather_data["daily"]
        df_daily = pd.DataFrame({
            "Datum": pd.to_datetime(daily_data["time"]).strftime("%d.%m.%Y"),
            "Max. Temp (°C)": daily_data["temperature_2m_max"],
            "Min. Temp (°C)": daily_data["temperature_2m_min"],
            "Wetter-Code": daily_data["weathercode"]
        })
        
        st.dataframe(df_daily, use_container_width=True)
    
    st.divider()
    st.write("Hinweis: OpenWeatherMap Layer benötigen einen API-Key. NOAA Layer sind kostenlos.")