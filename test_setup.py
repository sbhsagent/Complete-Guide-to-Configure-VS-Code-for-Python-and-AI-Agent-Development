import sys
import os
from dotenv import load_dotenv


def check_package(package_name):
    try:
        __import__(package_name)
        print(f"✓ {package_name} is installed.")
    except ImportError:
        print(f"✗ {package_name} is NOT installed.")


print("🔍 Verifying AI Development Setup...")
# Check Python Version
print(f"✓ Using Python {sys.version}")
# Check Packages
check_package("openai")
check_package("langchain")
check_package("torch")
check_package("dotenv")
# Check API Keys
load_dotenv()
if os.getenv("OPENAI_API_KEY"):
    print("✓ OPENAI_API_KEY found in .env file.")
else:
    print("✗ OPENAI_API_KEY is missing from .env file.")
print("\n🎉 Verification complete.")
