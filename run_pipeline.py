#!/usr/bin/env python3
"""AI Website Redesign Pipeline - Main Orchestrator"""
import sys, os, json, subprocess
from datetime import datetime

def run_step(step_num, script, *args):
    print(f"\n{'='*60}\n🚀 RUNNING STEP {step_num}\n{'='*60}\n")
    cmd = [sys.executable, script] + list(args)
    result = subprocess.run(cmd)
    return result.returncode == 0

def main():
    query = sys.argv[1] if len(sys.argv) > 1 else "nail salons"
    location = sys.argv[2] if len(sys.argv) > 2 else "Sydney, Australia"
    print(f"🤖 AI WEBSITE REDESIGN PIPELINE\n📅 {datetime.now()}\n🔍 {query} in {location}")
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    steps = [
        (1, "step1_google_maps_scraper.py", [query, location]),
        (2, "step2_website_qualifier.py", ["businesses.json"]),
        (3, "step3_website_redesigner.py", ["qualified.json"]),
        (4, "step4_website_deployer.py", ["redesigned/"])
    ]

    for step_num, script, args in steps:
        if not run_step(step_num, script, *args):
            print(f"\n❌ Step {step_num} failed. Aborting.")
            return 1

    print("\n🎉 PIPELINE COMPLETE!")
    return 0

if __name__ == "__main__":
    sys.exit(main())
