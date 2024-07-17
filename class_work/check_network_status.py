def check_network_status(net_con, firewall): 
    if net_con == True and firewall == True:
        return "No issues detected"
    elif net_con == True and firewall == False:
        return "Proceed with caution"
    elif net_con == False and (firewall == True or firewall == False):
        return "Network not detected"
    else:
        if (net_con != True or net_con != False) or (firewall != True or firewall != False):
            return "Unexpected network status"
        pass
    return net_con, firewall

# No issues detected
#print(check_network_status(True, True))

# Unexpected network status
#print(check_network_status(True, "Nope"))