import objects

class ObjectHolder(dict):
  def __init__(self, *args, **kwargs):
    dict.__init__(self, *args, **kwargs)
    self.players = []
    self.mappables = []
    self.tiles = []
    self.traps = []
    self.thiefs = []
    self.thiefTypes = []
    self.trapTypes = []

  def __setitem__(self, key, value):
    if key in self:
      self.__delitem__(key)
    dict.__setitem__(self, key, value)
    if isinstance(value, objects.Player):
      self.players.append(value)
    if isinstance(value, objects.Mappable):
      self.mappables.append(value)
    if isinstance(value, objects.Tile):
      self.tiles.append(value)
    if isinstance(value, objects.Trap):
      self.traps.append(value)
    if isinstance(value, objects.Thief):
      self.thiefs.append(value)
    if isinstance(value, objects.ThiefType):
      self.thiefTypes.append(value)
    if isinstance(value, objects.TrapType):
      self.trapTypes.append(value)

  def __delitem__(self, key):
    value = self[key]
    dict.__delitem__(self, key)
    if value in self.players:
      self.players.remove(value)
    if value in self.mappables:
      self.mappables.remove(value)
    if value in self.tiles:
      self.tiles.remove(value)
    if value in self.traps:
      self.traps.remove(value)
    if value in self.thiefs:
      self.thiefs.remove(value)
    if value in self.thiefTypes:
      self.thiefTypes.remove(value)
    if value in self.trapTypes:
      self.trapTypes.remove(value)

  def clear(self):
    for i in self.keys():
      del self[i]
