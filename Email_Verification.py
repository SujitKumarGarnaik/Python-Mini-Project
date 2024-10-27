email=input('Enter Your Email_Id :')
spac,up,sepcial=0,0,0
#CHECK ATLEAST 6 LENGTH
if len(email)>=6:
    #CONTAIN ONLY 1ST LETTER ALPHABET
    if email[0].isalpha():
        #CONTAIN @ ATLEAST 1
        if ('@' in email) and(email.count('@')==1):
            #CONATIN . IN -NEATIVE POSTION FOR .COM IN-4 AND .IN FOR -3
            if (email[-4]==".")^(email[-3]=="."):
                for ele in email:
                    #IF COTAIN SPACE COUNT = 1 IT DOES NOT CONATION SPACE
                    if ele==ele.isspace():
                        spac=1
                    #CONATION ONLY LOWER CASE
                    elif ele.isalpha():
                        if ele==ele.upper():
                            up=1
                            #DOESNOT CONTAINE DIGIT
                    elif ele.isdigit():
                        continue 
                    #CONTINUE ONLY . _ @ ONLY
                    elif ele=="_" or ele=="." or ele=="@":
                        continue
                    else:
                        sepcial=1
                if spac==1 or up==1 or sepcial==1:
                    print('Wrong Email 5')
                else:
                    print(f'Your enter email is write {email}')
            else:
                print('Wrong Email 4')
        else:
            print('Wrong Email 3')
    else:
        print('Wrong Email 2')
else:
    print('Wrong Email 1')