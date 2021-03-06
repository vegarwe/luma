====
luma
====

---------------------------------------
LDAP browser and administration utility
---------------------------------------

:Date:           April 26, 2011
:Copyright:      GNU General Public License version 2 or later
:Manual section: 1
:Manual group:   LDAP administration utility

SYNOPSIS
========
luma [OPTIONS]

DESCRIPTION
===========
Luma is a cross-platform, open source LDAP browser and administration utility,
capable of managing data stored on LDAP enabled server. It is written in Python,
with PyQt4 (*GUI*) and python-ldap (*LDAP connections*). Luma supports plugins 
through its own plugin system. A selection of plugins, providing useful LDAP 
functionality, is includeed with the base application:

- *Browser*:
  Provides a familiar interface to browse the entry tree on connected LDAP 
  enabled servers. Entry attributes can be edited and deleted. Supports adding
  filters to limit expansions on large subtrees.
- *Template*:
- *Search*:
  A specialized search plugin to do advanced and complex search on a LDAP
  server. Supports filter creation that can be applied in the Browser plugin.

Plugins included in *Luma 2.4*, but not ported from PyQt3 yet:

- *Schema browser*:
- *Addressbook*: Supports building addressbooks from LDAP entries on different 
  servers.
- *Massive user creation*:
- *Admin utilities*:

OPTIONS
=======
A summary of the options supported by *luma* is included below.

-h, --help
	Display a help message and exit.

-v, --verbose
	print more error, debug and info messages to the console.

--clear-config
	clear the config file before launching Luma.

--clear-serverlist
	clear the serverlist before launching Luma.

--clear-templates
	clear the templates file before launching Luma.

--clear-filters
    clear the filters file before launching Luma.

--clear-all
	clear everything before launching Luma. This will result in the same as 
	providing all the before mentioned clear options.

.. --config-dir=DIR
.. 	run Luma with another configuration directory.

.. --plugin-dir=DIR
..  define another directory to look for plugins. DIR will be appended to the 
.. 	list of default plugin directories.

FILES
=====
``~/.config/luma``
	Default directory for configuration data.

``~/.config/luma/luma.conf``
	Application settings.

``~/.config/luma/serverlist.xml``
	The serverlist.

``~/.config/luma/templatelist.xml``
	The templatelist created by the Template plugin.

``-/.config/luma/filters``
    The saved LDAP filters created by the Search plugin.

BUGS
====
Bug tracker: http://sourceforge.net/tracker/?group_id=89105

RESOURCES
=========
Website: http://luma.sf.net

AUTHORS
=======
Originally written and developed by Wido Depping wido@users.sourceforge.net 
from 2003, with help from Bjørn Over Grøtan bgrotan@grotan.com and Vegar 
Westerlund vegarwe@users.sourceforge.net.

Rewritten for PyQt4 and ported to multiple platforms in 2011 by Christian 
Forfang cforfang@gmail.com, Einar Uvsløkk einar.uvslokk@gmail.com, Johannes 
Harestad johannesharestad@gmail.com, Per Ove Ringstad peroveri@stud.ntnu.no,
Simen Natvig simen.natvig@gmail.com, Sondre Frisvold sondre.frisvold@c2i.net

