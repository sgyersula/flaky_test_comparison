The directory architecture is

- iDFlakies
  - dataset: here is where your data will go
  - IDFlakies (here is the IDFlakies that you clone from github)
  - all other files here (download.py, run.py, etc)


Run download.py first to download and checkout the correct sha 
Run nohup run.py to get the results. The results can be checked through:  
- nohup.out to see the [error] or [INFO] information
- the detection results should be saved under project/.dtfixingtools/detection-results
- cal.py will check what projects have run successfullly without error.