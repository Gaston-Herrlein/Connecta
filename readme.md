# Juego _Connecta_

Este juego utiliza la terminal comunicarse con el usuario. Por este motivo hay que indicarle a Docker que inicie una sesión interactiva (-i) de terminal de teletipo (-t).

1. Cree la imagen de docker:

   `docker build -t connecta .`

2. Inicie el contenedor:

   `docker run --rm -ti connetca`
