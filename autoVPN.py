import subprocess
import pyautogui
import time
import credential
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = False

subprocess.call(r'C:\Program Files (x86)\Cisco\Cisco AnyConnect Secure Mobility Client\vpnui.exe')
vpnconnect = pyautogui.locateCenterOnScreen('vpnconnect.png')
time.sleep(0.5)
if vpnconnect:
    pyautogui.click(vpnconnect)
    vpnnext = None
    while vpnnext is None:
        vpnnext = pyautogui.locateCenterOnScreen('vpnnext.png')
        if vpnnext:
            pyautogui.typewrite(credential.username)
    vpnnextbttn = None
    while vpnnextbttn is None:
        vpnnextbttn = pyautogui.locateCenterOnScreen('vpnnextbttn.png')
        if vpnnextbttn:
            pyautogui.click(vpnnextbttn)
    vpnpass = None
    while vpnpass is None:
        vpnpass = pyautogui.locateCenterOnScreen('vpnpass.png')
        if vpnpass:
            pyautogui.typewrite(credential.password)
    vpnsignin = None
    while vpnsignin is None:
        vpnsignin = pyautogui.locateCenterOnScreen('vpnsignin.png')
        if vpnsignin:
            pyautogui.click(vpnsignin)
    time.sleep(3)
    vpnapprove = None
    while vpnapprove is None:
        vpnapprove = pyautogui.locateCenterOnScreen('vpnapprove.png')
        if vpnapprove:
            pyautogui.click(vpnapprove)
            subprocess.Popen(r"C:\LDPlayer\LDPlayer64\dnplayer.exe")
            time.sleep(15)
            authenticator = None
            while authenticator is None:
                authenticator = pyautogui.locateOnScreen('authenticator.png')
                if authenticator:
                    pyautogui.click(authenticator)
                    approve1 = None
                    while approve1 is None:
                        approve1 = pyautogui.locateCenterOnScreen('approve1.png')
                        if approve1:
                            pyautogui.click(approve1)
                            pyautogui.hotkey('winleft', 'down')
                            vpnyes = None
                            while vpnyes is None:
                                vpnyes = pyautogui.locateCenterOnScreen('vpnyes.png')
                                if vpnyes:
                                    pyautogui.click(vpnyes)
                            vpnok = None
                            while vpnok is None:
                                vpnok = pyautogui.locateCenterOnScreen('vpnok.png')
                                if vpnok:
                                    pyautogui.press('enter')
                                    exit()
        else:
            vpnyes = None
            while vpnyes is None:
                vpnyes = pyautogui.locateCenterOnScreen('vpnyes.png')
                if vpnyes:
                    pyautogui.click(vpnyes)
            vpnok = None
            while vpnok is None:
                vpnok = pyautogui.locateCenterOnScreen('vpnok.png')
                if vpnok:
                    pyautogui.press('enter')
                    exit()
else:
    pyautogui.alert('You are already connected to the VPN.')
exit()

