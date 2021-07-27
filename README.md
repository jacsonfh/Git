# Alguns comandos de git  

## Este é um estudo de comandos para usar no repositório git.  

git status #Para ver o status do branch no stage que é local.
git add #Para adicionar arquivos no breach localmente.  
git commit -m "Descrição do Commit"  
git log #Mostra minhas entradas na branch.
git log --decorate #log com mais informacoes.  
git log --author=Jacson #Lista todas as entradas do autor Jacson.  
git shortlog  
git shortlog -sn  
git log --graph  
git show 71ef465e9c1d8069855efa0... #Dentro do git log tem  uma hash e pla hash é possível ver o que foadicionado.  
git diff --name-only #Mostra somente o nome do arquivo que foi modificado.  
git diff #mostra as diferencas antes de commit e para dar uma ultima lida e ver o que você fez.  
git checkout nome_arquivo.py #Fazendo isso o git vai retornar o arquivo para antes da edição.  
git reset HEAD readme_git.py #Fazer o git tirar a última entrada do commit.   
git commit -am #Adicionando todos os modif. mais a minha msg.  
git reset --soft #Volta o Commit para o Stage.  
git reset --mixed #Volta o Commit para o stage, e volta os arquivos para antes do stage  
git reset --hard #apaga o ultimo commit e volta os aquivos para antes de ele existir.  
git reset --soft 001523c82fe2d3fea4480b44eec8f4d270e30a3b #Você deve voltar para um comit anterior.  

## Trabalhando com repositório remoto.   
git init #Se logar no github.  
Adicione a sua chave publica ssh nas configurações de segurança do gitHub.  
git remote add origin git@github.com:jacsonfh/developer.git #conecte a sua pasta ao repositorio desejado.  
git remote -v #Mostra se está conectado ao repositório.  
git push -u origin master #ver o que houve.  
git clone ls nomeclone #Clonar repositório es colha uma nova pasta.  
git switch master #Por exemplo para mudar para branch master.  
É interessante ter uma pasta para cada branch.  
git remote add origin git@github.com:jacsonfh/developer.git -m dev #Adicionar branch especifica.  
Fork - Cria uma cópia de um projeto para você alterar e depois devolver.  
Breanch - Possibilita manter uma versão master e diversas outras assim.  
git checkout -b nome_novo_breach #Criando um breanch -b cria um novo, sem ele muda para o branch em questão.   
git branch #Mostra os branchs que tem e qual você está.  
git branch -D nome_branch_apagar #para apagar um branch especifico.  
Merge e Rebase = para juntar branch com as modificações.  
branch merge junta todas as modificações.  
branch rebase joga as modificações fora do master para o frente da fila do master.  
git init # Comando para inicializar o repositório.  
git push --set-upstream origin testing # Levar a saida para o branch chamado testing.   
git merge testing # Dentro do master leva tudo para o master.  
git log --graph # mostra o gráfico da branch.  
criar o arquivo .gitignore   
git stash para guardar alguma modificacao para aplicar depois WIP - work in progress.  
git stash list mostra todas as minhas modif. guardadas. clear para limpar os statist.
git stash apply para aplicar alguma alteracao.   
git config --global alias.s status #Criar alias no git.  
git tag -a 1.0.0 -m aspas Todos os comandos do Curso.aspas #cria a tag da versão.    
git push origin master --tags  
git revert b56224d7814f594d9149f3f983ad751dee5331fe #para reverter um commit, mas deixa no meu codigo.  
git tag -d 1.0.0 e depois git push origin :1.0.0 tags ou branch para apagar.  
 
 
