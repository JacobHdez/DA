from flask import Blueprint


historical_bp = Blueprint(
    name = 'historical',
    import_name = __name__,
    url_prefix = '/historical'
)

from api.historical import routes
