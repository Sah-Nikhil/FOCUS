Thankyou for trying out this script 
Commertial use is strictly prohibited without the consent of the Creator (https://github.com/xV3SPERx). Feel free to use it for individually.

STEPS TO AUTOMATE:
1- Download and extract files.
2- Post saving the files cut and paste the start.bat file into "C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    -->here <username> is your username...can be cross verified by Win+R -> cmd -> and noting the name which appears similarly in the commandline.
3- cut and paste the focus.py file into "C:\Windows\System32"
    -->You can edit the time in which you want to use the websites blocked( ie unlock the websites) by the script by editing the "ct = datetime.datetime(2022, 12, 31, 19, 0, 0, 0)" line in the code...edit the 4th numeral to change the start hour( accepted values are between 0 to 24). 
    -->You can edit the duration for which you want to use the websites blocked( ie unlock the websites) by the script by editing the "et = datetime.datetime(2022, 12, 31, 20, 0, 0, 0)" line in the code...edit the 4th numeral to change the end hour( accepted values are between 0 to 24).
    -->You can add or remove websites by making changes in the sites_to_block variable
      -->Currently blocked sites are ['www.twitch.tv', 'www.steampowered.com', 'www.steamcommunity.com','steamcommunity.com', 'www.facebook.com', 'www.twitter.com', 'www.youtube.com', 'www.instagram.com', 'web.snapchat.com']
