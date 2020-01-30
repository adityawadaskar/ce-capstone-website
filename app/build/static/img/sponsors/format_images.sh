mkdir sponsors_tmp
mogrify -format png -path ./sponsors_tmp ./sponsors_original/*
rm -r sponsors_original
mv sponsors_tmp sponsors_original
mogrify -resize 100x100 -background white -gravity center -extent 100x100 -path ./sponsors_small ./sponsors_original/*.png
mogrify -resize 500x200 -background white -gravity center -extent 500x200 -path ./sponsors_large ./sponsors_original/*.png
