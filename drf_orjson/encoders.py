from collections import OrderedDict

from rest_framework.utils import encoders


class JSONEncoder(encoders.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, OrderedDict):
            return dict(obj)
        return super().default(obj)
