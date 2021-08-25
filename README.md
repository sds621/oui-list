# oui-list.py

This program will read in a list of mac addresses and create a new list containing
only the manufacturer identification (OUI) portion of the mac address, excluding duplicates, 
and print the results to a text file called "vendor_list.txt".

This repo contains a file with sample mac addresses that can be used to verify that the script is working properly. Feel free to replace this
file with a list of mac addresses relevent to you. Note: Ensure that you maintain the name of this file "unknown-macs.txt".

**INSTRUCTIONS**
1. Download all files in this repo to a directory on your local PC. 
2. Open up Command Prompt/Terminal
3. Navigate to the new directory containing the python script
   - oui-list-main\oui-list-main
5. Run the script
   - $ python mac-vendor-id.py
