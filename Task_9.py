import os


class FileSystemError(Exception):
    ''' Class for errors in filesystem module '''
    pass


class FSItem(object):
    ''' Common class for OS items OS: Files and Directories '''

    def __init__(self, path):
        self.path = os.path.abspath(path)
        self.item_type = None

    def rename(self, newname):
        if os.path.exists(self.path):
            if os.path.exists(os.path.join(os.path.split(self.path)[0], newname)):
                raise FileSystemError("item with name {0} already exists".format(newname))
            else:
                new_path = os.path.join(os.path.split(self.path)[0], newname)
                os.rename(self.path, new_path)
                self.path = new_path
        else:
            raise FileSystemError("{0} item not exists".format(self.path))

    def create(self):
        if os.path.exists(self.path):
            raise FileSystemError("Item {0} with such path already exists".format(self.path))
        else:
            open(self.path, 'a').close()

    def getname(self):
        return os.path.basename(self.path)

    def isfile(self):
        return os.path.isfile(self.path)

    def isdirectory(self):
        return os.path.isdir(self.path)



class File(FSItem):


    def __init__(self, path):
        self.path = path
        if os.path.isdir(path):
          raise FileSystemError("{0} is a directory".
                                format(os.path.normpath(path)))

    def __len__(self):
        if os.path.exists(self.path):
           return os.path.getsize(self.path)
        else:
            raise FileSystemError("{0} file not exists".format(self.path))

    def getcontent(self):
        if os.path.exists(self.path):
             return open(self.path, 'r').read().splitlines()

        else:
            raise FileSystemError("{0} file not exists".format(self.path))

    def __iter__(self):
        if os.path.exists(self.path):
            return iter(self.getcontent())
        else:
            raise FileSystemError("{0} file not exists".format(self.path))


class Directory(FSItem):
    ''' Class for working with directories '''

    def __init__(self, path):
        self.path = path
        if os.path.isfile(self.path):
            raise FileSystemError("{0} is a file".format(os.path.normpath(path)))


    def items(self):
        if os.path.exists(self.path):
             for name in os.listdir(self.path):
                 new_path = os.path.join(self.path, name)
                 if os.path.isfile(new_path):
                     yield File(new_path)
                 elif os.path.isdir(new_path):
                     yield Directory(new_path)
        else:
            raise FileSystemError("{0} directory not exists".format(self.path))


    def files(self):
        if os.path.exists(self.path):
            yield from filter(lambda x: x.isfile(), self.items())
        else:
            raise FileSystemError("{0} directory not exists".format(self.path))

    def create(self):
        if os.path.exists(self.path):
            raise FileSystemError("{0} already exists".
                                  format(self.path))
        else:
            os.makedirs(self.path)

    def subdirectories(self):
        if os.path.exists(self.path):
            yield from filter(lambda x: x.isdirectory(), self.items())
        else:
            raise FileSystemError("{0} directory not exists".format(self.path))

    def filesrecursive(self):
        if os.path.exists(self.path):
            for file in self.files():
                yield file
            for dir in self.subdirectories():
                yield from directory.filesrecursive()

        else:
            raise FileSystemError("File {0} does not exist".format(self.path))

    def getsubdirectory(self, name):
        return Directory(os.path.join(self.path, name))
