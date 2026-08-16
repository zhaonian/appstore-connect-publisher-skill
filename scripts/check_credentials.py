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
        print("❌ Missing App Store Connect API Credentials:\n")
        for var in missing:
            print(f"  - {var}")
            
        print("\n" + "="*70)
        print("💡 WHY ARE THESE CREDENTIALS REQUIRED?")
        print("="*70)
        print("Apple's App Store Connect REST API requires a cryptographically signed")
        print("JSON Web Token (JWT) generated from your official Apple Developer .p8 private key.")
        print("This allows the skill to securely push metadata, territory rules, and screenshots")
        print("directly to your App Store Connect account without risking your Apple ID password.")
        
        print("\n" + "="*70)
        print("📖 STEP-BY-STEP: HOW TO GET & STORE YOUR API KEY")
        print("="*70)
        print("1. Log in to App Store Connect: https://appstoreconnect.apple.com/access/api")
        print("2. Navigate to: Users and Access ➔ Integrations tab ➔ App Store Connect API")
        print("3. Click 'Generate API Key' (Name: 'Antigravity Publisher', Access: 'App Manager')")
        print("4. Copy your Key ID (e.g. 'X123456789') and Issuer ID (UUID at top of page)")
        print("5. Click 'Download API Key' to save your file: AuthKey_<KEY_ID>.p8")
        
        print("\n" + "="*70)
        print("📂 WHERE TO STORE THEM ON YOUR MAC")
        print("="*70)
        print("Create the standard directory on your Mac and move your .p8 file there:")
        print("   mkdir -p ~/.appstoreconnect/private_keys")
        print("   mv ~/Downloads/AuthKey_<KEY_ID>.p8 ~/.appstoreconnect/private_keys/\n")
        print("Then export these 3 environment variables in your ~/.zshrc or workspace .env:")
        print("   export APP_STORE_CONNECT_API_KEY_KEY_ID=\"<YOUR_KEY_ID>\"")
        print("   export APP_STORE_CONNECT_API_KEY_ISSUER_ID=\"<YOUR_ISSUER_ID>\"")
        print("   export APP_STORE_CONNECT_API_KEY_KEY_FILE_PATH=\"$HOME/.appstoreconnect/private_keys/AuthKey_<YOUR_KEY_ID>.p8\"")
        print("="*70 + "\n")
        return False

    expanded_path = os.path.expanduser(key_path)
    if not os.path.exists(expanded_path):
        print(f"❌ API Key file not found at path: {key_path} (expanded: {expanded_path})")
        print("Please ensure your AuthKey_<KEY_ID>.p8 file is moved to ~/.appstoreconnect/private_keys/")
        return False

    print("✅ App Store Connect API Key credentials verified!")
    print(f"   Key ID:   {key_id}")
    print(f"   Issuer ID: {issuer_id}")
    print(f"   Key File:  {key_path}")
    return True

if __name__ == "__main__":
    success = check_appstore_credentials()
    sys.exit(0 if success else 1)
