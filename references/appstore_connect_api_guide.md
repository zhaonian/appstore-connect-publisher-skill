# 📖 App Store Connect API Setup Guide

This guide explains how to generate an official Apple App Store Connect API Key to enable 1-click automated metadata, territory distribution, and screenshot deployment.

---

## Step 1: Generate API Key in Apple Developer Portal
1. Log in to [App Store Connect](https://appstoreconnect.apple.com/).
2. Navigate to **Users and Access** ➔ Select the **Integrations** tab.
3. Under **App Store Connect API**, click **Generate API Key** (or the `+` button).
4. Enter Name: `Antigravity Publisher`
5. Select Access Role: **App Manager** or **Admin**.
6. Click **Generate**.

---

## Step 2: Download & Store Private Key File (.p8)
1. Next to your newly created API Key, copy:
   - **Key ID** (10-character string e.g. `X123456789`)
   - **Issuer ID** (UUID at the top of the page e.g. `69a67000-8888-4444-9999-111122223333`)
2. Click **Download API Key** to download `AuthKey_<KEY_ID>.p8`.
   > **Note**: Apple allows downloading the `.p8` file only once. Store it securely.

---

## Step 3: Save to Standard Local Mac Directory
Create the standard directory on your Mac and move your key:
```bash
mkdir -p ~/.appstoreconnect/private_keys
mv ~/Downloads/AuthKey_X123456789.p8 ~/.appstoreconnect/private_keys/
```

---

## Step 4: Export Environment Variables
Add these 3 lines to your `~/.zshrc` (or workspace `.env` file, which is added to `.gitignore`):

```bash
export APP_STORE_CONNECT_API_KEY_KEY_ID="X123456789"
export APP_STORE_CONNECT_API_KEY_ISSUER_ID="69a67000-8888-4444-9999-111122223333"
export APP_STORE_CONNECT_API_KEY_KEY_FILE_PATH="$HOME/.appstoreconnect/private_keys/AuthKey_X123456789.p8"
```
