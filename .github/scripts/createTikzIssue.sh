PAGES=$1
NAME=$2
if [ -z "$(gh issue list -l Tikz -S $NAME)" ]
then
	gh issue create --title "$NAME" --body "[Zadate stranice](../blob/main/Parts/$PAGES.pdf)" --label Tikz \
        && echo "Created Issue $NAME :D"
else
    echo "Issue $NAME already exists!" 
fi
