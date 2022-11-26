The directory architecture is

- iDFlakies
  - dataset/selected (here is where your data will go)
  - IDFlakies (here is the IDFlakies that you clone from github)
  - all other files here (download.py, run.py, etc)


Run download.py first to download and checkout the correct sha 
Run nohup run.py to get the results. The results can be checked through:  
- nohup.out to see the [error] or [INFO] information
- logging.out will keep the timing seconds. Check whether the time period is valid to see if it is run successfully.
- the detection results should be saved under project/.dtfixingtools/detection-results


Remember to modify the absolute path to make it run correctly.  
download.py: line3  
run.py: line5, line27  