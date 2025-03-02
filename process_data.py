import pyshark
import pandas as pd

# Coffee Company - 78:8a:20:d7:6c:53
# file_name = "raw_data/coffee_company_fixed.pcap"
# filter = 'wlan.sa == 78:8a:20:d7:6c:53 || wlan.da == 78:8a:20:d7:6c:53'
# output_file = "processed_data/coffee_company.feather"

# Bagels and Beans - 8a:83:94:9c:e3:8b, 62:68:c8:e6:39:fe
file_name = "raw_data/bagels_and_beans_fixed.pcap"
filter = 'wlan.sa == 8a:83:94:9c:e3:8b || wlan.da == 8a:83:94:9c:e3:8b || wlan.sa == 62:68:c8:e6:39:fe || wlan.da == 62:68:c8:e6:39:fe'
output_file = "processed_data/bagels_and_beans.feather"

# Anne and Max -

cap = pyshark.FileCapture(file_name, display_filter=filter, use_ek=True, keep_packets=False)

# List to store parsed packet data
packet_data = []
count = 0
# Iterate through packets and extract relevant fields
for packet in cap:
    count += 1
    if count % 1000 == 0:
        print(f"\rProcessed {count} packets", end="")
    try:
        # Extracting essential fields
        fcs_status = getattr(packet.wlan, 'fcs_status', None)
        fc_retry = getattr(packet.wlan, 'fc_retry', None)
        sa = getattr(packet.wlan.sa, 'value', None)  # Source Address
        da = getattr(packet.wlan.da, 'value', None)  # Destination Address
        datarate = getattr(packet.radiotap, 'datarate', None)
        ant_noise = getattr(packet.radiotap, 'dbm_antnoise', None)
        ant_signal = getattr(packet.radiotap, 'dbm_antsignal', None)
        signal_quality = getattr(packet.radiotap, 'quality', None)
        sniff_timestamp = getattr(packet, 'sniff_timestamp', None)

        # Append extracted data to list
        packet_data.append([fcs_status, fc_retry, sa, da, datarate, ant_noise, ant_signal[0], ant_signal[1], signal_quality, sniff_timestamp])

    except AttributeError:
        continue  # Skip packet if any attribute is missing

# Convert the extracted data into a DataFrame
df = pd.DataFrame(packet_data, columns=["FCS_Status", "FC_Retry", "Source_Addr", "Dest_Addr", "DataRate", "Antenna_Noise", "Antenna_Signal_0", "Antenna_Signal_1", "Signal_Quality", "Sniff_Timestamp"])
df.to_feather(output_file)
# Show results
print(df.head(10))
