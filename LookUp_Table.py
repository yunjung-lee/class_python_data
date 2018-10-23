
def paraCap() :  # 파라볼라 캡.

    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH




    Lookup = [0] * 256

    for i in range(256) :

        Lookup[i] = int(255- 255.0 * (( i / 128.0 - 1) * ( i / 128.0 - 1)))




    # 중요! 출력메모리의 크기를 결정

    outW = inW;  outH = inH;

    outImage = [];   tmpList = []

    for i in range(outH):  # 출력메모리 확보(0으로 초기화)

        tmpList = []

        for k in range(outW):

            tmpList.append(0)

        outImage.append(tmpList)

    #############################

    # 진짜 영상처리 알고리즘을 구현

    ############################

    for  i  in  range(inH) :

        for  k  in  range(inW) :

                outImage[i][k] = Lookup[inImage[i][k]]




    display()
