
import os

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

print("Ready for Trakt connection")
