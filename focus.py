import datetime

sites_to_block = ['www.twitch.tv', 'www.steampowered.com', 'www.steamcommunity.com','steamcommunity.com', 'www.facebook.com', 'www.twitter.com', 'www.youtube.com', 'www.instagram.com', 'web.snapchat.com']

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.42.0.69"


def block_sites():
    t = datetime.datetime.now()
    hrnow = t.hour
    ct = datetime.datetime(2022, 12, 31, 19, 0, 0, 0)
    cthr = ct.hour
    et = datetime.datetime(2022, 12, 31, 20, 0, 0, 0)
    ehr = et.hour
    if hrnow == cthr and hrnow < ehr:
        print("unblocking sites")
        with open(hosts_path, 'r+') as hostsfile:
            lines = hostsfile.readlines()
            hostsfile.seek(0)
            for line in lines:
                if not any(site in line for site in sites_to_block):
                    hostsfile.write(line)
            hostsfile.truncate()
    else:
        print("blocking sites")
        with open(hosts_path, 'r+') as hostsfile:
            hosts_content = hostsfile.read()
            for site in sites_to_block:
                if site not in hosts_content:
                    hostsfile.write(redirect + " " + site + "\n")


if __name__ == "__main__":
    block_sites()

