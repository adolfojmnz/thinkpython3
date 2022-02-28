import urllib.request

def retive_page(url):
    """ 
        Retive the contents of a web page.
        The content is converted to a string before returning it.
    """
    my_socket = urllib.request.urlopen(url)
    dta = str(my_socket.readall())
    my_socket.close()
    return dta


the_text = retive_page("http://xml.resource.org/public/rfc/txt/rfc793.txt")
print(the_text)
