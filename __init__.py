from os import (path, makedirs)

class Doc:
	def __init__(self, file_path):
		self.file_path = file_path
		self.encoding = 'utf-8'

	def isfile(self):
		return path.isfile(self.file_path)

	def file_buffer(self, file_name, open_type):
		return open(file_name, open_type, encoding=self.encoding)

	def doc_buffer(self, open_type):
		return self.file_buffer(self.file_path, open_type)

class Document(Doc):
	def read(self):
		_read = None
		with self.doc_buffer('r') as r:
			_read = r.read()
		return _read

	def write(self, data):
		with self.doc_buffer('w')  as w:
			w.write(data)

class BaseRelDir(object):
	def __init__(self, abs_file_path):
		self.dirname = path.dirname(path.abspath(abs_file_path))

	def join(self, *args):
		return path.join(self.dirname, *args)

	def doc(self, name):
		name = self.join(name)
		return Document(name)


class RelDir(BaseRelDir):
	def __init__(self, initial_dir, rel_dir='.'):
		BaseRelDir.__init__(self, initial_dir)
		self.dirname = self.join(rel_dir)

		if not path.isdir(self.dirname):
			print('Directory does not exist! resolving directory error')
			makedirs(self.dirname)