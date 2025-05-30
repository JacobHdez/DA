from api.historical import historical_bp


@historical_bp.route('/', methods=('GET',))
def index():
    return 'Hello, World!!! from Historical'
