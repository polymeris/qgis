# -*- coding: utf-8 -*-

#	QGIS Processing Framework
#
#	__init__.py (C) Camilo Polymeris
#	
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
# 
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#       
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#   MA 02110-1301, USA.

import moduleinstance
from itertools import chain
from traits.api import HasTraits, Instance, HTML

class Tag(str):
    """ Case insensitive strings for tag usage. """
    def __cmp__(self, other):
        """ Case insensitive string comparison ignoring extra whitespace
        at the beggining or end of the tag.
        
        >>> Tag('ArArAt') == Tag('ararat')
        True
        >>> Tag('Kenya') == Tag('Kilimanjaro')
        False
        >>> Tag('ACONCAGUA') != Tag(' AcOnCaGuA ')
        False
        """
        return self.strip().upper() == other.strip().upper()

class Framework:
    def __init__(self):
        self._moduleProviders = set()
    def registerModuleProvider(self, moduleprovider):
        """ Register module providers with the framework.
        moduleprovider must implement the modules() method,
        which returns a list of modules.
        """
        self._moduleProviders.add(moduleprovider)
    def modules(self):
        """ Returns complete list of registered modules."""
        moduleList = [set(mp.modules()) for mp in self._moduleProviders]
        return set(chain(*moduleList))
    def modulesByTag(self, tag):
        """ Returns modules that match the tag specified."""
        tag = Tag(tag)
        return filter(lambda m: tag in m.tags(), self.modules())
    def tagFrequency(self):
        """ Return a dict of tag => relative tag frequency.
        Relative tag ranges from 0.0 to 1.0, the latter identifing tags
        that every module has.
        """
        tags = dict()
        # perhaps standard tags could be given a bump?
        modules = self.modules()
        for m in modules:
            for t in m.tags():
                if t in tags: tags[t] += 1.0
                else: tags[t] = 1.0
        # divide by number of modules to get a list of
        # relative frequencies.
        tags = map(lambda (k, v): (k, v / len(modules)), tags.items())
        return dict(tags)
    def usedTags(self):
        """ Tags used."""
        return set(self.tagFrequency().keys())
    def representativeTags(self):
        """ Returns list of tags that aren't too frequent or to infrequent
        to be representative.
        That is, cut tags that only apply to 1% of the modules or to
        more than 25%.
        """
        criterion = lambda (_, v): v > 0.02 and v < 0.25
        tags = self.tagFrequency().items()
        tags, _ = zip(*filter(criterion, tags))
        return tags
        
    """ Default set of tags. Not binding. """
    standardTags = set([Tag(s) for s in ["2D", "3D", "analysis",
        "classification", "database", "display", "export", "filter",
        "imagery", "import", "interactive", "paint", "photo",
        "postscript", "projection", "raster", "simulation",
        "statistics", "vector"]])

""" Singleton framework """
framework = Framework()

class Module:
    """ A processing module. """
    def __init__(self, name,
        description = "", tags = None):
            self._name = name
            self._description = description
            self._tags = tags
    def name(self):
        return self._name
    def description(self):
        """ The modules description string.
        If no description is provided on construction, returns an empty
        string.
        """
        return self._description
    def instance(self):
        return ModuleInstance(self)
    def tags(self):
        """ The modules tags.
        By default, this method searches for 'standard tags' in the
        module's name & description. Dumb method, so reimplement if
        possible.
        To customize this, either indicate tags on construction or
        override this method.
        """
        if self._tags:
            return set(self._tags)
        else:
            text = (self.name() + " " + self.description()).lower()
            tags = set([Tag(s.strip(" .-_()/,")) for s in text.split()])
            return Framework.standardTags & tags

class ModuleInstance(HasTraits):
    def __init__(self, module, **traits):
        self.description = HTML(value = module.description())
        HasTraits.__init__(self, **traits)
