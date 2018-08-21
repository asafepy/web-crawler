.SILENT:

#------------------------------------------------------------------
# Init Web Crawler
#------------------------------------------------------------------

install:
	python setup.py install

remove_csv:
	rm -f product.csv

open_csv:
	vi product.csv

reload_db_force:
	rm -f captura.db
	python core/db/database.py

crawler:
	python core/modules/crawler.py

processor:
	python core/modules/processor.py

indexer:
	python core/modules/indexer.py



run: remove_csv reload_db_force crawler processor indexer open_csv