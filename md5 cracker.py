import hashlib as hl

def title_box():
     """Creates title box"""
     print("            **********************")
     print("            *     MD5 Cracker    *")
     print("            *        by          *")
     print("            *     Azan Shahid    *")
     print("            **********************")

def md5_gen(string):
     """Generate md5 of given string"""
     encoded_string=string.encode('UTF-8')
     md5=hl.md5(encoded_string).hexdigest()
     return md5

def main():
    """This is main part of program"""
    title_box()
    print("Enter md5 hash : ",end=" ")
    string=input()
    print("Enter wordlist : ",end=" ")
    wordlist=input()
    try:
        with open (wordlist) as wordlist:
             a=wordlist.readlines()
             for each in a:
                  if each.endswith('\n'):
                       word=each.strip()  #remove space and \n from start and end
                  else:
                       word=each
                  print("Trying ---> ",word)
                  if md5_gen(word)==string:
                       print("Found  ---> ",word)
                       break
    except IOError:
        print("I/O error occured")
        print("Cannot open wordlist")
                    

main()
