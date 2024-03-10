print("Este é um arquivo que criei para testar os comandos do git durante o curso de Github - Básico ao Avançado!")

print("----- Comandos -----")

print("git status --> mostra as mudanças que foram feitas no repositório antes do commit.")
print("git init --> inicializa um repositório.")
print("git add --> adiciona o arquivo no repositório e ao controle de versão.")
print("git commit -a -m 'mensagem' --> commita todos os arquivos de uma vez, enviando uma mensagem para o repositório explicando o que foi o commit.")
print("git clone <url> --> clona o repositório e baixa ele para a sua máquina.")
print("git pull --> atualiza o repositório remoto para adicionar, editar ou remover os arquivos que estão lá no github, caso esteja desatualizado.")
print("git rm <arquivo> --> remove o arquivo da pasta.")
print("git log --> mostra uma informação do commits realizado no projeto até o momento.")
print("git mv <arquivo> <local de destino> --> move o arquivo.")		
print("git mv <arquivo> <nome do arquivo> --> renomeia um arquivo. Se não mover o arquivo, ele entende que você quer renomear.")
print("git checkout <arquivo> --> desfaz a alteração e muda o arquivo de volta para como ele está no github.")
print("git reset --hard origin/master --> reseta todas as alterações feitas.")
print("git rebase <branch atual> <branch privado> -i --> cria um log para alterar o commits.")

print("----- Branches -----")
print("git branch --> visualiza os branches disponíveis")
print("git branch <nome> --> cria um novo branch")
print("git branch -d <nome da branch> --> apaga a branch.")
print("git checkout <nome de uma branch existente> --> muda para o branch existente.")
print("git checkout -b <nome da branch> --> cria e muda para o branch criado.")
print("git merge <nome> --> une o código duas branches.")

print("----- Stash -----")
print("git stash --> salva o código e guarda no stash")
print("git stash list --> mostra a lista de stashes.")
print("git stash apply <0,1,2,3...> --> recupera a stash.")
print("git stash show -p <0,1,2,3...> --> mostra as modificações da stash.")
print("git stash clear --> limpa todas as stashes da branch.")
print("git stash drop <0,1,2,3...> --> limpa uma stash específica.")

print("----- Tags -----")
print("git tag -a <nome> -m <mensagem> --> cria uma tag e sua mensagem.")
print("git tag --> verifica as tags de uma branch. É como se fosse uma branch de uma branch.")
print("git show <nome> --> verificamos os detalhes de uma tag.")
print("git checkout <nome da tag> --> troca de tag.")
print("git push origin <nome da tag> --> envia a tag pro repositório.")
print("git push origin --tags --> envia mais tag.")

print("----- Análise de Repositórios -----")
print("git fetch --> atualiza todos os branches e tag que ainda não estão reconhecidos por você.")
print("git remote add origin <link> --> adiciona um url de origem para o repositório.")
print("git remote -v --> verifica as origens do repositório.")
print("git remote rm origin --> remove a url de origem.")
print("git submodule add <repo> --> adiciona um submódulo.")
print("git submodule --> verifica os submódulos.")
print("git push --recurse-submodules=on-demand --> atualiza o submódulo.")
print("git show --> dá informações úteis de um branch e seus commits.")
print("git diff --> exibe as diferenças do branch atual com o remoto no terminal.")
print("git shortlog --> dá um log resumido do projeto.")
print("git reflog --> gera um log detalhado sobre tudo que foi feito no repositório, incluindo até mudanças de branch.")


print("----- Otimização do Repositório -----")
print("git clean --> limpa arquivos que não foram trackeados.")
print("git gc --> comprime e remove arquivos em que o git julga desnecessário.")
print("git fsck --> checa a integridade e procura por corrupções.")
print("	git archive --format zip --output master_files.zip master --> Zipa a branch master num arquivo .zip.")
