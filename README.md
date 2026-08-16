# 🚀 appstore-connect-publisher-skill

> **An Agent / Claude Skill to perform ASO keyword research, draft App Store metadata, set country availability rules (e.g. exclude France), verify API credentials, and deploy to Apple App Store Connect via Fastlane.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform: macOS](https://img.shields.io/badge/Platform-macOS-lightgrey.svg)]()
[![Fastlane: Deliver](https://img.shields.io/badge/Fastlane-Deliver-orange.svg)](https://docs.fastlane.tools/actions/deliver/)

---

## 🌟 Features

- 🔍 **AI-Driven ASO Keyword Research**: Scans your iOS codebase, models, UI, and README to craft 100-character non-redundant keywords, titles, and subtitles.
- 🌍 **Territory Rules**: Easily exclude specific countries (e.g. France `FR`) or set custom distribution rules.
- 🔐 **Pre-Flight Security Check**: Validates your Apple App Store Connect API Key (`.p8` key + Issuer ID + Key ID) before uploading.
- 🖼️ **Screenshot Sync**: Automatically picks up formatted ASO screenshots (1242 × 2688 px) and syncs them to App Store Connect display slots.
- ⚡ **1-Click Fastlane Integration**: Generates local `./fastlane/metadata/` and pushes directly to App Store Connect.

---

## 📁 Repository Structure

```
claude-skill-appstore-publisher/
├── SKILL.md                          # Main Agent Skill instructions & phased workflow
├── README.md                         # Documentation & Quick Start
├── scripts/
│   ├── aso_keyword_researcher.py     # Codebase scanner & ASO keyword generator
│   └── check_credentials.py          # App Store Connect API Key validator
└── references/
    └── appstore_connect_api_guide.md # Setup guide for generating .p8 API keys
```

---

## 🚀 Quick Start & Installation

### Option A: Install in Workspace
Clone or copy this repository into `.agents/skills/appstore-publisher` inside your project directory:
```bash
mkdir -p .agents/skills/appstore-publisher
```

### Option B: Install Globally on your Mac
```bash
mkdir -p ~/.gemini/config/skills/appstore-publisher
```

---

## 🔐 Credentials Setup

1. Generate an API Key in **App Store Connect ➔ Users and Access ➔ Integrations**.
2. Save your `.p8` key file locally to `~/.appstoreconnect/private_keys/AuthKey_<KEY_ID>.p8`.
3. Add the following to your `~/.zshrc` or workspace `.env`:
```bash
export APP_STORE_CONNECT_API_KEY_KEY_ID="YOUR_KEY_ID"
export APP_STORE_CONNECT_API_KEY_ISSUER_ID="YOUR_ISSUER_ID"
export APP_STORE_CONNECT_API_KEY_KEY_FILE_PATH="$HOME/.appstoreconnect/private_keys/AuthKey_YOUR_KEY_ID.p8"
```

---

## 📜 License
MIT License.
