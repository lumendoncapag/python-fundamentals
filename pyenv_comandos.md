install :
    sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
    libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl

    curl https://pyenv.run | bash

    vim ~/.bashrc -> Insert:
        export PYENV_ROOT="$HOME/.pyenv"
        export PATH="$PYENV_ROOT/bin:$PATH"
        if command -v pyenv >/dev/null; then
            eval "$(pyenv init -)";
            eval "$(pyenv init --path)"
            eval "$(pyenv virtualenv-init -)"
        fi
    
    exec "$SHELL"

Comandos :

pyenv install 3.7.2 --> install

pyenv versions -> Mostra as versões instaladas
    - Aquelas que tiver um (*) é aque está sendo usada no momento

pyenv global (versao) --> Set a versão em toda a maquina

pyenv local (versao)  --> Set a versão apenas no diretorio

Ambientação:

    pyenv virtualenv versão-do-python nome-do-projeto --> cria um ambiente , onde a versão e as libraries instaladas apenas serão acessadas pelo ambiente;
    
    pyenv active nome-do-projeto
    (my-env) $ (aparece qnd selecionado)
    
    pyenv deactivate

    pyenv virtualenv-delte env --> remove a env