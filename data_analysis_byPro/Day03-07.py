## 텍스트 파일 처리 1  ( 열기 -->  작업하기(내맘대로) --> 닫기 )
fname = 'c:/windows/win.ini'  # 원래 있는 파일
fname2 = 'my.txt'  # 복사될 원래 있는 파일

rfp  =  open(fname, 'r')
wfp  =  open(fname2, 'w')

while True :
    inStr = rfp.readline()
    if inStr == '' or  inStr == None :  # if  not inStr
        break
    wfp.writelines(inStr)

rfp.close()
wfp.close()
print('Ok')
