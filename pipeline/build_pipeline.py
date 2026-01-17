from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException


load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info("starting to build Pipeline")


        loader = AnimeDataLoader("data/anime_with_synopsis.csv", "data/anime_updated.csv")
        processed_csv = loader.load_and_process()
        logger.info("Data Loaded and Processed ")


        vector_build = VectorStoreBuilder(processed_csv)
        vector_build.build_and_save_vectorstore()
        logger.info("vector store build succesfully...")
        logger.info("Pipeline built Succesfully ... ")


    except Exception as e:
            logger.error(f" failed to executer the pipeline {str(e)}")
            raise CustomException("Error during pipeline execution" , e)
    
if __name__ == "__main__":
     main()