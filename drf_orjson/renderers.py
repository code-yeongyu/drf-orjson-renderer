import orjson
from rest_framework.renderers import BaseRenderer
from rest_framework.utils.encoders import JSONEncoder



class ORJSONRenderer(BaseRenderer):
    """
    Renderer which serializes to JSON.
    """
    media_type = 'application/json'
    format = 'json'
    encoder_class = JSONEncoder

    # We don't set a charset because JSON is a binary encoding,
    # that can be encoded as utf-8, utf-16 or utf-32.
    # See: https://www.ietf.org/rfc/rfc4627.txt
    # Also: http://lucumr.pocoo.org/2013/7/19/application-mimetypes-and-encodings/
    charset = None

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Render `data` into JSON, returning a bytestring.
        """
        if data is None:
            return bytes()

        return orjson.dumps(
            data, 
            default=self.encoder_class().encode,
            option=orjson.OPT_SERIALIZE_UUID | \
                orjson.OPT_SERIALIZE_NUMPY | \
                orjson.OPT_OMIT_MICROSECONDS | \
                orjson.OPT_NON_STR_KEYS,
        )
