all: anki-hierarchical-tags.zip

anki-hierarchical-tags.zip: hierarchical_tags_addon/*.py *.py README.md
	rm -f anki-hierarchical-tags.zip
	rm -rf dist
	mkdir dist
	cp *.py dist/
	cp -r hierarchical_tags_addon dist/
	cp README.md dist/hierarchical_tags_addon/
	cd dist && zip -r ../anki-hierarchical-tags.zip *
