@echo off
@cd %DIR%

cd trin1_samlet_korpus\Resultat_samlet_korpus
del /f *.txt

cd ..\..

cd trin2_stopord\Resultat
del /f *.txt

cd ..\..

cd trin3_Frekvensliste\Resultat
del /f *.txt

cd ..\..

cd trin4_lemma_token\Resultat
del /f *.txt

echo All text files are now deleted, except from those in the directory "Data" in "trin1_samlet_korpus\Resultat_samlet_korpus"
@pause

Rem Batch-script lavet af Nikolai Sandbeck
