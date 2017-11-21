from .base import Base
import sys
import os
from importlib import import_module
from inspect import getmembers, isclass




class RunMigration(Base):
  
  def run(self):
    print "Starting"
    sys.path.insert(0, os.getcwd())
    from app.models import mainDB
    import migrate
    
    migrations = sorted(migrate.__all__)
    migration_number = self.options['<version>']
    
    for migration_module in migrations:
      if migration_module.startswith(migration_number):
        migration_mod = migration_module
        
    
    migration_up = mainDB.execute_sql('select * from schema_migrations where version = ?', (migration_number,))
    is_migration_up = migration_up.fetchone() is not None
    
    
    if (not is_migration_up):
      current_migration = import_module('migrate.{0}'.format(migration_mod), 'migrate')
      commands = getmembers(current_migration, isclass)
      command = [command[1] for command in commands if command[0] == migration_mod.split('_', 1)[1]][0]()
      command.up()
      mainDB.execute_sql('INSERT INTO schema_migrations(version) VALUES (?)', (migration_number,))
      mainDB.commit()
      print 'All Done'
    else:
      print 'Migration is already ran'