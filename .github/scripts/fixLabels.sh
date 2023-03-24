# First delete all default labels
gh label list | awk -F '\t' '{ print $1 }' | xargs -I _ gh label delete --confirm '_'

# Create labels for common things
gh label create LaTeX  --description "Potrebno je prekucati text u LaTeX"  --color D93F0B
gh label create Tikz   --description "Potrebno je pretvoriti sliku u Tikz" --color E99695
gh label create Revise --description "Potrebno je označiti greške u PDFu"  --color 1D76DB
