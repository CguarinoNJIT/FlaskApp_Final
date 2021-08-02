from flask import Blueprint
from flask import   redirect, render_template, url_for

# Blueprint Configuration
contact_bp = Blueprint('contact_bp', __name__,template_folder='contact/templates')

__all__ = ['contact']

@contact_bp.route("/biostats/contact", methods=["GET", "POST"])
def contact():
    """Standard `contact` form."""
    from forms import ContactForm
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(url_for("contact"), form=form,template="form-template")
