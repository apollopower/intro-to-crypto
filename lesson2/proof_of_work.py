from hashlib import sha256
from random import choice

CHAR_SET = ''.join( [ chr( i ) for i in range( 33, 127 ) ] )

##################################
#            PART 1              #
##################################

def sha2( preimage: str ) -> str:
  ''' sha256 returning the hex '''
  return sha256( preimage.encode() ).hexdigest()

def binary_leading_0s(hex_str: str):
  ''' returns num of leading 0s in binary for a given hex string '''
  binary_representation = bin(int(hex_str, 16))[2:].zfill(256)
  return len(binary_representation) - len(binary_representation.lstrip('0'))

def is_valid(token: str, date: str, email: str, difficulty: int) -> bool:
  '''
  evaluates the validity of a hashcash token based on the specified difficulty,
  as well as proper hex size and date size
  '''
  nonce = token.split( ':' )[ -1 ]
  tokenDate = token.split( ':' )[ 1 ]
  if len( nonce ) <= 16 and len( date ) <= 6 and len( tokenDate ) <= 6:
    # input params are good; check now for proof-of-work
    digest = sha2( token )
    if difficulty == binary_leading_0s( digest ):
      return True
  return False
  


##################################
#            PART 2              #
##################################

def generateNonce( desiredLen: int ) -> str:
  '''
  generates a random nonce to be used as input for proof of work
  '''
  return ''.join( [ choice( CHAR_SET ) for i in range( desiredLen ) ] )

def mint(date: str, email: str, difficulty: int) -> str:
  '''
  does the work of producing a hash token with valid a valid number
  of leading binary 0's based on the difficulty specified
  '''
  prefix = '1:' + date + ':' + email + ':'
  nonce = generateNonce( 16 )
  digest = sha2( prefix + nonce )
  while binary_leading_0s( digest ) != difficulty:
    nonce = generateNonce( 16 )
    digest = sha2( prefix + nonce )
    if binary_leading_0s( digest ) > 10: print( binary_leading_0s( digest ) )
  return prefix + nonce
  