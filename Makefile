
MYSQL_VERSION=5.7.16

build_app:
	@echo 'Construcción de imágenes e inicialización de servicio backend y db'
	@echo 'Construcción de imágen APP'

	cd App && docker build -t servicio-app .

	@echo 'Descargando mysql'
	docker pull mysql:$(MYSQL_VERSION)

	@echo ''
	@echo '-----------------------'
	@echo 'Imágenes agregadas'
	@echo '-----------------------'
	@echo ''


