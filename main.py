import requests
import re
from multiprocessing import Pool
import subprocess
from bs4 import BeautifulSoup

headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
def get_mp4_url(page_url):
	response = requests.get(page_url, headers=headers)

	patterns = re.compile('videoUrl"\:"(.*?)"', re.S)
	url_list = re.findall(patterns, response.text)
	for url in url_list:
		if "720P" in url:
			url = url.replace("\\", "")
			return url
		else:
			return None

def get_mp4_name(page_url):
	response = requests.get(page_url, headers=headers).text
	soup = BeautifulSoup(response, 'lxml')
	name = soup.find("meta", {"name":"twitter:title"})["content"]
	return name

""" def get_mp4_file(mp4_url):
	with open('test.mp4', 'wb') as f:
		f.write(requests.get(mp4_url, headers=headers))
		f.close() """


def main():
	url = input("input URL:")
	page_url = url
	get_mp4_name
	mp4_url = get_mp4_url(page_url)
	name = get_mp4_name(page_url)
	subprocess.call(['wget', '-c', mp4_url, '-O', '{}.mp4'.format(name)])


if __name__=='__main__':
	main()