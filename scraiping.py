from bs4 import BeautifulSoup
import requests

targets = ['犬', '猫']

for target in targets:
    url = 'https://www.google.com/search?q=' + target + '&tbm=isch&ved=2ahUKEwil6sjjw5_qAhWTL6YKHYGCBuEQ2-cCegQIABAA&oq=' + target + '&gs_lcp=CgNpbWcQAzICCAAyAggAMgIIADICCAAyCAgAELEDELEDMggIABCxAxCxAzICCAAyCAgAELEDELEDMgIIADIICAAQsQMQsQM6BAgjECc6BQgAELEDOgcIABCDARAEOgcIABCxAxAEOgQIABAEOgUIABCDAToHCCMQ6gIQJ1DeVFiXdWCXeWgCcAB4AIABgAGIAfoKkgEEMC4xM5gBAKABAaoBC2d3cy13aXotaW1nsAEK&sclient=img&ei=dvD1XqXXNpPfmAWBhZqIDg&bih=766&biw=1440&rlz=1C5CHFA_enJP877JP877'
    print(url)