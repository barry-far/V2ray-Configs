import pybase64
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
        'https://mrpooya.xyz/api/ramezan/fastRay.php?sub=1',
        'https://mrpooya.xyz/api/ramezan/GreenNet.php?sub=1',
        'https://mrpooya.xyz/api/meli.php?forv2rayng=1'
    ]
    dir_links = [
        'https://raw.githubusercontent.com/IranianCypherpunks/sub/main/config',
        'https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/sub/sub_merge.txt',
        'https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/mix',
        'https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/donated'

    ]

    decoded_links = decode_links(links)
    decoded_dir_links = decode_dir_links(dir_links)
    merged_configs = decoded_links + decoded_dir_links
    output_folder = os.path.abspath(os.path.join(os.getcwd(), '..'))

    # Delete existing output files
    filename = os.path.join(output_folder, f'All_Configs_Sub.txt')
    if os.path.exists(filename):
        os.remove(filename)
    for i in range(20):
        filename = os.path.join(output_folder, f'Sub{i}.txt')
        if os.path.exists(filename):
            os.remove(filename)
    

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


    
if __name__ == "__main__":
    main()
