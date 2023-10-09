from loguru import logger


def configure_logger():
    logger.remove()
    logger.add(
        "log/app.log",
        rotation="500 MB",
        compression="zip",
        format=(
            "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
            "<level>{level: <8}</level> | "
            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
            "<level>{message}</level>"
        ),
        level="INFO",
    )
