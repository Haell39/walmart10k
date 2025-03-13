import kaggle

kaggle.api.authenticate()

kaggle.api.dataset_download_files('najir0123/walmart-10k-sales-datasets', path='.', unzip=True)