mkdir logos_tmp
mogrify -format png -path ./logos_tmp ./logos_original/*
rm -r logos_original
mv logos_tmp logos_original
mogrify -resize 400x200 -background white -gravity center -extent 400x200 -path ./logos_resized ./logos_original/*.png
