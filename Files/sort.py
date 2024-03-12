import requests
import os
import base64

vmess_text = """#profile-title: base64:8J+GkyBCYXJyeS1mYXIgfCB2bWVzc/Cfpbc=
#profile-update-interval: 1
#subscription-userinfo: upload=0; download=0; total=10737418240000000; expire=2546249531
#support-url: https://github.com/barry-far/V2ray-Configs
#profile-web-page-url: https://github.com/barry-far/V2ray-Configs

"""
vless_text = """#profile-title: base64:8J+GkyBCYXJyeS1mYXIgfCB2bGVzc/Cfpbc=
#profile-update-interval: 1
#subscription-userinfo: upload=0; download=0; total=10737418240000000; expire=2546249531
#support-url: https://github.com/barry-far/V2ray-Configs
#profile-web-page-url: https://github.com/barry-far/V2ray-Configs

"""
trojan_text = """#profile-title: base64:8J+GkyBCYXJyeS1mYXIgfCBUcm9qYW7wn6W3
#profile-update-interval: 1
#subscription-userinfo: upload=0; download=0; total=10737418240000000; expire=2546249531
#support-url: https://github.com/barry-far/V2ray-Configs
#profile-web-page-url: https://github.com/barry-far/V2ray-Configs

"""
ss_text = """#profile-title: base64:8J+GkyBCYXJyeS1mYXIgfCBTaGFkb3dTb2Nrc/Cfpbc=
#profile-update-interval: 1
#subscription-userinfo: upload=0; download=0; total=10737418240000000; expire=2546249531
#support-url: https://github.com/barry-far/V2ray-Configs
#profile-web-page-url: https://github.com/barry-far/V2ray-Configs

"""
ssr_text = """#profile-title: base64:8J+GkyBCYXJyeS1mYXIgfCBTaGFkb3dTb2Nrc1Ig8J+ltw==
#profile-update-interval: 1
#subscription-userinfo: upload=0; download=0; total=10737418240000000; expire=2546249531
#support-url: https://github.com/barry-far/V2ray-Configs
#profile-web-page-url: https://github.com/barry-far/V2ray-Configs

"""
tuic_text = """#profile-title: base64:8J+GkyBCYXJyeS1mYXIgfCBUdWljIPCfpbc=
#profile-update-interval: 1
#subscription-userinfo: upload=0; download=0; total=10737418240000000; expire=2546249531
#support-url: https://github.com/barry-far/V2ray-Configs
#profile-web-page-url: https://github.com/barry-far/V2ray-Configs

"""
hy2_text = """#profile-title: base64:8J+GkyBCYXJyeS1mYXIgfCBIeXN0ZXJpYTLwn6W3
#profile-update-interval: 1
#subscription-userinfo: upload=0; download=0; total=10737418240000000; expire=2546249531
#support-url: https://github.com/barry-far/V2ray-Configs
#profile-web-page-url: https://github.com/barry-far/V2ray-Configs

"""

ptt = os.path.abspath(os.path.join(os.getcwd(), '..'))
vmess_file = os.path.join(ptt, 'Splitted-By-Protocol/vmess.txt')
vless_file = os.path.join(ptt, 'Splitted-By-Protocol/vless.txt')
trojan_file = os.path.join(ptt, 'Splitted-By-Protocol/trojan.txt')
ss_file = os.path.join(ptt, 'Splitted-By-Protocol/ss.txt')
ssr_file = os.path.join(ptt, 'Splitted-By-Protocol/ssr.txt')
tuic_file = os.path.join(ptt, 'Splitted-By-Protocol/tuic.txt')
hy2_file = os.path.join(ptt, 'Splitted-By-Protocol/hysteria2.txt')

with open(vmess_file, "w") as file:
    file.write(vmess_text)
with open(vless_file, "w") as file:
    file.write(vless_text)
with open(trojan_file, "w") as file:
    file.write(trojan_text)
with open(ss_file, "w") as file:
    file.write(ss_text)
with open(ssr_file, "w") as file:
    file.write(ssr_text)
with open(tuic_file, "w") as file:
    file.write(tuic_text)
with open(hy2_file, "w") as file:
    file.write(hy2_text)

vless = ""
trojan = ""
ss = ""
ssr = ""
tuic = ""
hy2 = ""
respnse = requests.get("https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/All_Configs_Sub.txt").text
for config in respnse.splitlines():
    if config.startswith("vmess"):
        open(vmess_file, "a").write(config + "\n")     
    if config.startswith("vless"):
        vless += config + "\n"  
    if config.startswith("trojan"):
        trojan += config + "\n"   
    if config.startswith("ss"):   
        ss += config + "\n"
    if config.startswith("ssr"):
        ssr += config + "\n"
    if config.startswith("tuic"):
        ssr += config + "\n"
    if config.startswith("hy2"):
        ssr += config + "\n"
 
open(vless_file, "w").write(base64.b64encode(vless.encode("utf-8")).decode("utf-8"))  
open(trojan_file, "w").write(base64.b64encode(trojan.encode("utf-8")).decode("utf-8"))  
open(ss_file, "w").write(base64.b64encode(ss.encode("utf-8")).decode("utf-8"))  
open(ssr_file, "w").write(base64.b64encode(ssr.encode("utf-8")).decode("utf-8"))  
open(tuic_file, "w").write(base64.b64encode(tuic.encode("utf-8")).decode("utf-8"))  
open(hy2_file, "w").write(base64.b64encode(hy2.encode("utf-8")).decode("utf-8"))  

