import pybase64
import base64 
import requests
import binascii
import os


def decode_base64(encoded):

    decoded = ''
    for encoding in ['utf-8', 'iso-8859-1']:
        try:
            decoded = pybase64.b64decode(encoded + b'=' * (-len(encoded) % 4)).decode(encoding)
            break
        except (UnicodeDecodeError, binascii.Error):
            pass
    return decoded


def generate_v2ray_configs(decoded_data):

    configs = []

    for config in decoded_data:
        configs.append(config)

    sorted_configs = sorted(configs)

    return sorted_configs


def decode_links(links):

    decoded_data = []

    for link in links:
        response = requests.get(link)
        encoded_bytes = response.content
        decoded_text = decode_base64(encoded_bytes)
        decoded_data.append(decoded_text)

    sorted_configs = generate_v2ray_configs(decoded_data)

    return sorted_configs


def decode_dir_links(dir_links):


    decoded_dir_links = []

    for link in dir_links:
        response = requests.get(link)
        decoded_text = response.text
        decoded_dir_links.append(decoded_text)

    return decoded_dir_links


def main():
    links = [
        'https://raw.githubusercontent.com/MrPooyaX/VpnsFucking/main/Shenzo.txt',
        'https://raw.githubusercontent.com/MrPooyaX/SansorchiFucker/main/data.txt',
        'https://mrpooyax.camdvr.org/api/ramezan/lena.php?sub=1',
        'https://mrpooyax.camdvr.org/api/ramezan/run.php?sub=1',
        'https://mrpooyax.camdvr.org/api/ramezan/v2raySH.php?sub=1',
        'https://raw.githubusercontent.com/yebekhe/TVC/main/subscriptions/xray/base64/mix',
        'https://mrpooyax.camdvr.org/api/ramezan/alpha.php?sub=1'
    ]
    dir_links = [
        'https://raw.githubusercontent.com/IranianCypherpunks/sub/main/config',
        'https://raw.githubusercontent.com/sashalsk/V2Ray/main/V2Config',
        'https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/sub/sub_merge.txt',
        'https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/normal/mix'
    ]

    decoded_links = decode_links(links)
    decoded_dir_links = decode_dir_links(dir_links)
    merged_configs = decoded_links + decoded_dir_links
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
        for config in merged_configs:
            f.write(config + '\n')

    # Split merged configs into files with no more than 1000 configs per file
    with open(output_file, 'r') as f:
        lines = f.readlines()
    num_lines = len(lines)
    max_lines_per_file = 1000
    num_files = (num_lines + max_lines_per_file - 1) // max_lines_per_file
    for i in range(num_files):
        start_index = i * max_lines_per_file
        end_index = (i + 1) * max_lines_per_file
        filename = os.path.join(output_folder, f'Sub{i+1}.txt')
        with open(filename, 'w') as f:
            for line in lines[start_index:end_index]:
                f.write(line)
                
    # Encode to base64 and save merged configs to a single file
    encoded_merged_configs = base64.b64encode("\n".join(merged_configs).encode()).decode()
    output_file = os.path.join(output_folder, 'All_Configs_base64_Sub.txt')
    with open(output_file, 'w') as f:
        f.write(encoded_merged_configs)

    # Encode and save each Sub{i+1}.txt file to base64_folder as Sub{i+1}_base64.txt
    for i in range(num_files):
        input_filename = os.path.join(output_folder, f'Sub{i+1}.txt')
        output_filename = os.path.join(base64_folder, f'Sub{i+1}_base64.txt')

        with open(input_filename, 'r') as input_file:
            config_data = input_file.read()
        
        encoded_config = base64.b64encode(config_data.encode()).decode()

        with open(output_filename, 'w') as output_file:
            output_file.write(encoded_config)
    

    
if __name__ == "__main__":
    main()
