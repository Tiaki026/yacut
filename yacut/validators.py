from wtforms.validators import ValidationError
from settings import LIMIT_OR_ENTER_ERROR
from .utils import char_pool


def validate_char_pool(form, field):
    """Валидатор для проверки символов в custom_id."""
    if not char_pool(field.data):
        raise ValidationError(LIMIT_OR_ENTER_ERROR)
