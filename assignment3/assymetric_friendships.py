import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    record.sort()
    key = record[0]+" "+record[1]
    mr.emit_intermediate(key,1)

def reducer(key,count):
    # key: word
    # value: list of docid
    if len(count) == 1:
        key = key.split()
        mr.emit((tuple(key)))
        mr.emit((tuple(key[::-1])))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
