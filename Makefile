
all: 3mf_import_export

3mf_import_export:
	zip 3mf_import_export.zip src/*

clean:
	rm *.zip
