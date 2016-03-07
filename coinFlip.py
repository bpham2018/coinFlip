# Author: Bao Pham

# Date: 3/7/16

import random

headsTails = random.randint( 1, 6001 )

if headsTails <= 3000:

	print( "The coin is heads." )
	
if 3000 < headsTails <= 6000:
	
	print( "The coin is tails." )
	
if headsTails = 6001:

	print( "The coin landed on its side!" )