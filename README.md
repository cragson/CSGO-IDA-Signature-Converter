# CSGO-IDA-Signature-Converter
This is a litte script written in python 3.6.2, which generates you a mask and a byte signature out of a IDA Signature.

Example Usage:
                      [ IDA-Signature ]
                    
[ Input ] => A3 ? ? ? ? C7 05 ? ? ? ? ? ? ? ? E8 ? ? ? ? 59 C3 6A ?

                          [ Mask ]

[ Output ] => x????xx????????x????xxx?


                      [ Byte-Signature ]

[ Output ] => \xA3\x00\x00\x00\x00\xC7\x05\x00\x00\x00\x00\x00\x00\x00\x00\xE8\x00\x00\x00\x00\x59\xC3\x6A\x00
