from pathlib import Path

def get_config():
    return{
        "batch_size" :8,
        "num_epochs": 20,
        "lr": 10**-4,
        "seq_len": 350,
        "d_model":512,
        "lang_src": 'en',
        "lang_tgt": 'it',
        "model_folder":"weights",
        "model_filename": "tmodel_",
        "preload":None,
        "tokenizer_file": "tokenizer_{0}.json",
        "experiment_name": "runs/tmodel",
        "datasource": "opus_books"
    }

def get_weights_file_path(config, epoch: str):
    model_folder = f"{config['datasource']}_{config['model_folder']}"
    model_filename = f"{config['model_filename']}{epoch}.pt"
    return str(Path('.') / model_folder / model_filename)




    
    