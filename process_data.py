import pyshark
import pandas as pd
import socket

import tldextract

# Coffee Company Old - 78:8a:20:d7:6c:53
# file_name = "raw_data/coffee_company_fixed.pcap"
# display_filter = 'wlan.bssid == 78:8a:20:d7:6c:53'
# output_file = "processed_data/coffee_company.feather"

# Ikea - f0:1d:2d:63:e2:2b, f0:1d:2d:63:e2:29, 00:27:e3:7d:cb:81, f0:1d:2d:64:03:4b, f0:1d:2d:64:03:49, f0:1d:2d:63:f7:c9, f0:1d:2d:63:f7:cb, 00:27:e3:82:00:cb, 00:27:e3:81:cc:2b, 00:27:e3:82:00:c9, 00:27:e3:81:d1:a1, 00:27:e3:86:3e:0b, f0:1d:2d:65:d2:6b, f0:1d:2d:65:d2:69, f0:1d:2d:65:e6:49, f0:1d:2d:65:e6:4b, 00:27:e3:81:cc:21, 00:27:e3:7d:b7:81, f0:1d:2d:63:c4:a9, f0:1d:2d:66:f2:0b, f0:1d:2d:66:f2:09, f0:1d:2d:63:c4:ab, f0:1d:2d:63:c4:ab, 00:27:e3:81:ce:61, 00:27:e3:90:62:a1, 00:27:e3:90:64:c9, f0:1d:2d:65:d2:61, 00:27:e3:7d:c9:a1, 00:27:e3:7d:c9:ab, 00:27:e3:81:99:cb, f0:1d:2d:65:dc:c1, 00:27:e3:81:99:c9, f0:1d:2d:63:cb:a9, 00:27:e3:90:64:cb, f0:1d:2d:63:cb:ab, f0:1d:2d:65:ce:81, 00:27:e3:82:01:61, f0:1d:2d:64:02:e1, f0:1d:2d:66:dc:a1, f0:1d:2d:63:f7:c1, f0:1d:2d:63:e2:21, 00:27:e3:82:00:c1, f0:1d:2d:65:e6:41, f0:1d:2d:63:c4:a1, 00:27:e3:86:3e:01, f0:1d:2d:64:03:41, f0:1d:2d:63:cc:81, 00:27:e3:81:fd:6b, 00:27:e3:81:d5:a1, f0:1d:2d:63:cb:a1, f0:1d:2d:65:ea:a1, 00:27:e3:81:c3:a1, 00:27:e3:81:fd:61, f0:1d:2d:63:f1:01, f0:1d:2d:65:e9:81, f0:1d:2d:66:f2:01, f0:1d:2d:63:cd:e1, 00:27:e3:7d:cc:81, f0:1d:2d:65:e0:c1, 00:27:e3:81:d1:ab, f0:1d:2d:63:fe:e1, 00:27:e3:7d:cb:8b, f0:1d:2d:63:ff:41
file_name = "raw_data/Mar_8_Ikea_2.pcapng"
display_filter = ''
bssids = ["f0:1d:2d:63:e2:2b", "f0:1d:2d:63:e2:29", "00:27:e3:7d:cb:81", "f0:1d:2d:64:03:4b", "f0:1d:2d:64:03:49", "f0:1d:2d:63:f7:c9", "f0:1d:2d:63:f7:cb", "00:27:e3:82:00:cb", "00:27:e3:81:cc:2b", "00:27:e3:82:00:c9", "00:27:e3:81:d1:a1", "00:27:e3:86:3e:0b", "f0:1d:2d:65:d2:6b", "f0:1d:2d:65:d2:69", "f0:1d:2d:65:e6:49", "f0:1d:2d:65:e6:4b", "00:27:e3:81:cc:21", "00:27:e3:7d:b7:81", "f0:1d:2d:63:c4:a9", "f0:1d:2d:66:f2:0b", "f0:1d:2d:66:f2:09", "f0:1d:2d:63:c4:ab", "f0:1d:2d:63:c4:ab", "00:27:e3:81:ce:61", "00:27:e3:90:62:a1", "00:27:e3:90:64:c9", "f0:1d:2d:65:d2:61", "00:27:e3:7d:c9:a1", "00:27:e3:7d:c9:ab", "00:27:e3:81:99:cb", "f0:1d:2d:65:dc:c1", "00:27:e3:81:99:c9", "f0:1d:2d:63:cb:a9", "00:27:e3:90:64:cb", "f0:1d:2d:63:cb:ab", "f0:1d:2d:65:ce:81", "00:27:e3:82:01:61", "f0:1d:2d:64:02:e1", "f0:1d:2d:66:dc:a1", "f0:1d:2d:63:f7:c1", "f0:1d:2d:63:e2:21", "00:27:e3:82:00:c1", "f0:1d:2d:65:e6:41", "f0:1d:2d:63:c4:a1", "00:27:e3:86:3e:01", "f0:1d:2d:64:03:41", "f0:1d:2d:63:cc:81", "00:27:e3:81:fd:6b", "00:27:e3:81:d5:a1", "f0:1d:2d:63:cb:a1", "f0:1d:2d:65:ea:a1", "00:27:e3:81:c3:a1", "00:27:e3:81:fd:61", "f0:1d:2d:63:f1:01", "f0:1d:2d:65:e9:81", "f0:1d:2d:66:f2:01", "f0:1d:2d:63:cd:e1", "00:27:e3:7d:cc:81", "f0:1d:2d:65:e0:c1", "00:27:e3:81:d1:ab", "f0:1d:2d:63:fe:e1", "00:27:e3:7d:cb:8b", "f0:1d:2d:63:ff:41"]
for bssid in bssids:
    display_filter += f'wlan.bssid == {bssid} || '
display_filter = display_filter[:-4]
output_file = "processed_data/ikea.feather"

# Coffee Company New - 78:8a:20:d7:67:aa, 7e:8a:20:d7:67:aa
# file_name = "raw_data/Coffee_Company_March_06.pcapng"
# display_filter = 'wlan.bssid == 78:8a:20:d7:67:aa || wlan.bssid == 7e:8a:20:d7:67:aa'
# output_file = "processed_data/coffee_company.feather"

# Bagels and Beans - 8a:83:94:9c:e3:8b, 62:68:c8:e6:39:fe
# file_name = "raw_data/bagels_and_beans_fixed.pcap"
# display_filter = 'wlan.bssid == 8a:83:94:9c:e3:8b || wlan.bssid == 62:68:c8:e6:39:fe'
# output_file = "processed_data/bagels_and_beans.feather"

# Anne and Max - d0:21:f9:bf:91:05, d2:21:f9:cf:91:05, d2:21:f9:af:91:05
# file_name = "raw_data/anne_and_max_fixed.pcap"
# display_filter = 'wlan.bssid == d0:21:f9:bf:91:05 || wlan.bssid == d2:21:f9:cf:91:05 || wlan.bssid == d2:21:f9:af:91:05'
# output_file = "processed_data/anne_and_max.feather"

cap = pyshark.FileCapture(file_name, display_filter=display_filter, use_ek=True, keep_packets=False)

# # Print out all unique BSSIDs and their SSIDs
# bssids = {}
# counts = {}
# counter = 0
# for packet in cap:
#     counter += 1
#     if counter > 100000:
#         break
#     try:
#         bssid = getattr(packet.wlan, 'bssid', None)
#         ssid = getattr(packet, "wlan.mgt", None).wlan_ssid.showname.split(":")[1].strip().strip('"')
#
#     except AttributeError:
#         continue
#     if bssid is not None and ssid is not None:
#         if bssid in bssids.keys() and bssids[bssid] == ssid:
#             counts[bssid] += 1
#         elif bssid not in bssids.keys():
#             bssids[bssid] = ssid
#             counts[bssid] = 1
#             # print(f'{bssid} {ssid}')
#
# # Print bssids and their counts in sorted order of counts from highest to lowest
# print("\n\n")
# for bssid, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
#     print(f"{bssid} {bssids[bssid]} {count}")
#
# exit()

# List to store parsed packet data
packet_data = []
dns_map = {}
count = 0
# Iterate through packets and extract relevant fields
for packet in cap:
    count += 1
    if count % 1000 == 0:
        print(f"\rProcessed {count} packets", end="")
    try:
        # Extracting essential fields
        fcs_status = getattr(packet.wlan, 'fcs_status', None)
        fc_type = getattr(packet.wlan.fc.type, 'value', None)
        fc_subtype = getattr(packet.wlan.fc, 'subtype', None)
        fc_retry = getattr(packet.wlan, 'fc_retry', None)
        ta = getattr(packet.wlan.ta, 'value', None)  # Transmitter Address
        ra = getattr(packet.wlan.ra, 'value', None)  # Receiver Address
        data_rate = getattr(packet.radiotap, 'datarate', None)
        ant_noise = getattr(packet.radiotap, 'dbm_antnoise', None)
        ant_signal = getattr(packet.radiotap, 'dbm_antsignal', None)
        signal_quality = getattr(packet.radiotap, 'quality', None)
        snr = getattr(packet.wlan_radio, 'snr', None)
        sniff_timestamp = getattr(packet, 'sniff_timestamp', None)

        ip_src, ip_dst, ip_src_name, ip_dst_name = None, None, None, None
        if hasattr(packet, "ip"):
            ip_src = getattr(packet.ip.src, 'value', None)
            ip_dst = getattr(packet.ip.dst, 'value', None)

        if hasattr(packet, "dns") and packet.wlan.fc.fromds:
            if type(packet.dns.a) is list:
                dns_map[packet.dns.a[1]] = packet.dns.qry.name.value
            else:
                dns_map[packet.dns.a] = packet.dns.qry.name.value

        # Append extracted data to list
        if type(ant_signal) is list:
            packet_data.append([fcs_status, fc_type, fc_subtype, fc_retry, ta, ra, ip_src, ip_dst, data_rate, ant_noise, ant_signal[0], ant_signal[1], signal_quality, snr, sniff_timestamp])
        else:
            packet_data.append([fcs_status, fc_type, fc_subtype, fc_retry, ta, ra, ip_src, ip_dst, data_rate, ant_noise, None, ant_signal, signal_quality, snr, sniff_timestamp])

    except AttributeError:
        continue  # Skip packet if any attribute is missing

# Convert the extracted data into a DataFrame

df = pd.DataFrame(packet_data, columns=["FCS_Status", "FC_Type", "FC_Subtype", "FC_Retry", "Trans_Addr", "Recv_Addr", "Src_IP", "Dst_IP", "DataRate", "Antenna_Noise", "Antenna_Signal_0", "Antenna_Signal_1", "Signal_Quality", "SNR", "Sniff_Timestamp"])

print("\nResolving DNS names...")
# Add DNS names to the DataFrame
def get_dns_name(ip):
    if ip is None:
        return None
    try:
        name = tldextract.extract(dns_map.get(ip, None)).registered_domain.lower()
    except AttributeError:
        name = None
    if name is not None:
        return name if name != "" else None
    try:
        name = tldextract.extract(socket.gethostbyaddr(ip)[0]).registered_domain.lower()
        dns_map[ip] = name
        return name if name != "" else None
    except socket.herror:
        return None

df["Src_Name"] = df["Src_IP"].apply(get_dns_name)
df["Dst_Name"] = df["Dst_IP"].apply(get_dns_name)

df.to_feather(output_file)
