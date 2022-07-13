import meraki 
import json 

# configuration parameters

# Configuration parameters and credentials for MERAKI
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'

resp = meraki.DashboardAPI (api_key=API_KEY)

# get the organizations
orgs = resp.organizations.getOrganizations()

params = {}
print ("*"*20)
print ("Organizations")
for org in orgs:
    #display the organizations
    print("Organization Name: {}".format(org[ "name"]))
    print ("Organization Id: {}".format(org["id"]))
    print("="*5)

    #remember the organization info flagged
    if org ["name"] == "DevNet Sandbox" :
        params ["organizationId"] = org["id" ]
print ("*"*40)

#get the organization's networks
networks = resp.organizations.getOrganizationNetworks \
    (params["organizationId"])
#get the networks
print ("Networks:")
for network in networks:
    print ("Network Name: {}".format (network["id"]))
    print ("Network Name: {}". format (network[ "name"]))
    print("="*5)

    #remember a specific network
    if network["name"] == "DevNet Sandbox ALWAYS ON":
        params["networkId"] = network["id"]
        print(params["networkId"])
print ("*"*40)

devices = resp.networks.getNetworkDevices(params["networkId"])
net_equipment = devices[0]
print("Devices")
print(net_equipment)
print("*"*40)
