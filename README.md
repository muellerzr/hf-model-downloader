# hf-downloader

## Install

`pip install hf-downloader`

`pip install git+https://github.com/muellerzr/hf-downloader`

## What is it?

An easy way to download models quickly from huggingface.co with specified backends to specific directories. 

While on its own you can pass in `--local_dir` when using the `huggingface_hub` CLI, many libraries (such as all of the `meta-llama` models) come with two sets
of weights in the repo, `original` and `safetensor` varients *in the same branch*. As a result, this can bloat our downloads when we don't need them.

`hf-downloader` solves this by making it easier to download weights to wherever you want, specifying the weight revision you need (and then will also download the relevant config files, etc)

As this is a wrapper around the `huggingface_hub` CLI, tokens can be passed in via `--token` or by using `huggingface-cli login` (recommended)


### Examples with `meta-llama/Meta-Llama-3.1-8B-Instruct`


**Downloading the `.safetensors` version** (default)
```bash
hf-downloader --backend safetensors meta-llama/Meta-Llama-3.1-8B-Instruct 
```

**Downloading the `.pth` version**
```bash
hf-downloader --backend torch meta-llama/Meta-Llama-3.1-8B-Instruct 
```

**Downloading to a specific directory**
```bash
hf-downloader --local-dir my_llama meta-llama/Meta-Llama-3.1-8B-Instruct 
```

**Using `hf_transfer` for faster downloads**
```bash
hf-downloader --fast meta-llama/Meta-Llama-3.1-8B-Instruct
```