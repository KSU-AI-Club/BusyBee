#!/bin/bash

# Usage: ./<path-to-script> or bash <path-to-script>
# You need to change your current working directory to the one that contains the images and labels folder

if [ ! -d ./images ] && [ ! -d ./labels ]; then
    printf "You are in the wrong directory.\nChange directory to the directory that contains images and labels.\n"
    exit 1
else
    TRIBES=( "$(basename $(ls */*_[0-9]_*.txt | xargs -I DIR sh -c "echo DIR | tr '_' ' ' | awk '{ print \$1 }'" | uniq))" )
    
    printf "\e[32mCreating Tribe Directories...\e[0m\n"
    mkdir -vp ${TRIBES} 
    
    for TRIBE in ${TRIBES};
    do
        printf "%s: \e[32mCreating subdir...\e[0m\n" ${TRIBE}
        mkdir -vp ${TRIBE}/images
        mkdir -vp ${TRIBE}/labels 
    
        mv */${TRIBE}*.jpg ${TRIBE}/images
        mv */${TRIBE}*.txt ${TRIBE}/labels
    done;
    
    unset TRIBES

    printf "\e[32mRemoved:\e[0m \n"
    rm -rvf images labels
    [ -f $0 ] && mv -v $0 ../
    
    printf "\e[32mDone\e[0m\n"

    exit 0
fi
