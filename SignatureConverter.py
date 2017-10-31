# CSGO IDA Signature Converter
#
# written by cragson
#

def convertSig( sig ):

    SigArray = []
    
    for char in range( 0, len( sig ), 1 ):

        if( sig[ char ] == ' ' ):
            continue

        SigArray.append( sig[ char ] )

    return SigArray

def generateByteSignature( sig ):

    Signature = convertSig( sig )
    
    ByteSignature = []

    counter = 1

    for element in range( 0, len( Signature ), 1 ):
        
        if( counter >= 2 ):
            
            ByteSignature.append( r'\x' + str( Signature[ element - 1 ] ) + str( Signature[ element ] ) )
            
            counter = 1

            continue
        
        if( Signature[ element ] != '?' ):
             
            counter += 1

            continue

        if( Signature[ element ] == '?'):
            
            ByteSignature.append( r'\x00' )

            counter = 1


    return ''.join( ByteSignature )
    

def generateMask( sig ):

    SigArray = convertSig( sig )

    MaskArray = []

    counter = 1  

    for element in range( 0, len( SigArray ), 1 ):
        
        if( counter >= 2 ):
            
            MaskArray.append( 'x' )
            
            counter = 1

            continue
        
        if( SigArray[ element ] != '?' ):
             
            counter += 1

            continue

        if( SigArray[ element ] == '?'):
            
            MaskArray.append( '?' )

            counter = 1

    return ''.join( MaskArray )

def main():

    times = int( input( " How often should get a Mask generated ? >> " ) )
    if( times <= 0 ):
        exit()

    for time in range( 0, times, 1 ):

        signature = input( " Please enter your signature. \n>> " )

        print( " Mask : " + generateMask( signature ) )

        print( " Byte Signature : " + generateByteSignature( signature ) )
    

if __name__ == '__main__':
    main()
