git checkout gh-pages
markdown ../qgis.wiki/Home.md > body && \
    cat head body tail > index.html && git commit -m "Update static pages."
