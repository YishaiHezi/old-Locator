from address_excel_tools import Addresses_Excel_Tools
from names_excel_tools import Names_Excel_Tools
from flask import Flask, render_template, request, url_for, jsonify
import requests
import json


addresses_tools = Addresses_Excel_Tools()
names_tools = Names_Excel_Tools()


app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello! This is the locator app.'


@app.route('/macs', methods=['POST'])
def write_mac():
    input_json = request.get_json()
    client_mac = input_json['mac']
    client_name = input_json['name']
    print(client_mac)

    current_location = get_location(client_mac)

    write_mac_name_location_in_files(client_mac, client_name, current_location)

    return 'got it!'

@app.route('/names')
def get_location_of_name():
    input_json = request.get_json()
    name_to_find = input_json['name']
    location = get_location_from_name(name_to_find)

    if location:
        return location

    else:
        return 'Not found'


##########################################################################
def write_mac_name_location_in_files(mac, name, location):
    if not names_tools.find_key_in_excel(name):
        names_tools.write_mac_to_excel(mac, name)

    if not get_location_from_name(name):
        assign_mac_to_unknown_location(mac)

def assign_mac_to_unknown_location(current_mac):
    print(f'Your current location is unknown.')
    current_location = input(f'Please enter your current location: ')
    addresses_tools.write_mac_to_excel(current_mac, current_location)


def get_location(mac_address):

    macs_to_locations = addresses_tools.read_excel_to_dict()

    if mac_address in macs_to_locations:
        return macs_to_locations[mac_address]

    return None
##########################################################################


def get_location_from_name(name):
    desired_mac = names_tools.get_value_from_key(name)
    if desired_mac is not None:
        return addresses_tools.get_value_from_key(desired_mac)

    return None


app.run(debug=True, host="0.0.0.0", port=80)
