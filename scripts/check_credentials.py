#!/usr/bin/env python3
import os
import sys

def check_appstore_credentials():
    key_id = os.environ.get("APP_STORE_CONNECT_API_KEY_KEY_ID")
    issuer_id = os.environ.get("APP_STORE_CONNECT_API_KEY_ISSUER_ID")
    key_path = os.environ.get("APP_STORE_CONNECT_API_KEY_KEY_FILE_PATH")

    missing = []
    if not key_id:
        missing.append("APP_STORE_CONNECT_API_KEY_KEY_ID")
    if not issuer_id:
        missing.append("APP_STORE_CONNECT_API_KEY_ISSUER_ID")
    if not key_path:
        missing.append("APP_STORE_CONNECT_API_KEY_KEY_FILE_PATH")

    if missing:
        print("❌ Missing App Store Connect API Credentials:")
        for var in missing:
            print(f"  - {var}")
        print("\n📋 Setup Instructions:")
        print("1. Go to App Store Connect ➔ Users and Access ➔ Integrations")
        print("2. Download your AuthKey_<KEY_ID>.p8 file and move to ~/.appstoreconnect/private_keys/")
        print("3. Export key_id, issuer_id, and key_file_path in your environment.")
        return False

    if not os.path.exists(os.path.expanduser(key_path)):
        print(f"❌ API Key file not found at path: {key_path}")
        return False

    print("✅ App Store Connect API Key credentials verified!")
    print(f"   Key ID: {key_id}")
    print(f"   Issuer ID: {issuer_id}")
    print(f"   Key File: {key_path}")
    return True

if __name__ == "__main__":
    success = check_appstore_credentials()
    sys.exit(0 if success else 1)
