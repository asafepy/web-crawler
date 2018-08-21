.SILENT:

#------------------------------------------------------------------
# Init webserver
#------------------------------------------------------------------

install:
	python setup.py install

remove_csv:
	rm -f product.csv

reload_create_db:
	rm -f captura.db
	python core/db/database.py

crawler:
	python core/modules/crawler.py

indexer:
	python core/modules/indexer.py


processor:
	python core/modules/processor.py


run: remove_csv reload_create_db crawler processor indexer