import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

headers = {
	"x-rapidapi-key": "173db70cf6msh7c7494f4639582bp1c16e1jsnb058a4789aba",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}
response = requests.get(url, headers=headers)
print(response.json())
  