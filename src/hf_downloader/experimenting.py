from huggingface_hub import HfApi
from huggingface_hub.utils import filter_repo_objects
from huggingface_hub.file_download import repo_folder_name

from core_api import MODEL_TYPE_TO_EXTENSION, ALLOW_PATTERNS


api = HfApi()
repo_info = api.repo_info(repo_id="meta-llama/Meta-Llama-3.1-8B-Instruct", repo_type="model")


filtered_repo_files = list(
    filter_repo_objects(
        items=[f.rfilename for f in repo_info.siblings],
        allow_patterns=ALLOW_PATTERNS + MODEL_TYPE_TO_EXTENSION["safetensors"],
    )
)

print(filtered_repo_files)

print(repo_folder_name(repo_id=repo_info.id, repo_type="model"))