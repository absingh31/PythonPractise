import urllib.request
import re

url = input("Enter the url")
response = urllib.request.urlopen(url)

data = response.read()

##################################################################
domain_regex = r'(?=^.{4,253}$)(^((?!-)[a-zA-Z0-9-]{1,63}(?<!-)\.)+[a-zA-Z]{2,63}\.?$)'

pattern = re.compile(domain_regex, re.UNICODE)

domain_file = open('domain_regex_file.txt','w')
for match in pattern.findall(data):
	domain_file.write("%s\n"%match)
domain_file.close()
##################################################################

##################################################################
ipv6_regex = r'(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))'

pattern2 = re.compile(ipv6_regex)

domain_file2 = open('ipv6_regex_file.txt','w')
for match in pattern2.findall(data):
	domain_file2.write("%s\n"%match)
domain_file2.close()
###################################################################

###################################################################
visa_regex = r'^(?:4[0-9]{12}(?:[0-9]{3})?'

pattern3 = re.compile(visa_regex)

domain_file3 = open('visa_regex_file.txt','w')
for match in pattern3.findall(data):
	domain_file3.write("%s\n"%match)
domain_file3.close()
###################################################################

###################################################################
ipv4_regex = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'

pattern4 = re.compile(ipv4_regex)

domain_file4 = open('ipv4_regex_file.txt','w')
for match in pattern4.findall(data):
	domain_file4.write("%s\n"%match)
domain_file4.close()
###################################################################
