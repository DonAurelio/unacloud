# -*- encoding: utf-8 -*-


import yaml


class DeploymentManifest(object):
    """
    Resource deployent
    Action deployment
    """
   
    @staticmethod
    def _load_from_text(text):
        data = yaml.load(text)
        return data

    @staticmethod
    def _load_from_file(file_path):
        with open(file_path,'r') as file:
            data = yaml.load(file)
            return data

    def __init__(self,raw_text=None,file_path=None, data=None):
        if raw_text:
            self._data = self._load_from_text(raw_text)
            self._file_path = ''
        elif file_path:
            self._data = self._load_from_file(file_path)
            self._file_path = file_path
        elif data:
            self._data = data
            self._file_path = ''
        else:
            self._data = None

    @property
    def file_path(self):
        return self._file_path

    @property
    def is_resource_deployment(self):
        return 'specs' in self._data

    @property
    def is_action_deployment(self):
        return 'action' in self._data

    @property
    def action_id(self):
        return self._data.get('action_id')

    @property
    def data(self):
        return self._data

    @property
    def action(self):
        return self._data.get('action')

    @property
    def provider(self):
        return self._data.get('provider')    

    @property
    def name(self):
        return str(self._data.get('name'))

    @property
    def cpus(self):
        specs = self._data.get('specs')
        return specs.get('cpus', 1)

    @property
    def memory(self):
        specs = self._data.get('specs')
        return specs.get('memory', 512)

    @property
    def ports(self):
        specs = self._data.get('ports')
        return specs.get('ports', None)
    