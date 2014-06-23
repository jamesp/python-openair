import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

from .openair import parseFile
