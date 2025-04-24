import logging
import coloredlogs


logger = logging.getLogger("app")

coloredlogs.install(
    level='INFO', 
    logger=logger,
    fmt='%(asctime)s - %(levelname)s - %(message)s',  # Formato del log
    level_styles={'info': {'color': 'green'}, 'error':{'color':'red'}},  # Puedes personalizar los colores aquí
    field_styles={'asctime': {'color': 'yellow'}}
)

