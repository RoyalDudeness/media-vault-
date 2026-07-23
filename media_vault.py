import requests

headers = {
    "trakt-api-key": client_id,
    "trakt-api-version": "2"
}

response = requests.get(
    "https://api.trakt.tv/users/me",
    headers=headers
)

print(response.status_code)
print(response.text)
