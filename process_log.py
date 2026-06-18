import re


def process_log():
    log_pattern = re.compile(r'')
    can_data = {}
    
    try:
        with open('log.txt','r') as file:
            for line in file:
                line = line.strip()
                match = log_pattern.match(line)
                if match:
                    can_id, data = match.groups()
                    if not all(c == '0' for c in data):
                        can_data[can_id] += data
                    else:
                        can_data[can_id] = data

        for can_id in sorted(can_data.keys()):
            print(f'{can_id}: {can_data[can_id]}')
    except FileNotFoundError:
        print('Log file not found.')
    except Exception as e:
        print(f'something unexpected happened : {e}')

if __name__ =='__main__':
    process_log()