
from shared import style_list,in_file,grep,header,footer

def main():
    
    data=style_list("numlist",in_file("rawdata"))
    
    print(data)

#-----------------------------

header()
main()
footer()
