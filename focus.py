from datetime import datetime

sites_to_block = ['www.twitch.tv', 'www.steampowered.com', 'www.steamcommunity.com','steamcommunity.com', 'www.facebook.com', 'www.twitter.com', 'www.instagram.com', 'web.snapchat.com', 'www.literotica.com', 'www.pornhub.com', 'www.hqporner.com','www.ok.xxx', 'www.xhamster.desi','www.redtube.net']

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.42.0.69"


def block_sites():
    t = datetime.now()
    #hrnow = t.hour
    et = datetime(2023, 12, 12, 23, 0, 0, 0)
    if t < et:
        print("blocking sites")
        with open(hosts_path, 'r+') as hostsfile:
            hosts_content = hostsfile.read()
            for site in sites_to_block:
                if site not in hosts_content:
                    hostsfile.write(redirect + " " + site + "\n")
        
        
    else:
        print("unblocking sites")
        with open(hosts_path, 'r+') as hostsfile:
            lines = hostsfile.readlines()
            hostsfile.seek(0)
            for line in lines:
                if not any(site in line for site in sites_to_block):
                    hostsfile.write(line)
            hostsfile.truncate()


if __name__ == "__main__":
    block_sites()

