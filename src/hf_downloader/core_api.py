"""
Core API for downloading models from HuggingFace
"""
import logging
from hf_downloader.utils import get_logger

from huggingface_hub import snapshot_download
from huggingface_hub.file_download import repo_folder_name
from huggingface_hub.constants import HF_HUB_CACHE
from typing import Literal
from pathlib import Path
import sys

logger = get_logger(__file__)


# Snapshot download takes in ignore patterns
MODEL_TYPE_TO_EXTENSION = {
    "torch": ["*.bin", "*.pt", "*.pth", "*.pickle", "*.pkl", "*.pickle", "original/*"],
    "safetensors": ["*.safetensors"],
}

ALLOW_PATTERNS = ["*.json"]

def download_model(
    repo_id: str,
    token: str = None,
    local_dir: Path = None,
    backend: Literal["safetensors", "torch"] = "safetensors",
):
    """
    Download a model from the Hugging Face Hub and grabbing only the files
    related to the framework you are using

    Args:
        repo_id (str): 
            The repo id of the model to download (such as "meta-llama/Meta-Llama-3.1-8B-Instruct")
        token (str): 
            The token to use for the Hugging Face Hub API (if not using `huggingface-cli login`)
        local_dir (Path): 
            The local directory to download the model to. If not provided, the model will be downloaded to the 
            default cache directory and path `huggingface_hub` uses.
        backend (Literal["safetensors", "torch"]): 
            The backend to use for the model, either "safetensors" or "torch"
    """
    if local_dir is None:
        local_dir = Path(HF_HUB_CACHE) / repo_folder_name(repo_id=repo_id, repo_type="model")
    file_patterns = MODEL_TYPE_TO_EXTENSION[backend] + ALLOW_PATTERNS
    logger.info(f"Downloading {repo_id} to {local_dir} with allowed patterns: {file_patterns}")
    snapshot_download(
        repo_id=repo_id,
        repo_type="model",
        token=token,
        local_dir=local_dir,
        allow_patterns=file_patterns
    )