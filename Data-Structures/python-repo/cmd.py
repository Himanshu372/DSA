from json import JSONDecoder


class FileItem:
    def __init__(self, fname):
        self.fname = fname
    def __repr__(self):
        return self.fname


def from_json(json_object):
    if 'fname' in json_object:
        return FileItem(json_object['fname'])


if __name__ == "__main__":
    f = JSONDecoder(object_hook=from_json)
    obj = f.decode('{"fname": "/foo/bar"}')
    print(obj)
