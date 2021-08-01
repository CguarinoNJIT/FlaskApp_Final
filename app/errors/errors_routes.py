
from flask import Blueprint
from flask import   Response,  render_template

# Blueprint Configuration
errors_bp = Blueprint('errors_bp', __name__,template_folder='errors/templates')

__all__ = ['not_found','bad_request','server_error']

#Error Handling
@errors_bp.errorhandler(404)
def not_found():
    """Page not found."""
    return Response(render_template("404Error.html"), 404)

@errors_bp.errorhandler(400)
def bad_request():
    """Bad request."""
    return Response(render_template("400Error.html"), 400)


@errors_bp.errorhandler(500)
def server_error():
    """Internal server error."""
    return Response(render_template("500Error.html"), 500)