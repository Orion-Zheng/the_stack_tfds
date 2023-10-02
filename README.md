Please replace `$SCRATCH` in all scripts with the actual path to `the_stack_tfds` on your machine  
Dependencies: git-lfs (to git clone large files in hf datasets), tfds-nightly, zstandard, fastparquet  

# 1. Download the-stack-dedup  
Run the `download_scripts\get_the_stack_dedup.sh`. the-stack-dedup repo has a Terms of Use so you cannot clone it directly. Please agree with the repo's Terms of Use first on huggingface and enter your huggingface username and access token in git clone command like this.  
```git clone https://YOUR_HF_USERNAME:YOUR_HF_ACCESS_TOKEN@huggingface.co/datasets/bigcode/the-stack-dedup```  

# 2. Generate TFDS of the-stack-dedup  
Run `build_scripts/generate_the_stack_dedup.sh` to generate TFDS in the `the_stack_data` directory.  
Among the script:  
```
--manual_dir: The source directory for storing raw data.
--data_dir: The target directory for storing the generated TFDS.
```

# 3. Upload the TFDS to Google Cloud  
Install gsutil and sign in your Google Account, run `the_stack_data/upload.sh` to upload TFDS to your google storage bucket.  
[ref](https://cloud.google.com/storage/docs/gsutil_install#linux)  
