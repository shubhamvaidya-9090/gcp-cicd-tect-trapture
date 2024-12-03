import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/schedule/v1/international"

headers = {
    "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com",
    "X-RapidAPI-Key": "173db70cf6msh7c7494f4639582bp1c16e1jsnb058a4789aba"  # Replace with your RapidAPI key
}
response = requests.get(url, headers=headers)
print(response.json())
  