import logging
from .base import *

log = logging.getLogger(__name__)

class Component(BaseComponent):

    default_name = 'Résumé des découvertes'
    htmlTemplate = 'componentTemplates/FindingsTable.html'
    iconType = 'fas fa-th-list'
    iconColor = 'var(--orange)'