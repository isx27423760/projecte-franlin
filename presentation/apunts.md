## Pandoc 
# markdown to html

[root@i18 projecte-franlin]# dnf -y install pandoc texlive

[root@i18 projecte-franlin]# dnf -y install git gitg meld

[isx27423760@i18 presentation]$ pandoc -t beamer presentacion.md -V theme:Hannover -V author:franlin -o prova.html

[isx27423760@i18 presentation]$ pandoc --standalone --to=dzslides --incremental --css=example.css --output=example.html presentacion.md

Pandoc Documentation:

#pandoc -s --mathml -i -t dzslides SLIDES -o example16a.html

#pandoc -s --webtex -i -t slidy SLIDES -o example16b.html

#pandoc -s --mathjax -i -t revealjs SLIDES -o example16d.html


