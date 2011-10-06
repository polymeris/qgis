git checkout gh-pages
cat yaml-header ../qgis.wiki/Home.md > index.md && \
    git add index.md && git commit -m "Update static pages."
