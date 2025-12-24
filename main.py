import subprocess
import optparse
import re

def get_current_mac(inter):
    ifconfig_output = subprocess.check_output(["ifconfig", inter])
    mac_addr_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_output))

    if mac_addr_result:
        return mac_addr_result.group(0)
    else:
        print("Could not read MAC address.")


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
captured_mac = get_current_mac(options.interface)
print("Current MAC: " + str(captured_mac))

change_mac(inter=options.interface, mac=options.new_mac)

captured_mac = get_current_mac(options.interface)
if captured_mac == options.new_mac:
    print("MAC address was succesfully changed to: " + captured_mac)
else:
    print("MAC address failed to get changed.")