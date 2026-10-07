#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

import pytesseract
from PIL import Image
from transformers import pipeline


summarizer_model = None


def get_summarizer():
    global summarizer_model
    if summarizer_model is None:
        print("Loading local summarization model...")
        summarizer_model = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)
    return summarizer_model


def summarize_text(text: str) -> str:
    text = text.strip()
    if not text:
        raise ValueError("Text is empty.")

    if len(text.split()) < 10:
        return "Text is too short to summarize meaningfully."

    model = get_summarizer()
    result = model(text, max_length=120, min_length=30, do_sample=False)
    return result[0]["summary_text"]


def summarize_image(image_path: str) -> str:
    image = Image.open(image_path)
    if image.mode in ("RGBA", "LA", "P"):
        image = image.convert("RGB")

    extracted = pytesseract.image_to_string(image).strip()
    if not extracted:
        raise ValueError("No text was detected in the image.")

    return summarize_text(extracted)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["text", "image"], required=True)
    parser.add_argument("--input", required=True)
    args = parser.parse_args()

    try:
        if args.mode == "text":
            print(summarize_text(args.input))
        else:
            p = Path(args.input)
            if not p.exists():
                raise FileNotFoundError(args.input)
            print(summarize_image(str(p)))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        raise SystemExit(1)
