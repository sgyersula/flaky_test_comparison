# Jar from IDoft dataset

Environment settings:

Java 8.

Mainly used commands:

**nohup** **java -cp dtdetector/\*:./castle-java-2.3.0-fat-tests.jar: edu.washington.cs.dt.main.Main --isolate --tests=./allunittests.txt --report=./castle_isolation.txt --minimize=true** **>log.log &**

**nohup** **java -cp dtdetector/\*:./castle-java-2.3.0-fat-tests.jar: edu.washington.cs.dt.main.Main** **--reverse** **--tests=./allunittests.txt --report=./castle_reverse.txt --minimize=true** **>log_reverse.log &**

**nohup** **java -cp dtdetector/\*:./castle-java-2.3.0-fat-tests.jar: edu.washington.cs.dt.main.Main** **--combination --k=2** **--tests=./allunittests.txt --report=./castle_combination.txt --minimize=true** **>log_combination.log &**