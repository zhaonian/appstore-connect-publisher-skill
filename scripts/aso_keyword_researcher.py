#!/usr/bin/env python3
import sys

def validate_aso_keywords(keywords_str, title_str="", subtitle_str=""):
    """
    Validates App Store Connect keyword string against Apple guidelines:
    - Max 100 characters total length
    - No redundant duplicate words
    - No words already present in Title or Subtitle
    """
    keywords_raw = [k.strip().lower() for k in keywords_str.split(",") if k.strip()]
    title_words = set(w.lower() for w in title_str.replace("-", " ").split() if len(w) > 2)
    subtitle_words = set(w.lower() for w in subtitle_str.replace("-", " ").split() if len(w) > 2)

    unique_keywords = []
    seen = set()
    warnings = []

    for kw in keywords_raw:
        if kw in seen:
            warnings.append(f"Duplicate keyword removed: '{kw}'")
            continue
        if kw in title_words:
            warnings.append(f"Redundant keyword in Title removed: '{kw}'")
            continue
        if kw in subtitle_words:
            warnings.append(f"Redundant keyword in Subtitle removed: '{kw}'")
            continue
        seen.add(kw)
        unique_keywords.append(kw)

    clean_keyword_str = ",".join(unique_keywords)
    char_count = len(clean_keyword_str)

    print(f"📊 ASO Keyword Analysis:")
    print(f"   Original: '{keywords_str}' ({len(keywords_str)} chars)")
    print(f"   Cleaned:  '{clean_keyword_str}' ({char_count}/100 chars)")

    if warnings:
        print("\n⚠️ ASO Optimizations Applied:")
        for w in warnings:
            print(f"   - {w}")

    if char_count > 100:
        print(f"\n❌ Error: Keywords exceed Apple 100-character limit by {char_count - 100} chars!")
        return False
    else:
        print(f"\n✅ Valid ASO Keyword Set! ({100 - char_count} chars remaining for optimization)")
        return True

if __name__ == "__main__":
    test_kw = "offline,p2p,multiplayer,local,party,gomoku,tictactoe,games,no,wifi,bluetooth,nearby,card,board"
    test_title = "OMG - Offline Multipeer Games"
    test_subtitle = "Play Local Games Without Wi-Fi"
    validate_aso_keywords(test_kw, test_title, test_subtitle)
