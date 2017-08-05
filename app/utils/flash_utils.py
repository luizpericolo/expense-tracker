from flask import flash


def flash_form_errors(form):
    for field, field_errors in form.errors.items():
        flash('{}: {}'.format(field, ','.join(field_errors)), category='danger')