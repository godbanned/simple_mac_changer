import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change the MAC address of")
    parser.add_option("-m", "--mac", dest="new_mac", help="New desired MAC address")
    
    (options, arguments) = parser.parse_args()
    
    if not options.interface:
        parser.error("Perhaps you forgot an interface? Use --help for more info.")

    elif not options.new_mac:
        parser.error("Perhaps you forgot an MAC? Use --help for more info.")
        
    return options


def change_mac(inter, mac):
    print("Changing MAC Address for: " + inter + " to " + mac)

    subprocess.call(["ifconfig", inter, "down"])
    subprocess.call(["ifconfig", inter, "hw", "ether", mac])
    subprocess.call(["ifconfig", inter, "up"])


options = get_arguments()
change_mac(inter=options.interface, mac=options.new_mac)
