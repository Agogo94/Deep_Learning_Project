from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"


try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Base Model preparation"

try:
    logger.info(f"****************")
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training"

try:
    logger.info(f"****************")
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation"

try:
    logger.info(f"****************")
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e