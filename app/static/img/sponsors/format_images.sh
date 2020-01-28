mkdir current_sponsors_tmp
mogrify -format png -path ./current_sponsors_tmp ./current_sponsors/*
rm -r current_sponsors
mv current_sponsors_tmp current_sponsors
mogrify -resize 100x100 -background white -gravity center -extent 100x100 -path ./current_sponsors_resized ./current_sponsors/*.png
cp -R current_sponsors/. all_sponsors/.
cp -R current_sponsors_resized/. all_sponsors_resized/.
