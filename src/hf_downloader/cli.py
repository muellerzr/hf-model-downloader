import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Download models from HuggingFace Hub")
    parser.add_argument("repo_id", type=str, help="The repo id of the model to download")
    parser.add_argument("--token", type=str, help="The token to use for the Hugging Face Hub API", default=None)
    parser.add_argument("--local_dir", type=str, help="The local directory to download the model to", default=None)
    parser.add_argument("--backend", type=str, choices=["safetensors", "torch"], default="safetensors", help="The backend to use for the model")
    parser.add_argument("--fast", action="store_true", help="Enable fast download via HF_TRANSFER")

    args = parser.parse_args()

    if args.fast:
        os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
    # Since we may enable fast download, we need to import the API after setting the env
    from hf_downloader.core_api import download_model
    
    download_model(
        repo_id=args.repo_id,
        token=args.token,
        local_dir=args.local_dir,
        backend=args.backend
    )

if __name__ == "__main__":
    main()
