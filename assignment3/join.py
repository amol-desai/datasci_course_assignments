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
    order_id = record[1]
    mr.emit_intermediate(order_id,record)

def reducer(order_id,records):
    # key: word
    # value: list of docid
    order = None
    for record in records:
        if record[0] == 'order':
            order = record
            records.remove(record)
            break
    if order != None:
        for i,record in enumerate(records):
            record = order+record
            records[i] = record
            mr.emit(record)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
