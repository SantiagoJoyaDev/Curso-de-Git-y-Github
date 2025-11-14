# ---------- COMANDOS BASICOS ----------

# Para inicializar y usar git y github
# Para iniciar el git --> git init
# Para conectar el repositorio de github --> git remote add origin "Link del repositorio en Github"
# Para añadir los cambios al escenario de stage --> git add .
# Para ver los diferentes cambios que se han realizado antes de hacer un commit --> git status
# Para hacer un guardado de los cambios realizados --> git commit -m "Primer commit"(Se escribe algo en general relacionado de los cambios que se hicierion)
# Para ver ya los diferentes commits(guardados que se han echo) que se han realizado --> git log
# Pero tambien hay diferentes maneras de usar el git log para que nos muestre el contenido de manera mas agradable
# por ejemplo -- > git log --graph -- git log --graph --pretty=oneline -git log --graph --decorate --all --oneline
# Para volver a un estado anterior es como retroceder pero sin haber realizado un commit--> git checkout "nombre del archivo"(Tambien en vez del nombre del arcvhivo se puede colocar el id) tambien se puede volver al mismo estado mas actualizado
# Para volver a un estado anterior pero ya habiendo hecho un commit --> git reset "Nombre del archivo"
# Para la creacion de un alias --> git config --global alias.tree "log --graph --decorate --all --oneline"(Y luego ya solo se usa el comando de git tree)
# Para ver las diferencias entre los ultimos cambios guardados y lo nuevo que se hizo --> git diff
# Para volver tambien a una version anterior pero ahora del proyecto y desaparecen los otros commits que se ha realizado --> git reset --hard
# Para volver al punto mas actualizado por si se hizo un git reset hard sin querer --> git reflog
# Para etiquetar un commit en especifico si es un cambio importante y saber a que se refiere mediante un tag --> git tag "Nombre del tag"
# Por si me voy a una rama de manera repentina pero no quiero hacer un commit sino guardar en borrador lo que hice por el momento --> git stash
# para ver la lista de stash que tengo es --> git stash list cuando ya volvi a la rama y quiero obtener de nuevo lo que deje guardado es --> git stash pop