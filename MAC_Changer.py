import subprocess
import optparse

print("""
------- MAC_CHANGER -------
  _____ _           _     _     _ _           _           
 |  __ (_)         | |   | |   | (_)         | |          
 | |__) | _ __ __ _| |_  | |__ | |_ _ __   __| | ___ _ __ 
 |  ___/ | '__/ _` | __| | '_ \| | | '_ \ / _` |/ _ \ '__|
 | |   | | | | (_| | |_  | |_) | | | | | | (_| |  __/ |   
 |_|   |_|_|  \__,_|\__| |_.__/|_|_|_| |_|\__,_|\___|_|   s
                     ______                               
                    |______|                              
""")

def opParser():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="user_interface", help="Enter your interface network")
    parser.add_option("-m", "--mac", dest="user_mac", help="Enter your mac address")
    (options, arguments) = parser.parse_args()
    if not options.user_interface:
        parser.error("Please enter your Interface, use --help for more infos")
    elif not options.user_mac:
        parser.error("Please enter your mac address, use --help for more infos")
    return options


def mac_changer(interface, new_mac):
    print("Changing MAC for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = opParser()
mac_changer(options.user_interface, options.user_mac)
