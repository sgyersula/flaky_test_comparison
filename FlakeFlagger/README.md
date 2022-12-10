# FlakeFlagger
Refer to https://github.com/AlshammariA/FlakeFlagger for more information.

Automation selection script: FlakeFlagger/project-choose-automation/scripts/download_sha_jdk8.py

Prediction results: [flaky_test_comparison](https://github.com/sgyersula/flaky_test_comparison)/[FlakeFlagger](https://github.com/sgyersula/flaky_test_comparison/tree/main/FlakeFlagger)/[predict-result](https://github.com/sgyersula/flaky_test_comparison/tree/main/FlakeFlagger/predict-result)/**results**/

Environment settings:

- Python >=3.6

- imbalanced_learn >= 0.6.2

- numpy >= 1.18.1

- pandas >= 1.0.1

- scikit_learn >= 0.22.1

- Java 1.8.0-341 

- Maven 3.8.6 

  Mainly used commands: 

  bash extended-predict.sh

  bash processed_data.sh
  
  nohup python -u download_sha_jdk8.py --csv_path pr-data.csv > Job_out1.log 2>&1 &
