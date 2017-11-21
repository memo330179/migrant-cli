from .base import Base
import os
from datetime import datetime

class GenerateMigration(Base):
  
  def run(self):
    file_path = os.path.dirname(os.path.realpath(__file__))
    print file_path
    migration_name = self.options['<name>']
    
    # get template
    with open('{0}/../../migration_template.txt'.format(file_path), 'rb') as template:
      template_string = template.read()
      
    # modify template
    template_string = template_string.replace('{{migration_name}}', migration_name)
    
    # get the working directory
    cwd = os.getcwd()
    
    # create timestamp
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
      
    # create_migration
    with open('{0}/migrate/{1}_{2}.py'.format(cwd, timestamp, migration_name), 'wb') as migration:
      migration.write(template_string)
      
    print("migration created")