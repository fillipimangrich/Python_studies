from traceback import print_tb
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('Deu error')
else:
    print('Consegui acessar!')
