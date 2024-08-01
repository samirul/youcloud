import json
from rest_framework import renderers

class UserErrorRender(renderers.JSONRenderer):
    charset = 'utf-8'
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        if 'ErrorDetail' in str(data):
            response = json.dumps({'Errors.':data})
        else:
            response = json.dumps(data)
        return response