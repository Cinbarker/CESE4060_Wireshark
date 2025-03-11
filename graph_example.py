import pandas as pd
import plotly.express as px

df = pd.read_feather("processed_data/coffee_company.feather")
df["Sniff_Timestamp"] = pd.to_datetime(df["Sniff_Timestamp"])  # Convert sniff timestamp to datetime
df = df[(df["Antenna_Signal_1"] != 0) & (df["Antenna_Noise"] != 0)]

print(df.info())

# Plot the Signal Quality against the Antenna Signal
# fig = px.scatter(df, x="Antenna_Signal_0", y="Signal_Quality", color="DataRate", title="Signal Quality vs Antenna Signal")
# fig.show()

# Plot the Antenna Signal against the Data Rate
# fig = px.scatter(df, x="DataRate", y="Antenna_Signal_1", title="Antenna Signal vs Data Rate")
# fig.show()

# plot data rate vs retry as a histogram where the labels are the data rates
# fig = px.histogram(df, x="DataRate", color="FC_Retry", title="Retry Count vs Data Rate", labels={"FC_Retry": "Retry Count", "DataRate": "Data Rate"})
# fig.show()

# Data rate vs retries
# fig = px.scatter(df, x="DataRate", y="FC_Retry", title="Data Rate vs Retry Count")
# fig.show()

# Retries vs FCS Status
# fig = px.scatter(df, x="FC_Retry", y="FCS_Status", title="Retry Count vs FCS Status")
# fig.show()

# Filter out points with antenna signal = 0 or antenna noise = 0


# # Antenna signal 1 vs time
# fig = px.scatter(df, x="Sniff_Timestamp", y="Antenna_Signal_1", title="Antenna Signal 1 vs Time")
# fig.show()
#
# fig = px.scatter(df, x="Sniff_Timestamp", y="Antenna_Noise", title="Antenna Noise vs Time")
# fig.show()

# Data rate vs time
# fig = px.scatter(df, x="Sniff_Timestamp", y="DataRate", color="FC_Retry", title="Data Rate vs Time")
# fig.show()

# Source a

# # Number of retries vs time in 5 minute bins, with stacked bar chart for rety or not retry
# df["Sniff_Timestamp"] = pd.to_datetime(df["Sniff_Timestamp"])
# retries = df.groupby([pd.Grouper(key="Sniff_Timestamp", freq="5min"), "FC_Retry"])["FC_Retry"].count().reset_index(name="Count")
# fig = px.bar(retries, x="Sniff_Timestamp", y="Count", color="FC_Retry", title="Number of Retries vs Time")
# fig.show()



# Number of retries vs time in 5 minute bins, with stacked bar chart data rates
# df["Sniff_Timestamp"] = pd.to_datetime(df["Sniff_Timestamp"])
# retries = df.groupby([pd.Grouper(key="Sniff_Timestamp", freq="5min"), "DataRate"])["FC_Retry"].sum().reset_index()
# fig = px.bar(retries, x="Sniff_Timestamp", y="FC_Retry", color="DataRate", title="Number of Retries vs Time")
# fig.show()

# df["Sniff_Timestamp"] = pd.to_datetime(df["Sniff_Timestamp"])
# retries = df.groupby(pd.Grouper(key="Sniff_Timestamp", freq="5min"))["FC_Retry"].sum().reset_index()
# fig = px.bar(retries, x="Sniff_Timestamp", y="FC_Retry", title="Number of Retries vs Time")
# fig.show()
#
# Number of messages sent vs time in 15 minute bins
# messages = df.groupby(pd.Grouper(key="Sniff_Timestamp", freq="5min"))["FC_Retry"].count().reset_index()
# fig = px.bar(messages, x="Sniff_Timestamp", y="FC_Retry", title="Number of Messages Sent vs Time")
# fig.show()


# Useful graphs:

# # # Antenna signal 0 vs signal quality
# fig = px.scatter(df, x="Antenna_Signal_0", y="Signal_Quality", color="DataRate", title="Signal Quality vs Antenna Signal")
# fig.show()

# # Antenna signal 1 vs signal quality
# fig = px.scatter(df, x="Antenna_Signal_1", y="Signal_Quality", color="DataRate", title="Signal Quality vs Antenna Signal")
# fig.show()

# # Antenna signal 0 vs antenna signal 1
# fig = px.scatter(df, x="Antenna_Signal_0", y="Antenna_Signal_1", color="DataRate", title="Antenna Signal 0 vs Antenna Signal 1")
# fig.show()


# Retries vs signal quality in stacked bar chart with retries as the bar color
# retries = df.groupby(["Antenna_Signal_0", "FC_Retry"])["FC_Retry"].count().reset_index(name="Count")
# fig = px.bar(retries, x="Antenna_Signal_0", y="Count", color="FC_Retry", title="Antenna Signal 0 vs Retries")
# fig.show()

# # df = df[(df["Antenna_Signal_1"] != 0) & (df["Antenna_Noise"] != 0) & (df["Antenna_Signal_1"] != -80)]
# retries = df.groupby(["Antenna_Signal_1", "FC_Retry"])["FC_Retry"].count().reset_index(name="Count")
# fig = px.bar(retries, x="Antenna_Signal_1", y="Count", color="FC_Retry", title="Antenna Signal 1 vs Retries")
# fig.show()



# # Antenna signal 1 vs time
# fig = px.scatter(df, x="Sniff_Timestamp", y="Antenna_Signal_1", title="Antenna Signal 1 vs Time")
# fig.show()

# # Antenna noise vs time
# fig = px.scatter(df, x="Sniff_Timestamp", y="Antenna_Noise", title="Antenna Noise vs Time")
# fig.show()

# noise vs signal
# fig = px.scatter(df, x="Antenna_Noise", y="Antenna_Signal_1", color="DataRate", title="Antenna Noise vs Antenna Signal 1")
# fig.show()


# # See how many packets are broadcasts and directed based on the destination address
# df["Dest_Addr"] = df["Dest_Addr"].apply(lambda x: x.lower())
# broadcasts = df[df["Dest_Addr"] == "ff:ff:ff:ff:ff:ff"]
# directed = df[df["Dest_Addr"] != "ff:ff:ff:ff:ff:ff"]
# print(f"Broadcasts: {len(broadcasts)}")
# print(f"Directed: {len(directed)}")
#
# # Histogram of data rates
# fig = px.histogram(df, x="DataRate", title="Data Rate Histogram")
# fig.show()


# histogram of antenna signal 1 when antenna noise is -93
# noise = df[df["Antenna_Noise"] == -93]
# fig = px.histogram(noise, x="Antenna_Signal_1", title="Antenna Signal 1 when Antenna Noise is -93")
# fig.show()

# # Make a pie chart of the Src_Names in the data that aren't null
# df_filtered = df[["Src_Name", "Dst_Name"]].copy()
# df_filtered = df_filtered.melt(value_name="Host").dropna(subset=["Host"])
# hostname_counts = df_filtered["Host"].value_counts().reset_index()
# hostname_counts.columns = ["Host", "Count"]
#
# # Calculate total and percentage for each host
# total = hostname_counts["Count"].sum()
# hostname_counts["Percent"] = hostname_counts["Count"] / total * 100
#
# # Create pie chart using the custom label
# fig = px.pie(
#     hostname_counts,
#     names="Host",
#     values="Count",
#     title="Distribution of Accessed Hostnames (Non-Null)",
#     hole=0.3,
# )
#
# fig.update_traces(textposition="inside", textinfo="percent+label")
# fig.show()


# print all unique hosts that used chatgpt.com


# # Exclude specific addresses
# excluded_addresses = ["78:8a:20:d7:6c:53"]
# df_filtered = df.loc[~df['Trans_Addr'].isin(excluded_addresses)].copy()
# df_filtered["Interval"] = df_filtered["Sniff_Timestamp"].dt.floor("5min")
# device_counts = (df_filtered.groupby("Interval")["Trans_Addr"].nunique().reset_index(name="Unique_Devices"))
#
# # site = "chatgpt.com"
# site = "fbcdn.net"
# # Unique devices that used chatgpt.com (in Src_Name or Dst_Name) per interval
# chatgpt_counts = (
#     df_filtered[df_filtered["Src_Name"].str.contains(site, case=False, na=False) |
#                 df_filtered["Dst_Name"].str.contains(site, case=False, na=False)]
#                 .groupby("Interval")["Trans_Addr"].nunique().reset_index(name="ChatGPT_Devices")
# )
#
# # Merge the overall and ChatGPT-specific counts
# merged_counts = pd.merge(device_counts, chatgpt_counts, on="Interval", how="left")
# merged_counts["ChatGPT_Devices"].fillna(0, inplace=True)
#
# # Create a bar chart colored by the number of ChatGPT using devices
# fig = px.bar(
#     merged_counts,
#     x="Interval",
#     y="Unique_Devices",
#     color="ChatGPT_Devices",
#     title="Unique Devices and ChatGPT Usage Over Time",
#     color_continuous_scale="Viridis",
# )
#
# fig.update_layout(showlegend=True)
# fig.show()


# df["Interval"] = df["Sniff_Timestamp"].dt.floor("5min")
#
# # plot the number of unique devices over time in 1 min bins
# unique_devices = df.groupby("Interval")["Trans_Addr"].nunique().reset_index(name="Unique_Devices")
# fig = px.line(unique_devices, x="Interval", y="Unique_Devices", title="Number of Unique Devices Over Time")
# fig.show()
#
# # # plot the retries vs data rate in 5 min time bins
# total_messages = df.groupby("Interval")["FC_Retry"].count().reset_index(name="Total_Messages").copy()
# retries = df.groupby(["Interval", "DataRate"])["FC_Retry"].sum().reset_index().copy()
# retries = retries.merge(total_messages, on="Interval")
# retries["Retry_Percentage"] = retries["FC_Retry"] / retries["Total_Messages"] * 100
# fig = px.bar(retries, x="Interval", y="Retry_Percentage", color="DataRate", title="Retry Percentage vs Data Rate Over Time")
# fig.show()
#
#
# # plot FCS_Status errors over time in 5 min bins colored by the data rate
# fcs_errors = df.groupby(["Interval", "DataRate"])["FCS_Status"].apply(lambda x: (x == 1).sum()).reset_index(name="Good_FCS").copy()
# fcs_errors["Bad_FCS"] = df.groupby(["Interval", "DataRate"])["FCS_Status"].apply(lambda x: (x == 0).sum()).values
# fcs_errors["Total_Messages"] = df.groupby("Interval")["FCS_Status"].count().values
# fcs_errors["Error_Percentage"] = fcs_errors["Bad_FCS"] / fcs_errors["Total_Messages"] * 100
# fig = px.bar(fcs_errors, x="Interval", y="Error_Percentage", color="DataRate", title="FCS Error Percentage Over Time")
# fig.show()

# plot snr over time
# fig = px.scatter(df, x="Sniff_Timestamp", y="SNR", title="SNR Over Time")
# fig.show()


# plot Data rate vs unique devices in 1 min bins as a scatter plot


# Make a histogram of the subtypes for type 0 frames
type_0 = df[df["FC_Type"] == 2]
fig = px.histogram(type_0, x="FC_Subtype", title="Subtype Histogram for Type 0 Frames")
fig.show()