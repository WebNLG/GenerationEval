### Amazon Mechanical Turk: scripts used for human evaluation experiments for WebNLG+ challenge 2020
## English data

1. The pipeline for data collection is inspired by the simple-amt framework: https://github.com/jcjohnson/simple-amt.
We use parts of its code, highly modify them and add our adjustments to build the scripts in particular for our task.

2. To start data collection, please look into the .sh files. They have to be started in separate terminal windows.
Those with 'publish' in their titles, deal with publishing tasks on AMT, while those with 'review' in them extract results
of these tasks and assign qualifications to the workers based on their performance.

3. Do not forget to add and edit the 'config.json' file accordingly! We provide the example file in this repository.
