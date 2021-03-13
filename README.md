# Tools-do-LiveDivulgador
Todos os scripts usados para complementar a vida do bot

## Pré requisitos
- Python 3.x
- Python-dotenv (opcional, caso esteja em um ambiente de desenvolvimento)

## Ficheiros
Não esquecer retirar o prefixo `ex_` de todos os ficheiros `.csv`.

O ficheiro `streamers.csv` vem do [LiveDivulgador](https://github.com/LiveDivulgador/Live-Divulgador)

Já as colunas do ficheiro `streamers_mod.csv` têm o seguinte significado:

- Nome: Nome do(a) streamer

- Avatar: URL para o avatar do(a) streamer

- Twitter: Username do twitter do(a) streamer, caso não tenha não irá ser incluído da geração das imagens (se o(a) streamer não tiver mesmo Twitter, basta colocar o nome do(a) mesmo(a))

- Tipo: Os valores são `art` para streamers de arte e artesanato e `code` para streamers de ciência e tecnologia


A imagem `black.jpg` é usada para preencher os espaços em falta no mosaico de avatares(banner). Não tem que ser necessariamente preta.

## Scripts
Cada script tem uma funcionalidade, vamos citá-las:

- create_csv.py: Cria o .csv para usar no [site](https://github.com/LiveDivulgador/LiveDivulgador-Site) do LIveDivulgador

- dm_twitter.py: Envia uma mensagem privada no Twitter para todos os streamers no ficheiro `streamers.csv`

- gen_avatar.py: Gera o avatar do LiveDivulgador a partir do ficheiro `streamers_mod.csv`

- gen_banner.py: Gera o banner do LiveDivulgador a partir do ficheiro `streamers_mod.csv`


## Colaboração
Se gostou do projeto e tem interesse em ajudar, pode sempre seguir as contas do bot no Twitter: [@LiveDivulgador](https://twitter.com/LiveDivulgador) e [@LiveDivulgador2](https://twitter.com/LiveDivulgador2)

Dessa forma estará a ajudar o projeto e os streamers divulgados por ele!

Também pode contribuir com código ou mesmo reportando falhas e dando palpites de novas funcionalidades.

Opiniões são sempre bem vindas!