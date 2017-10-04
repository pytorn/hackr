import base64
import tempfile
import os

def b64_encode(source_filepath, dest_filepath=None):
	""" base64_encode source file to destination

	If dest_filepath not provided, will save to a temp file and returns path """
	with open(source_filepath, 'rb') as f:
		data = f.read()

	if dest_filepath is None:
		fd, filepath = tempfile.mkstemp()
		f = os.fdopen(fd, 'wb')
		f.write(base64.b64encode(data))
		f.close()
		return filepath

	with open(dest_filepath, 'wb') as f:
		f.write(base64.b64encode(data))
	return dest_filepath

def b64_decode(source_filepath, dest_filepath=None):
	""" base64 decode source file to destination

	If dest_filepath not provided, will save to a tmp file and return path """
	with open(source_filepath, 'rb') as f:
		data = f.read()

	if dest_filepath is None:
		fd, filepath = tempfile.mkstemp()
		f = os.fdopen(fd, 'wb')
		f.write(base64.b64decode(data))
		f.close()
		return filepath

	with open(dest_filepath, 'wb') as f:
		f.write(base64.b64decode(data))
	return dest_filepath