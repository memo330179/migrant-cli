class Base(object):
  """a base command"""
  
  def __init__(self, options, *args, **kwargs):
    self.options = options
    self.args = args
    self.kwargs = kwargs
    
  def run(self):
    raise NotImplementedError("That hasn't been implemented: You should implement it!")