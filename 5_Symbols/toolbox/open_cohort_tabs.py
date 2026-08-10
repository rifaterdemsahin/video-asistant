#!/usr/bin/env python3
"""
Utility script to open all cohort-related web links in the default browser.
Author: Gemini Coder / Antigravity Agent
"""
import webbrowser
import sys
import time

COHORT_LINKS = [
    ("Cohort Script", "https://www.canva.com/design/DAHR6cycvQg/R59DcxBa5olAryxm8IH4nA/edit?ui=e30"),
    ("Cohort Summary", "https://docs.google.com/document/d/1KGMeo7ITeu5TGjH3nL59RrsLJRXcWYxFmGsxHRKMezg/edit?tab=t.7bf97qu78f2p"),
    ("Cohort Link to Watch", "https://canva.link/qx6bnd3gl29rndl"),
    ("Tactics", "https://canva.link/he50e3a03vqa6ly"),
    ("Google Flow", "https://labs.google/fx/tools/flow/project/6f72686d-76e5-4845-b65e-ff45058c82ce"),
    ("Gaps", "https://canva.link/fx8uwgad7k5xbnb"),
    ("Index Page", "https://www.canva.com/design/DAHRZe5KBoA/OJU0sL318CozUaTBpkdT2g/edit")
]

def main():
    print("🚀 Initializing cohort link opener...")
    print(f"Total links to open: {len(COHORT_LINKS)}\n")
    
    for i, (name, url) in enumerate(COHORT_LINKS, 1):
        print(f"[{i}/{len(COHORT_LINKS)}] Opening {name}...")
        print(f"    URL: {url}")
        webbrowser.open(url)
        # Small delay to allow the browser application to handle the previous request
        time.sleep(0.5)
        
    print("\n✅ All links successfully requested in the default browser.")

if __name__ == "__main__":
    main()
