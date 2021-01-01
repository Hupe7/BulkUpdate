import subprocess
import ast
import time


def connect_to_device(ip):
    subprocess.call("adb connect "+str(ip),shell=True)

def install_update(APK_Name):
    subprocess.call("adb install -r "+str(APK_Name)+".apk",shell=True)
    #time.sleep(120)

def disconnect_device(ip):
    subprocess.call("adb disconnect "+str(ip),shell=True)

IP_Adressen = "IP_Adressen.txt"
alle_ips= open(IP_Adressen).read()
alle_ips = ast.literal_eval(alle_ips)
APK = input("Was soll installiert werden (Name der APK) : ")
for a in alle_ips:
    print(a)
    print(APK)

    connect_to_device(a)
    install_update(APK)
    disconnect_device(a)



#subprocess.call("adb devices",shell=True)




