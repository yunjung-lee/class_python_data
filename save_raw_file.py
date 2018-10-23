
import struct

def saveFile() :

    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH

    saveFp = asksaveasfile(parent=window, mode='wb',

                               defaultextension="*.raw", filetypes=(("RAW파일", "*.raw"), ("모든파일", "*.*")))

    for i in range(outW):

        for k in range(outH):

            saveFp.write( struct.pack('B',outImage[i][k]))




    saveFp.close()
