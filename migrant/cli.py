"""
migrant
 
Usage:
  migrant run_migrations
  migrant run_migration <version>
  migrant generate_migration <name>
  migrant -h | --help
  migrant --version
 
Options:
  -h --help                         Show this screen.
  --version                         Show version.
 
Examples:
  migrant -h
 
Help:
  For help using this tool, Ask Guillermo
"""
 
 
from inspect import getmembers, isclass
 
from docopt import docopt
 
from . import __version__ as VERSION
 
 
def main():
    """Main CLI entrypoint."""
    import commands
    options = docopt(__doc__, version=VERSION)
    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for k, v in options.iteritems():
      if v:
        module = getattr(commands, k, None)
        
        if module is not None:
            commands = getmembers(module, isclass)
            command = [command[1] for command in commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()