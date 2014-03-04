register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the test file into Pig
--raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);
-- later you will load to other files, example:
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray);

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

f1 = FILTER ntriples BY subject matches '.*rdfabout\\.com.*';
--f1 = FILTER ntriples BY subject matches '.*business.*';
f2 = FOREACH f1 GENERATE * AS (subject2:chararray,predicate2:chararray,object2:chararray);
joined_data = JOIN f1 BY object, f2 BY subject2;
--joined_data = JOIN f1 BY subject, f2 BY subject2;
joined_data = DISTINCT joined_data;


-- store the results in the folder /user/hadoop/example-results
--store joined_data into '/user/hadoop/prob3a' using PigStorage();
store joined_data into '/user/hadoop/prob3b' using PigStorage();
-- Alternatively, you can store the results in S3, see instructions:
-- store count_by_object_ordered into 's3n://superman/example-results';
