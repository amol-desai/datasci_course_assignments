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
    key = record[0]
    value = record[1]
    docid = key
    words = value.split()
    for w in words:
      mr.emit_intermediate(w, docid)

def reducer(key, values):
    # key: word
    # value: list of docid
    values = list(set(values))
    mr.emit((key, values))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
