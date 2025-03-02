import pandas as pd
import plotly.express as px

df = pd.read_feather("processed_data/bagels_and_beans.feather")

print(df.info())

# Plot the Signal Quality against the Antenna Signal in a heatmap
fig = px.scatter(df, x="Antenna_Signal_1", y="Signal_Quality", color="DataRate", title="Signal Quality vs Antenna Signal", labels={"Antenna_Signal_1": "Antenna Signal", "Signal_Quality": "Signal Quality", "DataRate": "Data Rate"})
fig.show()

# plot data rate vs retry as a histogram where the labels are the data rates

fig = px.histogram(df, x="DataRate", color="FC_Retry", title="Retry Count vs Data Rate", labels={"FC_Retry": "Retry Count", "DataRate": "Data Rate"})
fig.show()
