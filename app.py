
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from sensor_data import read_sensor_data

st.set_page_config(
    page_title="Aerolytix",
    page_icon="🫁",
    layout="wide"
)

st.title("Aerolytix")
st.subheader(
    "Intelligent Breath Analytics for Early Disease Screening"
)

st.warning(
    "Research prototype only. This application does not "
    "diagnose diseases or provide validated medical results."
)

if "readings" not in st.session_state:
    st.session_state.readings = []

if st.button("Capture Simulated Reading"):
    st.session_state.readings.append(read_sensor_data())

if st.session_state.readings:
    df = pd.DataFrame(st.session_state.readings)
    latest = df.iloc[-1]

    st.subheader("Latest Readings")

    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", f"{latest['temperature']} °C")
    col2.metric("Humidity", f"{latest['humidity']} %")
    col3.metric("Total Readings", len(df))

    st.subheader("Gas Sensor Readings")

    sensors = ["MQ2", "MQ3", "MQ7", "MQ135"]

    st.dataframe(
        df[["timestamp"] + sensors],
        use_container_width=True
    )

    st.subheader("Sensor Trend Graph")

    fig, ax = plt.subplots(figsize=(10, 4))

    for sensor in sensors:
        ax.plot(df.index, df[sensor], marker="o", label=sensor)

    ax.set_xlabel("Reading Number")
    ax.set_ylabel("Simulated Sensor Value")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)
    plt.close(fig)

    csv_data = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Sensor Data (CSV)",
        data=csv_data,
        file_name="aerolytix_sensor_data.csv",
        mime="text/csv"
    )
else:
    st.info(
        "Click 'Capture Simulated Reading' to begin."
    )
