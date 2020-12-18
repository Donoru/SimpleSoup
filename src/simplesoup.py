import requests
from bs4 import BeautifulSoup

headers = {
    'Access-Control-Allow-Origin':'*',
    'Access-Control-Allow-Methods':'GET',
    'Access-Control-Allow-Headers':'Content-Type',
    'Access-Control-Max-Age':'3600',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

class WebsiteNotFound(Exception):
    pass

def scrape(url, useHeaders, tag, returnAsArray):
    if url and isinstance(url, str):
        if useHeaders == True:
            try:
                site = requests.get(url, headers)
            except:
                raise WebsiteNotFound("Does the provided URL start with 'http://' or 'https://'? If not, that's why this error occurred. Otherwise, that website doesn't exist.")
            else:
                scraper = BeautifulSoup(site.content, "html.parser")
                if tag != "":
                    if returnAsArray == True:
                        return scraper.find_all(tag)
                    elif returnAsArray == False:
                        return "\n".join(scraper.find_all(tag))
                    else:
                        raise TypeError("Fourth argument (returnAsArray) must be a boolean value")
                elif tag == "":
                    return scraper.prettify()
                else:
                    raise TypeError("Third argument (tag) must be a string value, either the tag name or an empty string")
        elif useHeaders == False:
            try:
                site = requests.get(url, {})
            except:
                raise WebsiteNotFound("Does the provided URL start with 'http://' or 'https://'? If not, that's why this error occurred. Otherwise, that website doesn't exist.")
            else:
                scraper = BeautifulSoup(site.content, "html.parser")
                if tag != "":
                    if returnAsArray == True:
                        return scraper.find_all(tag)
                    elif returnAsArray == False:
                        return "\n".join(str(item) for item in scraper.find_all(tag))
                    else:
                        raise TypeError("Fourth argument (returnAsArray) must be a boolean value")
                elif tag == "":
                    return scraper.prettify()
                else:
                    raise TypeError("Third argument (tag) must be a string value, either the tag name or an empty string")
        else:
            raise TypeError("Second argument (useHeaders) must be a boolean value")
    else:
        raise TypeError("First argument (url) must be a string value")
