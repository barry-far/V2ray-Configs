import pybase64
import base64 
import requests
import binascii
import os

fixed_text = """#profile-title: base64:8J+GkyBHaXRodWIgfCBCYXJyeS1mYXIg8J+ltw==
#profile-update-interval: 1
#subscription-userinfo: upload=29; download=12; total=10737418240000000; expire=2546249531
#support-url: https://github.com/barry-far/V2ray-Configs
#profile-web-page-url: https://github.com/barry-far/V2ray-Configs

"""

def decode_base64(encoded):
    decoded = ''
    for encoding in ['utf-8', 'iso-8859-1']:
        try:
            decoded = pybase64.b64decode(encoded + b'=' * (-len(encoded) % 4)).decode(encoding)
            break
        except (UnicodeDecodeError, binascii.Error):
            pass
    return decoded

def decode_links(links):
    decoded_data = []
    for link in links:
        response = requests.get(link)
        encoded_bytes = response.content
        decoded_text = decode_base64(encoded_bytes)
        decoded_data.append(decoded_text)
    return decoded_data

def decode_dir_links(dir_links):
    decoded_dir_links = []
    for link in dir_links:
        response = requests.get(link)
        decoded_text = response.text
        decoded_dir_links.append(decoded_text)
    return decoded_dir_links

def filter_for_protocols(data, protocols):
    filtered_data = []
    for line in data:
        if any(protocol in line for protocol in protocols):
            filtered_data.append(line)
    return filtered_data

def main():
    protocols = ['vmess', 'vless', 'trojan', 'ss', 'ssr', 'hy2', 'tuic', 'warp://']
    links = [
        'https://raw.githubusercontent.com/MrPooyaX/VpnsFucking/main/Shenzo.txt',
        'https://raw.githubusercontent.com/MrPooyaX/SansorchiFucker/main/data.txt',
        'https://mrpooyax.camdvr.org/api/ramezan/lena.php?sub=1',
        'https://mrpooyax.camdvr.org/api/ramezan/run.php?sub=1',
        'https://raw.githubusercontent.com/yebekhe/TVC/main/subscriptions/xray/base64/mix',
        'https://mrpooyax.camdvr.org/api/ramezan/alpha.php?sub=1',
        'https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt',
        'https://raw.githubusercontent.com/mfuu/v2ray/master/v2ray',
        'https://raw.githubusercontent.com/resasanian/Mirza/main/sub',
        'https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/reality',
        'https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/vless',
        'https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/vmess',
        'https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/trojan',
        'https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/shadowsocks',
        'https://raw.githubusercontent.com/ts-sf/fly/main/v2',
        'https://raw.githubusercontent.com/aiboboxx/v2rayfree/main/v2'
    ]
    dir_links = [
        'https://raw.githubusercontent.com/IranianCypherpunks/sub/main/config',
        'https://raw.githubusercontent.com/sashalsk/V2Ray/main/V2Config',
        'https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity.txt',
        'https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/normal/mix',
        'https://mrpooya.top/api/lena.php',
        'https://raw.githubusercontent.com/sarinaesmailzadeh/V2Hub/main/merged',
        'https://raw.githubusercontent.com/freev2rayconfig/V2RAY_SUBSCRIPTION_LINK/main/v2rayconfigs.txt'
    ]

    decoded_links = decode_links(links)
    decoded_dir_links = decode_dir_links(dir_links)

    combined_data = decoded_links + decoded_dir_links
    merged_configs = filter_for_protocols(combined_data, protocols)

    output_folder = os.path.abspath(os.path.join(os.getcwd(), '..'))
    base64_folder = os.path.join(output_folder, 'Base64')

    # Delete existing output files
    filename = os.path.join(output_folder, f'All_Configs_Sub.txt')
    filename1 = os.path.join(output_folder, f'All_Configs_base64_Sub.txt')
    if os.path.exists(filename):
        os.remove(filename)
    elif os.path.exists(filename1):
        os.remove(filename1)
    for i in range(20):
        filename = os.path.join(output_folder, f'Sub{i}.txt')
        if os.path.exists(filename):
            os.remove(filename)
        filename1 = os.path.join(base64_folder, f'Sub{i}_base64.txt')
        if os.path.exists(filename1):
            os.remove(filename1)
    

    # Write merged configs to output file
    output_file = os.path.join(output_folder, 'All_Configs_Sub.txt')
    with open(output_file, 'w') as f:
        f.write(fixed_text)
        for config in merged_configs:
            f.write(config + '\n')

    # Split merged configs into files with no more than 600 configs per file
    with open(output_file, 'r') as f:
        lines = f.readlines()
    num_lines = len(lines)
    max_lines_per_file = 600
    num_files = (num_lines + max_lines_per_file - 1) // max_lines_per_file
    for i in range(num_files):
        profile_title = f'🆓 Git:Barry-far | Sub{i+1} 🫂'  # Dynamic title
        encoded_title = base64.b64encode(profile_title.encode()).decode()  # Encode to base64
        custom_fixed_text = f"""#profile-title: base64:{encoded_title}
#profile-update-interval: 1
#subscription-userinfo: upload=29; download=12; total=10737418240000000; expire=2546249531
#support-url: https://github.com/barry-far/V2ray-Configs
#profile-web-page-url: https://github.com/barry-far/V2ray-Configs

"""

        f.write(custom_fixed_text)
        start_index = i * max_lines_per_file
        end_index = min((i + 1) * max_lines_per_file, num_lines)
        for line in lines[start_index:end_index]:
            f.write(line)
                
    # Encode to base64 and save merged configs to a single file
    for i in range(num_files):
        input_filename = os.path.join(output_folder, f'Sub{i+1}.txt')
        with open(input_filename, 'r') as input_file:
            config_data = input_file.read()

    # Encode and save each Sub{i+1}.txt file to base64_folder as Sub{i+1}_base64.txt
    for i in range(num_files):
        profile_title = f'🆓 Git:Barry-far | Sub{i+1} 🫂'  # Dynamic title
        encoded_title = base64.b64encode(profile_title.encode()).decode()  # Encode to base64
        custom_fixed_text = f"""#profile-title: base64:{encoded_title}
#profile-update-interval: 1
#subscription-userinfo: upload=29; download=12; total=10737418240000000; expire=2546249531
#support-url: https://github.com/barry-far/V2ray-Configs
#profile-web-page-url: https://github.com/barry-far/V2ray-Configs

"""
        input_filename = os.path.join(output_folder, f'Sub{i+1}.txt')
        output_filename = os.path.join(base64_folder, f'Sub{i+1}_base64.txt')
        encoded_config = base64.b64encode(config_data.encode()).decode()
        with open(output_filename, 'w') as output_file:
            output_file.write(custom_fixed_text + encoded_config)
    

    
if __name__ == "__main__":
    main()
