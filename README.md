# headerpy
A CLI HTTP(S) Header fuzzer, we fuzz so you don't need to.

## Installation
```
git clone --depth 1 https://github.com/Armageddon0x00/headerpy
cd headerpy/
pip install -r requirements.txt
```

## Help Output
```
godkiller@ubuntu-vm-1:~/Safe_Place/header$ ./header.py -h
usage: python3 header.py --url https://target_domain.com

Fuzz HTTP Headers for missing pieces. Enter the realm of justice.

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     URL to fuzz for. Please enter as http(s)://target_domain.com
  -f FILENAME, --filename FILENAME
                        File containing domains and subdomains
  -m [METHOD], --method [METHOD]
                        Define HTTP Method. Currently supports GET, and POST. Default:GET
  -s [STATUSCODE], --statuscode [STATUSCODE]
                        Set HTTP status code to show for. Default:200 OK
  -v [VERIYFCERT], --veriyfcert [VERIYFCERT]
                        Should SSL Certificate be verified? Default:True
```

## Single URL Parsing
```
godkiller@ubuntu-vm-1:~/Safe_Place/header$ ./header.py --url https://trendyol.com

	 _                    _                       
	| |                  | |                      
	| |__   ___  __ _  __| | ___ _ __ _ __  _   _ 
	| '_ \ / _ \/ _` |/ _` |/ _ \ '__| '_ \| | | |
	| | | |  __/ (_| | (_| |  __/ |_ | |_) | |_| |
	|_| |_|\___|\__,_|\__,_|\___|_(_)| .__/ \__, |
	                                 | |     __/ |
	                                 |_|    |___/                                 
	
A CLI HTTP(S) Header fuzzer, we fuzz so you don't need to. 


############################################################
########################RESULTS#############################
############################################################


Target               Missing Headers
------               ---------------
			
https://trendyol.com Content-Security-Policy GET 200
https://trendyol.com Strict-Transport-Security GET 200
https://trendyol.com X-Frame-Options GET 200
```

## Parsing Multiple URL from file
```
godkiller@ubuntu-vm-1:~/Safe_Place/header$ ./header.py -f exampledomains.txt  -m GET -s 200

	 _                    _                       
	| |                  | |                      
	| |__   ___  __ _  __| | ___ _ __ _ __  _   _ 
	| '_ \ / _ \/ _` |/ _` |/ _ \ '__| '_ \| | | |
	| | | |  __/ (_| | (_| |  __/ |_ | |_) | |_| |
	|_| |_|\___|\__,_|\__,_|\___|_(_)| .__/ \__, |
	                                 | |     __/ |
	                                 |_|    |___/                                 
	
A CLI HTTP(S) Header fuzzer, we fuzz so you don't need to. 


############################################################
########################RESULTS#############################
############################################################


Target               Missing Headers
------               ---------------
			
https://google.com Cache-Control GET 200
https://google.com Strict-Transport-Security GET 200
https://google.com X-XSS-Protection GET 200
https://google.com X-Frame-Options GET 200

Target               Missing Headers
------               ---------------
			
https://yandex.com Cache-Control GET 200
https://yandex.com Content-Security-Policy GET 200
https://yandex.com X-Frame-Options GET 200
```

## Method, SSL Cert and Status Code Check
```
godkiller@ubuntu-vm-1:~/Safe_Place/header$ ./header.py -u https://yandex.com -m POST -s 200 -v False

	 _                    _                       
	| |                  | |                      
	| |__   ___  __ _  __| | ___ _ __ _ __  _   _ 
	| '_ \ / _ \/ _` |/ _` |/ _ \ '__| '_ \| | | |
	| | | |  __/ (_| | (_| |  __/ |_ | |_) | |_| |
	|_| |_|\___|\__,_|\__,_|\___|_(_)| .__/ \__, |
	                                 | |     __/ |
	                                 |_|    |___/                                 
	
A CLI HTTP(S) Header fuzzer, we fuzz so you don't need to. 


############################################################
########################RESULTS#############################
############################################################

Target               Missing Headers
------               ---------------
			
https://yandex.com Cache-Control POST 200
https://yandex.com Content-Security-Policy POST 200
https://yandex.com X-Frame-Options POST 200

```

### TODOs
- Disable SSL warning when cert is not checked
- Fix Dradis export function
- Fix 10 requsts to be random user-agent and method each.
- Fix report_template array to function within our scope
- Add checking function for server/version headers.