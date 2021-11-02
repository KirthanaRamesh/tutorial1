from rest_framework.renderers import BaseRenderer
from rest_framework.utils import json


class ApiRenderer(BaseRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
         response_dict = {
             'id':'',     
         }
         if data.get('id'):
             response_dict['data'] = data.get('data')
         data = response_dict
         return json.dumps(data)