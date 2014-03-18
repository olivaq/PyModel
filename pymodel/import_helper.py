from os.path import exists
import imp


def load_module(mname):
    try:
        return __import__(mname)
    except ImportError:
        if mname.endswith(".py"):
            pyfile, mname = mname, mname[:-3]
        else:
            pyfile = mname + ".py"
        if exists(pyfile):
            return imp.load_source(mname, pyfile)
        raise
