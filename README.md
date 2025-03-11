# CESE4060 - Wireless IoT and LAN - Wireshark Project - Group "Big Brother"

## Data Capture
Data capture is done in Wireshark in monitor mode, which is then stored in a pcap file in the [raw_data](raw_data) directory. This data is too large to be uploaded to GitHub.

## Data Processing
After a capture [process_data.py](process_data.py) is used to extract the useful information from the pcap file, which is then stored in pandas dataframes in feather files in the [processed_data](processed_data) directory.

## Data Analysis and Visualization
The jupyterlab notebook [process_data.ipynb](process_data.ipynb) is designed to be used in a Google colab environment. The notebook reads the processed feather files from this repo and processes the data to generate the plots and statistics.

- The flag `EXPORT_FIGURES` can be set to `True` to export the figures as SVG files. Otherwise the figures are displayed in the notebook.
- The flag `DOWNLOAD_FIGURES` can be set to `True` to download the figures as a zip file.


## Directory Structure
```
.
├── README.md                       : The file you are reading
├── process_data.ipynb              : Jupyter notebook for data analysis
├── process_data.py                 : Python script to process pcap files
├── raw_data                        : Directory for raw data
    ├── coffee_company_capture.pcap : Example pcap file
├── processed_data                  : Directory for processed data
    ├── coffee_company.feather      : Example processed data file
├── graph_example.py                : Sandbox for processing and plotting data
```