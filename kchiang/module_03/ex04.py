import asyncio
from requests_html import HTMLSession
from bs4 import BeautifulSoup

url = "https://weather.com/my/city/kuala-lumpur/today"

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
	"Accept-Language": "en-US,en;q=0.5",
}

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
session = HTMLSession()

def main():
	html_content: str = None
	try:
		response = session.get(url, headers=headers)
		if response.status_code == 200:
			response.html.render(sleep = 5)
			html_content = response.html.html
		else:
			print(f"Request failed with status code: {response.status_code}")
			return
	except Exception as e:
		print(f"Error: {e}")
		return

	soup = BeautifulSoup(html_content, "html.parser")

	temp_data = soup.find("span", attrs={"class": "leading-[88px]"})
	if not temp_data:
		print(f"Could not find temperature information.")
		return
	
	temp_data = temp_data.find("span", attrs={"data-testid": "TemperatureValue"})

	if temp_data and temp_data.text != "--":
		fahrenheit = int((temp_data.text)[:-1])
		celsius = (fahrenheit - 32) * (5.0 / 9.0)
		print(f"The temperature in Kuala Lumpur is {celsius:.1f}°C")
	else:
		print(f"Could not find temperature information.")


if __name__ == "__main__":
	main()