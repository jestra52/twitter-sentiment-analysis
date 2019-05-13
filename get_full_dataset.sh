#!/bin/bash

# You should run this only ONCE if there's no "movie_data" folder
# To run this you should past a train and test folder, like this:
#    $ ./get_full_dataset.sh TRAIN_DATA_DIR TEST_DATA_DIR
# Note: you should consider that each folder must have pos and neg directories

TRAIN_DATA_DIR=$1
TEST_DATA_DIR=$2
RESULT_DIR='movie_data'

if [ ! -d $RESULT_DIR ]; then
    echo "Created '$RESULT_DIR' folder"
    mkdir $RESULT_DIR
fi

for split in $TRAIN_DATA_DIR $TEST_DATA_DIR; do
    for sentiment in pos neg; do
        for file in $split/$sentiment/*; do
            echo -e "Mergin \t $file \t in \t $RESULT_DIR/full_$(basename $split).txt"
            cat $file >> $RESULT_DIR/full_$(basename $split).txt
            echo >> $RESULT_DIR/full_$(basename $split).txt
        done
    done
done
