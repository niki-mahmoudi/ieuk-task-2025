PATH = "sample-log.log"
FLAG = False # flag to mark if there is suspicious activity 

def check_doc():
    with open(PATH, 'r') as logs:
        lines = len(logs.readlines())
        for line in logs:

            # gets ip from the logs
            ip = line.split(' - ', 1)[0].strip()

            # gets the request type from the logs
            start_of_request = line.find('"')
            end_of_request = line.find('"', start_of_request + 1)
            req = line[start_of_request + 1:end_of_request].strip()

            if req is None:
                FLAG = True

    return FLAG
