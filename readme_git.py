#!/usr/bin/env python

"""readme_git.py:Este programa mostra os comandos aprendidos no curso de Git/Github. """

__author__ = "Jacson"
__copyright__ = "Copyright 2021, Brasil"
__annotations__ = "URL da Convenção sobra anotação. https://www.python.org/dev/peps/pep-0257/"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Jacson"
__email__ = "jacsonfh@gmail.com"
__status__ = "Production"

import os

os.system('clear') or None

print("\nEste é um estudo de comandos para usar no repositório git.\n")
print("git status #Para ver o status do branch no stage que é local.")
print("git add #Para adicionar arquivos no breach localmente.")
print("git commit -m ``Arquvos que eu envei`` ")
print("git log #Mostra minhas entradas na branch") 
print("git log --decorate #log com mais informacoes.")
print("git log --author=Jacson #Lista todas as entradas do autor Jacson.")
print("git shortlog")
print("git shortlog -sn")
print("git log --graph")
print("git show 71ef465e9c1d8069855efa0ad912362644e6f01d #Dentro do git log tem  uma hash e pla hash é possível ver o que foi adicionado.")
print("git diff #mostra as diferencas antes de commit e para dar uma ultima lida e ver o que você fez.")
print("git diff --name-only #Mostra somente o nome do arquivo que foi modificado.")
print("git checkout nome_arquivo.py #Fazendo isso o git vai retornar o arquivo para antes da edição.")
print("git reset HEAD readme_git.py #Fazer o git tirar a última entrada do commit")
print("git commit -am #Adicionando todos os modif. mais a minha msg.")
print("git reset --soft #Volta o Commit para o Stage.")
print("git reset --mixed #Volta o Commit para o stage, e volta os arquivos para antes do stage")
print("git reset --hard #apaga o ultimo commit e volta os aquivos para antes de ele existir.")
print("git reset --soft 001523c82fe2d3fea4480b44eec8f4d270e30a3b #Você deve voltar para um comit anterior.")
print("\n")
print("Trabalhando com repositório remoto. ")
print("Se logar no github.")
print("Adicione a sua chave publica ssh nas configurações de segurança do gitHub.")
print("git remote add origin git@github.com:jacsonfh/developer.git #conecte a sua pasta ao repositorio desejado.")
print("git remote -v #Mostra se está conectado ao repositório.")
print("git push -u origin master #ver o que houve.")
print("git clone ls nomeclone #Clonar repositório escolha uma nova pasta.")
print("git switch master #Por exemplo para mudar para branch master.")
print("É interessante ter uma pasta para cada branch.")
print("git remote add origin git@github.com:jacsonfh/developer.git -m dev #Adicionar branch especifica.")
print("Fork - Cria uma cópia de um projeto para você alterar e depois devolver.")
print("Breanch - Possibilita manter uma versão master e diversas outras assim.")
print("git checkout -b nome_novo_breach #Criando um breanch -b cria um novo, sem ele muda para o branch em questão. ")
print("git branch #Mostra os branchs que tem e qual você está.")
print("git branch -D nome_branch_apagar #para apagar um branch especifico.")
print("# Merge e Rebase = para juntar branch com as modificações.")
print("branch merge junta todas as modificações.")
print("branch rebase joga as modificações fora do master para o frente da fila do master.")
print("git init # Comando para inicializar o repositório.")
print("git push --set-upstream origin testing # Levar a saida para o branch chamado testing")



