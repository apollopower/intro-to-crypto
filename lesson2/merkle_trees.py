from hashlib import sha256
import math

#######################################
#              PART 1                 #
#######################################

def calculatePowerDiff( originalNum: int ) -> int:
  '''
  returns the value difference between the provided number and
  the next power of 2. Used to calculate the amount of padding
  needed.
  '''
  diff = 0
  while not math.log2( originalNum ).is_integer():
    diff += 1
    originalNum += 1
  return diff

def mergeHashes( hashList: list ) -> list:
  '''
  given a list of strings, merges two elements at a time in a single hash.
  Returns new list of merged hashes, 1/2 len of original list
  '''
  if not math.log2( len( hashList ) ).is_integer():
    raise Exception( "Num of hashes provided are not power of 2. Please include padding" )
  mergedHashes = []

  for i in range( 0 , len( hashList ), 2 ):
    combinedHash = hashList[ i ] + hashList[ i + 1 ]
    mergedHashes.append( sha256( combinedHash.encode() ).hexdigest() )
  return mergedHashes

def merkleize(sentence: str) -> str:
  hashes = [ sha256( word.encode() ).hexdigest() for word in sentence.split( ' ' ) ]
  if not math.log2( len( hashes ) ).is_integer():
    # Adding proper padding to make blocks a power of 2
    diff = calculatePowerDiff( len( hashes ) )
    hashes.extend( [ chr( 0 ) for x in range( diff ) ] )
  while len(hashes) > 1:
    hashes = mergeHashes( hashes )
  return hashes[ 0 ] # Have accumulated all hashes into a single string
  

#######################################
#              PART 2                 #
#######################################

from enum import Enum
class Side(Enum):
  LEFT = 0
  RIGHT = 1

def validate_proof(root: str, data: str, proof: [(str, Side)]) -> bool:
  currentHash = sha256( data.encode() ).hexdigest()
  for sibHash, side in proof:
    if side.name == 'LEFT':
      currentHash = sha256( ( sibHash + currentHash ).encode() ).hexdigest()
    else:
      currentHash = sha256( ( currentHash + sibHash ).encode() ).hexdigest()
  return currentHash == root


merkleize( "In our village, folks say God crumbles up the old moon into stars." )
