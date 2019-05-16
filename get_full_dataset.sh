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
	    # echo 'text;;score' >> $RESULT_DIR/full_$(basename $split).csv

        for file in $split/$sentiment/*; do
            # score_with_fextension=$(basename $file | cut -d '_' -f 2)
            # score=${score_with_fextension%.*}
        
            echo -e "Merging \t $file \t in \t $RESULT_DIR/full_$(basename $split).txt"
            # echo "$(cat $file);;$score" >> $RESULT_DIR/full_$(basename $split).csv
            echo $(cat $file) >> $RESULT_DIR/full_$(basename $split).txt
        done
    done
done
