from ..facades import Loader
from ..exceptions import NotFoundException


def find_or_fail(model, pk):
    """
    Find model instance or raise 404 error.

    model: instance or string
    pk: model primary key
    """
    if isinstance(model, str):
        model_name = model.split(".")[-1]
        model_class = Loader.get_object(model, model_name)
    else:
        model_class = model

    record = model_class.find(pk)
    if not record:
        raise NotFoundException()

    return record
