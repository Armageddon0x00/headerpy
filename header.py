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

parser.add_argument('-u', '--url', help='URL to fuzz for. Please enter as http(s)://target_domain.com', 
					action='store', nargs='?', const="https://catakantest.com", type=str)
parser.add_argument('-f', '--filename', help='File containing domains and subdomains', 
					action='store')
parser.add_argument('-r', '--randomize', 
					help='Randomize User-Agent, sends multiple requests to same site with different User-Agents', 
					action='store', nargs='?', const=0, type=bool)
parser.add_argument('-m', '--method', help='Define HTTP Method. Currently supports GET, and POST. Default:GET', 
					action='store', nargs='?', const="GET", type=str)
parser.add_argument('-s', '--statuscode', help='Set HTTP status code to show for. Default:200 OK', 
					action='store', nargs='?', const=200, type=int)
parser.add_argument('-d', '--dradis', help='Export in Dradis format for tabling under, header.dradis', 
					action='store')
# TODO
# ADD COOKIE
# ADD DRADIS PARSING
# FIX STATUS CODE - SHOW ALL
# FIX RANDOMIZER

args = parser.parse_args()

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

def get_status_and_headers(target_url, show_status=200, method="GET", user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", target_randomize='0'):
	return_array_positive = []
	return_array_negative = []

	user_agent = random.choice(user_agent_array)

	our_headers = {
	'User-Agent': user_agent
	}

	if target_randomize:
		if method == "GET":	
			response = requests.get(target_url, headers=our_headers)
		elif method == "POST":
			response = requests.post(target_url, headers=our_headers)
	else:	
		if method == "GET":	
			response = requests.get(target_url)
		elif method == "POST":
			response = requests.post(target_url)
	
	url_status = response.status_code
	if url_status != show_status:
		print(bcolors.WARNING + "Invalid Status Code for: " + str(target_url) + " " + str(url_status) + bcolors.ENDC)
	
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
	
	return return_array_positive, return_array_negative

def print_results(url, selected_method, show_status, positives, negatives):	
	print("""
Target               Missing Headers               Method               Status Code
------               ---------------               ------               -----------
			""")

	for poz in positives:
		print(bcolors.WARNING + str(url) + "               " + poz + "               " + str(selected_method)+ "               " + str(show_status) + bcolors.ENDC)

def main():
	file_array = []

	print_entry()

	if args.method == None:
		target_method = "GET"
	else:
		target_method = args.method

	if args.statuscode == None:
		target_status_code = 200
	else:
		target_status_code = args.statuscode

	if args.filename == None:
		target_filename = None
	else:
		target_filename = args.filename

	target_randomize = args.randomize
	
	# MY HEAD HURTS.
	try: 
		file_array = read_from(target_filename)
	except:
		file_array = []
	print(bcolors.OKCYAN + """
############################################################
########################RESULTS#############################
############################################################
		""" + bcolors.ENDC)

	if not file_array:		
		if validators.url(str(args.url)):
			target_url = args.url
			print(bcolors.OKGREEN + "Starting Enumeration for: | URL: " + str(target_url) + " | Method: " +  str(target_method) + " | Listing Status Code: " + str(target_status_code) + " |" + bcolors.ENDC)
			positive_list, negative_list = get_status_and_headers(target_url)

		else:
			print(bcolors.WARNING + "Invalid URL! Please enter a valid URL (HTTP/HTTPS) or leave me alone.\n" + bcolors.ENDC)
			exit()
	else:
		for target_url in file_array:
			positive_list, negative_list = get_status_and_headers(target_url)
			print_results(target_url, target_method, target_status_code, positive_list, negative_list)



main()