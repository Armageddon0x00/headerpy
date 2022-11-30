#!/usr/bin/python3

# Licensed under my will. :)
# CAI sent his regards.

import requests
import argparse
import validators
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

user_agent_array = [
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:102.0) Gecko/20100101 Firefox/102.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:106.0) Gecko/20100101 Firefox/106.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0",
"Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0",
"Mozilla/5.0 (Windows NT 10.0; rv:106.0) Gecko/20100101 Firefox/106.0",
"Mozilla/5.0 (Windows NT 10.0; rv:107.0) Gecko/20100101 Firefox/107.0",
"Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.5.710 Yowser/2.5 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.106",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.24",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0",
"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0"
]

parser = argparse.ArgumentParser(description='Fuzz HTTP Headers for missing pieces. Enter the realm of justice.',
					prog='header.py', usage='python3 header.py --url https://target_domain.com')

parser.add_argument('-u', '--url', help='URL to fuzz for. Please enter as http(s)://target_domain.com')
parser.add_argument('-f', '--filename', help='File containing domains and subdomains')
parser.add_argument('-m', '--method', help='Define HTTP Method. Currently supports GET, and POST. Default:GET', 
					nargs='?', default="GET", type=str)
parser.add_argument('-s', '--statuscode', help='Set HTTP status code to show for. Default:200 OK', 
					nargs='?', default=200, type=int)
parser.add_argument('-v', '--veriyfcert', help='Should SSL Certificate be verified? Default:True', 
					nargs='?', default="True", type=str)
# TODO
# ADD COOKIE
# ADD DRADIS PARSING
# FIX STATUS CODE - SHOW ALL
# FIX RANDOMIZER

def print_entry():
	print(bcolors.OKCYAN + """
	 _                    _                       
	| |                  | |                      
	| |__   ___  __ _  __| | ___ _ __ _ __  _   _ 
	| '_ \ / _ \/ _` |/ _` |/ _ \ '__| '_ \| | | |
	| | | |  __/ (_| | (_| |  __/ |_ | |_) | |_| |
	|_| |_|\___|\__,_|\__,_|\___|_(_)| .__/ \__, |
	                                 | |     __/ |
	                                 |_|    |___/                                 
	""" + bcolors.ENDC)

	print(bcolors.OKCYAN + "A CLI HTTP(S) Header fuzzer, we fuzz so you don't need to. \n" + bcolors.ENDC)


def read_from(file): # lulz
	testsite_array = []
	with open(file, 'r') as my_file:
		for line in my_file:
			testsite_array.append(line.strip())

	return testsite_array

def get_status_and_headers(target_url, show_status, target_method, verify_choice):
	return_array_positive = []
	return_array_negative = []

	for i in range(10):
		user_agent = random.choice(user_agent_array)

		our_headers = {
		'User-Agent': user_agent
		}
		
		#response = requests.get(target_url, headers=our_headers, verify=verify_choice)

		if target_method == "GET":	
			response = requests.get(target_url, headers=our_headers, verify=verify_choice)
		elif target_method == "POST":
			response = requests.post(target_url, headers=our_headers, verify=verify_choice)
		
		url_status = response.status_code

		if url_status != show_status:
			print(bcolors.WARNING + "Invalid Status Code for domain. Got: " + str(url_status) + "  Wanted:" + str(show_status) + bcolors.ENDC)
		
		# Check for our report template first.
		# 0 = Cache Control
		# 1 = Content Security Policy
		# 2 = HSTS
		# 3 = X-XSS-Protection
		# 4 = X-Frame-Options
		report_template = ['Cache-Control', 'Content-Security-Policy', 'Strict-Transport-Security',
		 'X-XSS-Protection', 'X-Frame-Options', 'Secure', 'HttpOnly', 'SameSite']

		url_headers = response.headers
		for report_header in report_template:
			if str(report_header) in url_headers:
				return_array_positive.append(report_header)
			else:
				return_array_negative.append(report_header) 

		#print(return_array_positive)
		#print(return_array_negative)

		# Clear dups before returning
		return_array_positive = list(dict.fromkeys(return_array_positive))
		return_array_negative = list(dict.fromkeys(return_array_negative))
	return return_array_positive, return_array_negative

def print_results(url, selected_method, show_status, positives, negatives):	
	print("""
Target               Missing Headers
------               ---------------
			""")

	for poz in positives:
		print(bcolors.WARNING + str(url) + " " + poz + " " + str(selected_method) + " " + str(show_status) + bcolors.ENDC)

def output_in_dradis():
	print("TODO")

args = parser.parse_args()

file_array = []
poz_array = []
neg_array = []

print_entry()

print(bcolors.OKCYAN + """
############################################################
########################RESULTS#############################
############################################################
""" + bcolors.ENDC)

target_method = args.method

target_status_code = args.statuscode

if args.veriyfcert == "True": #  argparse does not support bools out of the box. So we do this.
	target_verifycert = True
else:
	target_verifycert = False

if args.filename == None:
	if  args.url != "http://catakantest.net":
		if not validators.url(str(args.url)):
			print(bcolors.WARNING + "Invalid URL! Please enter a valid URL (HTTP/HTTPS) or leave me alone.\n" + bcolors.ENDC)
			exit()
		else:
			target_url = args.url
			poz_array, neg_array = get_status_and_headers(target_url, target_status_code, target_method, target_verifycert)
			print_results(target_url, target_method, target_status_code, poz_array, neg_array)
else:
	target_filename = args.filename 
	file_array = read_from(target_filename)
	for host_name in file_array:
		poz_array, neg_array = get_status_and_headers(host_name, target_status_code, target_method, target_verifycert)
		print_results(host_name, target_method, target_status_code, poz_array, neg_array)