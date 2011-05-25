class Plugin:
    def __init__(self, iface, libraries):
        self.iface = iface
        self.libraries = libraries
    def initGui(self):
        pass
    def unload(self):
        pass

class Library:
    def __init__(self, name, description = None, modules = None):
        self.name = name
        self.description = description
        self.modules = modules
        print "Loading library " + name
    def name(self):
        return self.name
    def description(self):
        return self.description
    def modules(self):
        return self.modules

""" Case insensitive strings for tag usage.
"""
class Tag(str):
    """ Case insensitive string comparison ignoring extra whitespace
        at the beggining or end of the tag.
        
        >>> Tag('ArArAt') == Tag('ararat')
        True
        >>> Tag('Kenya') == Tag('Kilimanjaro')
        False
        >>> Tag('ACONCAGUA') != Tag(' AcOnCaGuA ')
        False
    """
    def __cmp__(self, other):
        return self.strip().upper() == other.strip().upper()

""" Default list of tags.
    Not binding.
"""
standardTags = [Tag(s) for s in ["2D", "3D", "analysis",
            "classification", "database", "display", "export", "filter",
            "imagery", "import", "interactive", "paint", "photo",
            "postscript", "projection", "raster", "simulation",
            "statistics", "vector"]]


class Module:
    def __init__(self, name,
        description = None, tags = None, parameters = None):
            self.name = name
            self.description = description
            self.tags = tags
            self.parameters = parameters
            print "Loading module " + name
    def name(self):
        return self.name
    def description(self):
        return self.description
    def tags(self):
        if self.tags:
            return tags
        else:
            return name.split()
    def parameters(self):
        return self.parameters
