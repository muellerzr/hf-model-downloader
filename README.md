# hf-model-downloader

## Install

`pip install hf-model-downloader`

`pip install git+https://github.com/muellerzr/hf-model-downloader`

## What is it?

An easy way to download models quickly from huggingface.co with specified backends to specific directories. 

While on its own you can pass in `--local_dir` when using the `huggingface_hub` CLI, many libraries (such as all of the `meta-llama` models) come with two sets
of weights in the repo, `original` and `safetensor` varients *in the same branch*. As a result, this can bloat our downloads when we don't need them.

`hf-downloader` solves this by making it easier to download weights to wherever you want, specifying the weight revision you need (and then will also download the relevant config files, etc)

As this is a wrapper around the `huggingface_hub` CLI, tokens can be passed in via `--token` or by using `huggingface-cli login` (recommended)


### Examples with `meta-llama/Meta-Llama-3.1-8B-Instruct`


**Downloading the `.safetensors` version** (default)
```bash
download-model --backend safetensors meta-llama/Meta-Llama-3.1-8B-Instruct 
```

**Downloading the `.pth` version**
```bash
download-model --backend torch meta-llama/Meta-Llama-3.1-8B-Instruct 
```

**Downloading to a specific directory**
```bash
download-model --local_dir my_llama meta-llama/Meta-Llama-3.1-8B-Instruct 
```

**Using `hf_transfer` for faster downloads**
```bash
download-model --fast meta-llama/Meta-Llama-3.1-8B-Instruct
```



