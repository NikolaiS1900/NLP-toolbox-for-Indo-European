#!/bin/bash

cd 'Target_text'
rm *.txt

cd ..

cd 'preprocess/Result_character_list'
rm *.txt

cd ../..

cd 'preprocess/preprocessed_text'
rm *.txt

cd ../..

cd 'sort/Result'
rm *.txt

cd ../..

cd 'mirror/Result'
rm *.txt

cd ../..

cd 'extractor/Result'
rm *.txt


read -p "Alle tekstfiler er nu slettet, bortset fra dem i mappen Data i første trin. Tryk på enter for at afslutte..."
