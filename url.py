#############################################################################	
#									    #
#									    #
#		Get the base domain from any given url                      #
#			   Abhishek Singh				    #
#									    #
#									    #
#############################################################################			
import urllib.parse
def get_domain(url):
    u = urllib.parse.urlsplit(url)
    return u.netloc


def get_top_domain(url):
    domain = get_domain(url)
    domain_parts = domain.split('.')
    if len(domain_parts) < 2:
        return domain
    top_domain_parts = 2
    # if a domain's last part is 2 letter long, it must be country name
    if len(domain_parts[-1]) == 2:
        if domain_parts[-1] in ['uk', 'jp']:
            if domain_parts[-2] in ['co', 'ac', 'me', 'gov', 'org', 'net']:
                top_domain_parts = 3
        else:
            if domain_parts[-2] in ['com', 'org', 'net', 'edu', 'gov']:
                top_domain_parts = 3
    return '.'.join(domain_parts[-top_domain_parts:])

u=input('Enter the url bitches')
hell=get_top_domain(u)
print(hell)
print(type(hell))
