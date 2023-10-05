import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name='ML-PROJECT'

list_of_files = [
    "github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "Dockerfile",
]

for file in list_of_files:
    file_path = Path(file)
    filedir, filename = os.path.split(file_path)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created {filedir} for the file {filename}") 

    if(not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):

        with open(file_path, "w") as f:
            pass
            logging.info(f"Created empty {file_path} file")

    else:
        logging.info(f"File {file_path} already exists")        
            






