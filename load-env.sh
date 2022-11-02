#! /bin/bash

host=`hostname`

if [[ "$NERSC_HOST" == cori ]]; then
    echo \$NERSC_HOST matched cori

    module load cray-python/3.8.5.0
    which python

    export SS_DIR="$CFS"/m3918/pearson
    echo "\$SS_DIR = $SS_DIR"
elif [[ "$NERSC_HOST" == perlmutter ]]; then
    echo \$NERSC_HOST matched perlmutter

    module load cray-python/3.9.4.1
    which python
    export SS_DIR="$CFS"/m3918/pearson
    echo "\$SS_DIR = $SS_DIR"
elif [[ `hostname` =~ ascicgpu030 ]]; then
    echo hostname matched ascicgpu030

    export SS_DIR="$HOME/suitesparse"
    echo "\$SS_DIR = $SS_DIR"
elif [[ `hostname` =~ rzvernal ]]; then
    echo hostname matched rzvernal

    export SS_DIR="/usr/workspace/cwpears/suitesparse"
    echo "\$SS_DIR = $SS_DIR"
fi

