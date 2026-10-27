"""Download the project datasets without loading CLIP or extracting features."""

from pathlib import Path

from datasets import load_dataset
from huggingface_hub import snapshot_download


def main() -> None:
    root = Path(__file__).resolve().parent
    print("Downloading ImageNet validation only (about 703 MB)...", flush=True)
    snapshot_download(
        repo_id="benjamin-paine/imagenet-1k-256x256",
        repo_type="dataset",
        revision="1bd0400450249a7fe90c0aece37d0d03e7ea956a",
        allow_patterns=[
            "data/validation-00000-of-00002.parquet",
            "data/validation-00001-of-00002.parquet",
        ],
        local_dir=root / "data" / "imagenet_validation",
    )
    print("ImageNet validation files ready.", flush=True)

    print("Downloading Flickr8k (about 1.1 GB) and preparing its local cache...", flush=True)
    flickr = load_dataset("Naveengo/flickr8k", split="train")
    print(f"Flickr8k ready: {len(flickr):,} image-caption pairs.", flush=True)
    print("Done. No model weights, feature extraction or experiments were run.", flush=True)


if __name__ == "__main__":
    main()
