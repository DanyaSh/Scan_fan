# Scan_fan😎
-------------------------------------------------------------------------------------------------------
Bot uploads torrents to working directory from rutracker.org based on preference in config.py file
-------------------------------------------------------------------------------------------------------


0 Preliminary deeds 
-------------------------------------------------------------------------------------------------------
0.1) Install Python3  (https://www.python.org/)

0.2) Install libraries, input (one by one) to cmd or terminal:

pip3 install requests

pip3 install bs4

pip3 install fake_useragent


1 Editing the code for yourself
-------------------------------------------------------------------------------------------------------
1.2) Rename file  your_config.py to config.py and fill in the lines (with personal data and preferences):

selection='1105'        # 1105 for Аниме (HD Video) - you can see the last digits in the link (rutracker.org/forum/tracker.php?f=1105)

maxGB=20                #max value of files for upload

minLS=1                 #min division leech/sid for upload (for example 1)

your_maxGB=500          #your value for work (for example 500)

max_len_tor=200         #how much torrents you will can process (for example 200)


2 Set up a torrent client 
-------------------------------------------------------------------------------------------------------
2.1) In the torrent client, select the folder for autoloading torrents from the folder

2.2) In the torrent client, select a folder for downloading files + disable the dialog prompt when adding a torrent
