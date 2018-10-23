###텍스트 파일 처리1 ( 열기 --> 작업하기(읽기, 쓰기) --> 닫기)
#읽기, 쓰기

#
fname = 'c:/windows/win.ini'    #원래 있는 파일
fname2 = 'my.txt'               #복사 될 파일

rfp =  open(fname, 'r')
wfp =  open(fname2,'w')

while True :

    instr =  rfp.readline()                 #파일 읽기
    if instr== '' or instr ==None:          # if not instr : 동일한 코드
        break
    print(instr,end='')
    wfp.writelines(instr)                 #파일 쓰기

rfp.close()
wfp.close()
print('ok')                                 #권장 사항: 실행만 되는 코드에 실행 종료를 위해 넣어주는 사인