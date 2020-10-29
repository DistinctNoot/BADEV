class NoOneToSummonError(Exception):
  pass

def meme(meme=None):
  if meme == None:
    raise NoOneToSummonError(f"Hehehe, nope")
  else:
    print(meme)

#custom error lol
#also how to raise error