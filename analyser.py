# this code is used to analyse the logs
import pandas as pd

PATH = "sample-log.log"

with open(PATH, 'r') as logs:
    lines = len(logs.readlines())

    
# creates a csv file 
df = pd.read_csv(
    'data.csv',
    sep=",",
    header=None,
    names=[
        "ip", "identity", "country", "user", "timestamp",
        "request", "status", "bytes", "referer", "ua", "rt"
    ],
    quotechar='"'
    )

# counts how many times an ip address has been detected 
counts = df["ip"].value_counts()

total = 0
for count in counts:
    total += count

print(counts)
print(counts/total*100) # to calculate the percentage of appearance


