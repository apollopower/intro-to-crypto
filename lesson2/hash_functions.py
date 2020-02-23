from hashlib import md5
from random import choice

def md125(s: str) -> str: # use this hash function to generate a collision
  return md5(s.encode()).hexdigest()[:8]
  
def generate_preimage( charSet, prefix='', byteSize=4 ):
  ''' based on a set of characters generate a random string '''
  return prefix + ''.join( choice( charSet ) for _ in range( byteSize ) )

def generate_md125_collisions() -> (str, str):
  ''' Main func to generate collisions / test '''
  charSet = ''.join( [ chr( i ) for i in range( 33, 127 ) ] ) # commonly used ASCII characters
  hashMap = {}
  while True:
    preimage = generate_preimage( charSet, 'nakamoto', 4 )
    digest = md125( preimage )
    if hashMap.get( digest ) and preimage != hashMap.get( digest ):
      print("Collision found: {}, {}".format( hashMap.get( digest ), preimage ) )
      return hashMap.get( digest ), preimage 
    else:
      hashMap[ digest ] = preimage