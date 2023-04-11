Black="\033[1;30m"       # Black
Red="\033[1;31m"         # 
Green="\033[1;32m"       # 'هGreen
Yellow="\033[1;33m"      # Yellow
Blue="\033[1;34m"        # Blue
Purple="\033[1;35m"      # Purple
Cyan="\033[1;36m"        # Cyan
White="\033[1;37m"       # White
#IMPORT LIBRARYS 
#       - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
try :
    from search_engines import Google
except:
    print(f'    |[-] {Red} TO Run The Tool , You Must Put The search_engines Folder {White} ')
    print(f'    |[-] {Red} And The Tool Must Be Outside The Folder {White}')
    exit()
#       - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

  
try :
    import requests
except:
        print(f'    |[-] {Red}  Please Install Requests Lbrary  ')
        print(f'    |[-] {Red}  pip install requests  ')
        exit()

#       - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


try:
    import os
except:
        print(f'    |[-] {Red}  Please Install Os Lbrary  ')
        print(f'    |[-] {Red}  pip install os  ')
        exit()
        
#       - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        


try :
    import random
except:
        print(f'    |[-] {Red}  Please Install Random Lbrary  ')
        print(f'    |[-] {Red}  pip install random  ')
        exit()
    
#       - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


print(f'''
            /gg\          /gg\ 
           /g{Yellow}.{White}gg\        /gg{Yellow}.{White}g\ 
          |gg{Yellow}..{White}gg\      /gg{Yellow}..{White}gg| 
          |gg{Yellow}...{White}g|      |g{Yellow}...{White}gg| 
          |gg{Yellow}...{White}g|      |g{Yellow}...{White}gg| 
          \gg{Yellow}..{White}g/       \g{Yellow}..{White}gg/ 
           |gg.gvgggggggvg.gg| 
          /ggggggggggggggggggg\ 
         /gggg(((ggggggg)))gggg\ 
        |ggggg{Red}....{White}ggggg{Red}....{White}ggggg| 
        |ggggg{Red}....{White}ggggg{Red}....{White}ggggg| 
        |ggcccgggg\___/ggggcccgg| 
        |ggcccccgggg|ggggcccccgg| 
          \gcccggg\{Yellow}---{White}/gggcccg/ 
             \ggggggggggggg/

    | [+] {Yellow}This Tool For Searching For Leaks {White}
    | [+] {Yellow}Do Not Try Too Much Because You Will Be Banned{White}
    | [+] {Yellow}The Search Will Be Saved In This Folder | search_engines {White}
    | [+] {Yellow}You Can Enter The Name Of The Site And The Tool Wiil Search For Leaks {White}
    | [+] {Yellow}You Can Also Enter An Email TO Search For A Password If It Has Been Leake {White}
    
    | [+] {Yellow}This Tool By : {Red}FX{White}  ---  Instagram : {Red}FX_PY3{Yellow}     &  {White}   Telegram channel : {Red}FX_PY               {White}
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
      ''')


class Fx_py():  
    
    try:      
        
        def __init__(self):
            
            self.ranDom='wertyuiopasdfghjklzxcvbnm1234567890'
            self.search = str(input(f'    | [+] {Yellow}Enter The Site Whose Leaks You Want To Search For {Cyan} >>> {White}'))
            self.search=self.search.upper()
            if '.COM' and 'HTTPS://' in self.search:
                self.search=self.search.split('/')[2]
                self.search=self.search.split('.com')[0]
            elif '.COM' in self.search:
                self.search=self.search.split('.com')[0]
            elif '.COM' and 'HTTP://' in self.search:
                self.search=self.search.split('/')[2]
                self.search=self.search.split('.com')[0]
            else:
                pass
                 
            
            
            if len(self.search) <= 3:
                print(f'    | [-] {Red}Please Enter A Valid Site  {White}')
                self.search = str(input(f'    | [+] {Yellow}Enter The Site Whose Leaks You Want To Search For >>> {White}'))
                
                
                if len(self.search) <= 3:
                    print(f'    | [-] {Red}You Did Not Enter A valid Site  {White}')
                    exit()
     
     
            self.title=''
            self.FILTER=[]
            
            
        def git_info(self,url):
            
            
            try:
                    
                    
                    
                    
                    

                    if 'import' in res :
                        pass
                    
                    
                    elif '<html>' in res:
                        pass
                    
                    
                    elif '<iostream>' in res:
                        pass
                    
                    elif 'const' in res:
                        pass
                    
                    elif '?php' in res:
                        pass
                    
                    elif '7z' in res:
                        pass
                    
                    elif 'public' in res:
                        pass
                    
                    
                    else :
                        
                        res=requests.get(url).text
                        text=res.split('<ol class="text"><li class="li1"><div class="de1">')[1]
                        text=text.split('</div></li></ol>')[0]
                        ress=text.split('</div></li><li class="li1"><div class="de1">')
                        
                        
                        
                        
                        for i in ress:
                            
                            
                            if '</div>' in i :
                                filter=(i.split('</div>')[0])
                                
                            else:
                                
                                filter=(i)
                            FILTER=filter.upper()


                            link=url.split('pastebin.com')[1]
                            link='https://pastebin.com/raw'+link
                            res=requests.get(link).text
                            try:
                                reques=requests.post('https://api.translatedlabs.com/language-identifier/identify?fingerprint=1522657272',data={
                                    'etnologue': 'true',
                                    'text': FILTER
                                    }).json()['language'] 
                            
                            except :
                                reques=None
                            
                            if '&NBSP;' in FILTER :
                                pass
                            
                           
                            elif reques=='Arabic':
                                pass
                           
                    
                            elif 'DOWNLOAD' in FILTER :
                                pass
                            
                            elif 'HTTPS' in FILTER :
                                pass
                            
                            elif self.search.upper() in FILTER:
                                pass
                            
                            elif 'PASSWORD:' or 'PASSOWRD' in FILTER:
                                self.FILTER.append(i)
                                
                                
                            elif 'EMAIL:'or 'EMAIL' in FILTER:
                                self.FILTER.append(i)
                                
                                
                            elif 'USER:'or 'USER' in FILTER:
                                self.FILTER.append(i)
                                
                                
                            elif 'USERNAME:' or 'USERNAME' in FILTER:
                                self.FILTER.append(i)
                                
                                
                            elif '-' in filter:
                                self.FILTER.append(i)
                                
                                
                            elif '=' in filter:
                                self.FILTER.append(i)
                            
                            
                            else:
                                pass
                            
                            
                        title=self.title
                        response=requests.get(url).text 
                        dat=response.split('<span title="')[1]
                        date=dat.split('">')[0]
                        #print('\n\n')
                        #print(url2)
                        #print(" - "*30)
                        #print(Red+'TITLE : '+Purple+title)
                        #print(Red+'DATE : '+Purple+date)
                        #rint(Red+'TEXT : '+White)
                        #print(len(text))
                        #print(text)
                        #print(" - "*30)
                        
                        
                        if self.FILTER == None or '' or ' ' :
                            pass
                       
                        else :
                            
                            print(f'   | {White}- - - - - - - - - - - - - - - - - - - - -  ')
                            print(f'   | [+] {Yellow}Been Captued Site {White}')
                           
                            try:
                                
                                print(f'   | [+] {Yellow}Site Date | {date}{White}')
                           
                            except:
                                
                                pass
                            
                            print('\n\n')
                            
            except:
                pass
        def URLS(self):
                search1 = self.search
                search = f'site:pastebin.com "{search1}" password '
                engine = Google()
                results = engine.search(search, pages=20)
                print(f'\n    | [+] Please Wait , This May take Up To [2:00 - 3:00 ] \n')
                for data in results.__dict__['_results']:
                    
                    link = data['link']
                    self.title = data['title']
                    fuck='Wait |' ,'Wait \  ', 'Wait --  ' ,'Wait  /  ' ,'Wait |  '
                    fuck=random.choice(fuck)
                    print(f"\r    | [+]{Yellow} {fuck}{White}",end='')

                    self.git_info(link)
                
                if results.__dict__['_results'] == []:
                    
                        print(f'\n\n    | [-]{Red} Check Your Wifi {White} ')
                        print(f'    | [-]{Red} If You Are Already Connected To The WiFi , It Is Possible That You Have Been Blocked Due To Too Many Attempts , Try Later Or Turn The VPN  {White} ')
                        print(f'    | [-]{Yellow} Or We Did Not Find Information For The Site Yiu Entered  {White} ')
                        
                        exit()
                
                for i in self.FILTER :
                
                    try:
                        
                        
                            with open(f"{search1}.txt", "a", encoding='utf-8') as F:
                                    F.write(i+'\n')
                                    
                            
                
                    except:
                        try:
                                
                            
                                
                                with open(f"{search1}.txt", "a", encoding='utf-8') as F:
                                        F.write(i+'\n')                                       
                            
                            
                        except :
                                with open(f"{search1}.txt", "a", encoding='utf-8') as F:
                                        F.write(i+'\n')                                

                        
                    
                F.close()        
                print(f"{Green}   | [+] Done Save in This File -> {os.getcwd()}/{search1}.txt")
                
        
    except:
        pass

Fx=Fx_py()
Fx.URLS()

