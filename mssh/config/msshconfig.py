import shutil

import yaml
import io
from os.path import expanduser, sep, exists, join
from os import makedirs
import mssh.config

def get_cnf_folder_path():
	return expanduser('~') + sep + '.config' + sep + 'mssh'

def get_cnf_file_path():
	return get_cnf_folder_path() + sep + 'config.yml'

class MsshConfig(object):
	def __init__(self, file_name=None):
		if file_name is None:
			cnf_folder = get_cnf_folder_path()
			try:
				makedirs(cnf_folder)
			except FileExistsError:
				pass
			file_name = get_cnf_file_path()

		if not exists(file_name):
			config_sample = join(mssh.config.__path__[0], 'sample','config_sample.yml')
			shutil.copyfile(config_sample,file_name)

		self._file_name = file_name
		self.environments = None

	def load(self):
		if exists(self._file_name):
			with io.open(self._file_name) as cnf_file:
				self._parse(yaml.full_load(cnf_file))
		else:
			self.environments = CnfValue()
		return self

	def save(self):
		if exists(self._file_name):
			shutil.copy(self._file_name, self._file_name + '.bck')
		with io.open(self._file_name, 'w') as cnf_file:
			yaml.dump(self.__dict__, cnf_file)

	def _parse(self, cnf):
		self.__dict__.update(_dict_2_obj(cnf).__dict__)

	def __str__(self):
		return self.__dict__.__str__()


class CnfValue(object):
	def __str__(self):
		return self.__dict__.__str__()

	def __iter__(self):
		for k, v in self.__dict__.items():
			yield v

	def __getitem__(self, item):
		return self.__dict__[item]

	def __setitem__(self, key, value):
		setattr(self, key, value)

	def __len__(self):
		return len(self.__dict__)

	def __contains__(self, item):
		return self.__dict__.__contains__(item)

	def keys(self):
		return self.__dict__.keys()

	def items(self):
		return self.__dict__.items()

	def add(self, name):
		val = CnfValue()
		setattr(self, name, val)
		return val


def _dict_2_obj(dic):
	result = CnfValue()
	for k, v in dic.items():
		if isinstance(v, dict):
			setattr(result, k, _dict_2_obj(v))
		else:
			setattr(result, k, v)
	return result
