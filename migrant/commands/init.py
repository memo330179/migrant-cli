from .base import Base
import os
from datetime import datetime
from app.models import mainDB

class Init(Base):
  
  def run(self):
    
    # create the template
    with open('init_template.txt', 'rb') as initializer:
      init_template = initializer.read()
      
    # get current location
    cwd = os.getcwd()
    
    # create migrate dir
    migrate_dir = '{0}../migrate'.format(cwd)
    if not os.path.exists(migrate_dir):
      os.makedirs(migrate_dir)
      
    # create file  
    fname = '{0}/{1}'.format(cwd, '__init__.py')
    if not os.path.isfile(fname):
      with open(fname, 'wb') as initializer:
        initializer.write(init_template)
        initializer.write('VERSION = 0')
        
    mainDB.execute_sql('CREATE TABLE schema_migrations (version integer PRIMARY KEY);')
    mainDB.commit()
        
    
      
        
    print('Migration directory created')