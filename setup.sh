#!/bin/bash

# --------------------------------------------
# Obsolete
# --------------------------------------------

FONT_FOLDER=$HOME/.fonts
FONTS_LIST=("Monaco_Linux.ttf", "aaaa", "sfsdfg")

echo $FONT_FOLDER
echo $FONTS_LIST

cat <<EOF

******************************************************

Installing Linux programming fonts
github: https://github.com/egorhm/linux-fonts.git

******************************************************

EOF

if [ ! -d $FONT_FOLDER ]; then
    mkdir $FONT_FOLDER
    echo "Folder $FONT_FOLDER is created"
fi

for font in ${FONTS_LIST[@]}
do
    echo $font
done


cat <<EOF

******************************************************
Fonts installed
******************************************************

EOF
