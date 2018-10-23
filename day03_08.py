###텍스트 파일 처리1 ( 열기 --> 작업하기(읽기, 쓰기) --> 닫기)
#읽기, 쓰기

#
fname = 'c:/windows/win.ini'    #원래 있는 파일
fname2 = 'my.txt'               #복사 될 파일

with open(fname, 'r') as  rfp :         #  close() : 없이도 자동으로 닫히는 (에러시 유용) 명명법
    with open(fname2,'w') as wfp :

         inList =  rfp.readlines()                 #파일 읽기(한번에 모두) : 작은 파일은 괜찮은데 큰 파일은 위험

         for instr in inList :
             wfp.writelines(instr)

print('ok')                                 #권장 사항: 실행만 되는 코드에 실행 종료를 위해 넣어주는 사인