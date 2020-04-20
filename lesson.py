import logging


logger = logging.getLogger(__name__)


logger.error('Api call is failed')

logger.error({
    'action': 'cteate',
    'status': 'fail',
    'message': 'Api call is failed'
})