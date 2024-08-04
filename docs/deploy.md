Se algum modulo foi atualizado reconstrua o requirements com este comando:
poetry export --without-hashes --without-urls | awk '{ print $1 }' FS=';' > requirements.txt

Faz o commit na branch dev

Faz um pull request de dev -> main
Ou vai para main e faz um merge com dev

Servidor faz autobuild