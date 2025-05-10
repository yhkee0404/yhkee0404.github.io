#!/bin/bash

# Additional fonts should be embedded in the document to ensure it displays correctly after download.
# Alternatively, you can reduce the file size by loading fonts on demand, assuming the required fonts are installed, like this:
# 
# export NOTO_SANS_KR='/usr/local/share/fonts/Google/TrueType/Noto Sans KR/'
# curl -sS https://fonts.google.com/download/list?family=Noto%20Sans%20KR | tail -n +2 | jq ".manifest.fileRefs[].url" -r | xargs -I{} wget -q --content-disposition -P "$NOTO_SANS_KR" {}
# fc-cache -f "$NOTO_SANS_KR"

cwd=$(pwd)
filepaths=(
    "_site/cv/ko/yhkee0404.docx"
    "_site/cv/en/yhkee0404.docx"
)
for filepath in "${filepaths[@]}"
do
    dir="${filepath%/*}"
    file="${filepath##*/}"
    cd $dir
    libreoffice --headless --invisible --convert-to 'pdf:draw_pdf_Export:{"SelectPdfVersion":{"type":"long","value":"3"}}' $file
    cd $cwd
done