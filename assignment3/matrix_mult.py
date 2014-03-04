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
    if record[0] == 'a':
        mr.emit_intermediate(tuple([record[1],0]),tuple(["a",record[2],record[3]]))
        mr.emit_intermediate(tuple([record[1],1]),tuple(["a",record[2],record[3]]))
        mr.emit_intermediate(tuple([record[1],2]),tuple(["a",record[2],record[3]]))
        mr.emit_intermediate(tuple([record[1],3]),tuple(["a",record[2],record[3]]))
        mr.emit_intermediate(tuple([record[1],4]),tuple(["a",record[2],record[3]]))
    elif record[0] == 'b':
        mr.emit_intermediate(tuple([0,record[2]]),tuple(["b",record[1],record[3]]))
        mr.emit_intermediate(tuple([1,record[2]]),tuple(["b",record[1],record[3]]))
        mr.emit_intermediate(tuple([2,record[2]]),tuple(["b",record[1],record[3]]))
        mr.emit_intermediate(tuple([3,record[2]]),tuple(["b",record[1],record[3]]))
        mr.emit_intermediate(tuple([4,record[2]]),tuple(["b",record[1],record[3]]))

def reducer(key,values):
    # key: word
    # value: list of docid
    toret = 0
    for i,value in enumerate(values):
        for othervalue in values[i:]:
            if (value[1] == othervalue[1]) and (value[0] != othervalue[0]):
                toret += value[2]*othervalue[2]
    if toret != 0:
        mr.emit((key[0],key[1],toret))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
