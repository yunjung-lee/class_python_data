

import threading

def display() :

    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH

    # 기존에 캐버스 있으면 뜯어내기.

    if  canvas != None :

        canvas.destroy()

    # 화면 준비 (고정됨)

    window.geometry(str(outH) + 'x' + str(outW))

    canvas = Canvas(window, width=outW, height=outH)

    paper = PhotoImage(width=outW, height=outH)

    canvas.create_image((outW/2, outH/2), image=paper, state='normal')

    # 화면에 출력

    def putPixel() :

        for i in range(0, outH) :

            for k in range(0, outW) :

                data = outImage[i][k]

                paper.put('#%02x%02x%02x' % (data, data, data), (k,i))




    threading.Thread(target=putPixel).start()

    canvas.pack()
