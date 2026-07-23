import os
import requests

print("🚀 Media Vault engine started")

client_id = os.getenv("TRAKT_CLIENT_ID")
client_secret = os.getenv("TRAKT_CLIENT_SECRET")

if client_id:
    print("✅ Trakt Client ID loaded")
else:
    print("❌ Missing Trakt Client ID")

if client_secret:
    print("✅ Trakt Client Secret loaded")
else:
    print("❌ Missing Trakt Client Secret")


print("🔗 Testing Trakt connection...")

headers = {
    "trakt-api-key": client_id,
    "trakt-api-version": "2"
}

response = requests.get(
    "https://api.trakt.tv/users/settings",
    headers=headers
)

print("Trakt response:", response.status_code)

if response.status_code == 200:
    print("✅ Trakt connection successful")
else:
    print("❌ Trakt connection failed")
    print(response.text)

print("🎬 Media Vault ready")
