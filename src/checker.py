PATH = "sample-log.log"
LIMIT = 100  # can be changed as needed

def check_doc(ip_counts, problematic_ips):

    with open(PATH, 'r', encoding='utf-8', errors='replace') as logs:
        for l in logs:
            line = l.rstrip('\r\n')

            pos = line.find(' - ')
            if pos != -1:
                ip = line[:pos].strip()
            else:
                sp = line.find(' ')
                ip = line[:sp].strip() if sp != -1 else line.strip() # gets ip address in each line

            # count ip repetitions
            if ip in ip_counts:
                ip_counts[ip] += 1
            else:
                ip_counts[ip] = 1

            # add to problematic list if repeated too much
            if ip_counts[ip] == LIMIT + 1 : 
                problematic_ips.append(ip)

            start_of_request = line.find('"')
            if start_of_request == -1:
                # no opening quote means its malformed
                if ip not in problematic_ips:
                    problematic_ips.append(ip)
                continue

            end_of_request = line.find('"', start_of_request + 1)
            if end_of_request == -1:
                # no closing quote means its malformed
                if ip not in problematic_ips:
                    problematic_ips.append(ip)
                continue

            req = line[start_of_request + 1:end_of_request].strip()
            if not req:  # empty request string
                if ip not in problematic_ips:
                    problematic_ips.append(ip)


def main():
    ip_counts = {}
    problematic_ips = []
    check_doc(ip_counts, problematic_ips)
    print(problematic_ips)

if __name__ == '__main__':
    main()