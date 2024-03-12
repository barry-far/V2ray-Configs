import requests
import os
import base64

# Function to generate base64 encoded header text for each protocol
def generate_header_text(protocol_name):
    titles = {
        'vmess': "8J+GkyBCYXJyeS1mYXIgfCB2bWVzc/Cfpbc=",
        'vless': "8J+GkyBCYXJyeS1mYXIgfCB2bGVzc/Cfpbc=",
        'trojan': "8J+GkyBCYXJyeS1mYXIgfCBUcm9qYW7wn6W3",
        'ss': "8J+GkyBCYXJyeS1mYXIgfCBTaGFkb3dTb2Nrc/Cfpbc=",
        'ssr': "8J+GkyBCYXJyeS1mYXIgfCBTaGFkb3dTb2Nrc1Ig8J+ltw==",
        'tuic': "8J+GkyBCYXJyeS1mYXIgfCBUdWljIPCfpbc=",
        'hy2': "8J+GkyBCYXJyeS1mYXIgfCBIeXN0ZXJpYTLwn6W3"
    }
    base_text = """#profile-title: base64:{base64_title}
#profile-update-interval: 1
#subscription-userinfo: upload=0; download=0; total=10737418240000000; expire=2546249531
#support-url: https://github.com/barry-far/V2ray-Configs
#profile-web-page-url: https://github.com/barry-far/V2ray-Configs

"""
    return base_text.format(base64_title=titles.get(protocol_name, ""))

protocols = {
    'vmess': 'vmess.txt',
    'vless': 'vless.txt',
    'trojan': 'trojan.txt',
    'ss': 'ss.txt',
    'ssr': 'ssr.txt',
    'tuic': 'tuic.txt',
    'hy2': 'hysteria2.txt'
}

ptt = os.path.abspath(os.path.join(os.getcwd(), '..'))
splitted_path = os.path.join(ptt, 'Splitted-By-Protocol')

# Ensure the directory exists
os.makedirs(splitted_path, exist_ok=True)

protocol_data = {protocol: generate_header_text(protocol) for protocol in protocols}

# Fetching the configuration data
response = requests.get("https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/All_Configs_Sub.txt").text

# Processing and grouping configurations
for config in response.splitlines():
    for protocol in protocols.keys():
        if config.startswith(protocol):
            protocol_data[protocol] += config + "\n"
            break

# Encoding and writing the data to files
for protocol, data in protocol_data.items():
    file_path = os.path.join(splitted_path, protocols[protocol])
    encoded_data = base64.b64encode(data.encode("utf-8")).decode("utf-8")
    with open(file_path, "w") as file:
        file.write(encoded_data)
