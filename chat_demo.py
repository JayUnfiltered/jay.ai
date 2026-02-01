#!/usr/bin/env python3
"""
Simple chat demo for Jay's AI chatbot.
"""

import argparse
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="Jay AI Chat Demo")
    parser.add_argument("--model", default=os.getenv("BASE_MODEL", "meta-llama/Llama-2-7b-hf"),
                        help="HuggingFace model ID")
    args = parser.parse_args()
    
    print(f"Loading model: {args.model}")
    print("Chat demo - not yet implemented")
    # TODO: Implement chat functionality

if __name__ == "__main__":
    main()
