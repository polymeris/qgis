git checkout gh-pages
markdown ../qgis.wiki/Home.md > body && \
    cat head > index.html && \
    tail -n +2 body >> index.html && \
    cat tail >> index.html && \
    git commit -a -m "Update static pages"
