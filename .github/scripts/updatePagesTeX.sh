if [ -d Src/Pages ]
then
    rm Src/Pages.tex
for i in $(ls Src/Pages | grep tex$)
    do
        printf '\input{Pages/%s}\n' ${i%.*} >> Src/Pages.tex
    done
else
    echo "No Src/Pages, Doing Nothing"
fi 
