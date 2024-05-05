import argparse
import tempfile
from pathlib import Path

from transformers import AutoModelForSequenceClassification, AutoTokenizer

if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument("--model_name", type=str, required=True)
    parse.add_argument("--output_dir", type=str, default="/opt/app/models")
    args = parse.parse_args()

    output_dir = Path(args.output_dir) / args.model_name
    output_dir.mkdir(parents=True, exist_ok=True)

    # Use a temp dir to avoid downloading the model to cache and then saving it to the output dir
    with tempfile.TemporaryDirectory() as temp_dir:
        model = AutoModelForSequenceClassification.from_pretrained(args.model_name, cache_dir=temp_dir)
        tokenizer = AutoTokenizer.from_pretrained(args.model_name, cache_dir=temp_dir)
        model.save_pretrained(output_dir)
        tokenizer.save_pretrained(output_dir)

    print(f"Model and tokenizer saved to {args.output_dir}")
