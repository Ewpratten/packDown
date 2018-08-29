import requests
from bs4 import BeautifulSoup
import wget

base_page = "https://pkgs.org/download/"

name = input("Package name?\n>")

page = requests.get(base_page + str(name))

if str(page) == "<Response [404]>":
	print("invalid package")
	exit(1)

soup = BeautifulSoup(page.text, 'html.parser')
dllist = soup.find('div', attrs={"id":"distro-88"})
anc = dllist.find('td', attrs={"class":"w-50 pl-4"})

page = requests.get("https://debian.pkgs.org/sid/debian-main-amd64/" + str(anc.find('a').text) + ".html")

soup = BeautifulSoup(page.text, 'html.parser')
dllink = soup.find('table', attrs={"class":"table table-bordered-2 table-hover table-sm1"})
dllink = dllink.find('a')
print("Found Link: " + str(dllink["href"]))

wget.download(str(dllink["href"]))