import streamlit as st
from PIL import Image

# Definindo o CSS para remover funções de adm e customização da interface do site
customizando_site = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {
        background: radial-gradient(circle, violet, pink); /* Gradiente rosa-roxo */
        font-family: 'Roboto', sans-serif; /* Aplicando a fonte Roboto */
    }
    .nome {
        text-align: center; /* Centraliza o texto */
        font-size: 24px; /* Tamanho do texto dos nomes */
        color: #C71585; /* Cor do texto em rosa escuro */
        background-color: rgba(255, 255, 255, 0.5); /* Cor de fundo branca com 50% de transparência */
        padding: 3px; /* Espaçamento interno da caixa reduzido */
        border-radius: 5px; /* Bordas arredondadas */
        margin: 3px; /* Margem reduzida */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Sombra para destacar */
    }
    .imagem-container {
        display: flex;
        flex-direction: column;
        align-items: center; /* Centraliza horizontalmente */
        justify-content: center; /* Centraliza verticalmente */
        margin: 20px 0; /* Espaçamento entre cada contêiner */
    }
    .titulo {
        color: white; /* Cor do texto do título */
        font-size: 4vw; /* Tamanho responsivo do texto do título */
        text-align: center; /* Centraliza o texto */
        text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.6); /* Sombra para o título */
        border-bottom: 4px solid #C71585; /* Linha embaixo do título */
        padding-bottom: 5px; /* Espaçamento abaixo do título */
        width: 100%; /* Largura total */
        margin: -20px 0 0 0; /* Margens */
    }
    .descricao {
        color: #C71585; /* Cor rosa escuro */
        font-size: 13px; /* Tamanho do texto da descrição */
        text-align: center; /* Centraliza o texto */
        margin-top: 10px; /* Margem superior */
        padding: 0 1%; /* Espaçamento nas laterais */
    }
    </style>
    """

# Aplicando o CSS
st.markdown(customizando_site, unsafe_allow_html=True)

# Definição do título centralizado
st.markdown(
    """
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: column; width: 100%;">
        <h1 class='titulo'>
            A Influência das Mulheres Gonçalenses na Construção Identitária da Sociedade
        </h1>
        <p class='descricao'>
            Este site foi criado para destacar mulheres que, com suas ações e exemplos, impactaram profundamente a vida das pessoas ao seu redor. Aqui, nosso objetivo é enfatizar as contribuições dessas mulheres de São Gonçalo na formação das identidades.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Função para exibir a legenda com estilo
def styled_caption(text):
    # Separar a legenda em duas partes: antes e depois do "-"
    parts = text.split(" - ")
    if len(parts) == 2:
        first_part = parts[0]
        second_part = parts[1]
        # Parte após o "-"
        return f"<span style='color: white; font-size: 23px;'>{first_part}<br><span style='color: black; font-size: 18px;'>{second_part}</span></span>"
    return f"<span style='color: white; font-size: 23px;'>{text}</span>"

# Nomes e imagens
images = {
    "Maria de Fátima": "IMAGES.SITE/Maria de Fátima.jpg",
    "Sheila Mota": "IMAGES.SITE/Sheila.jpg",
    "Isabella Medeiros": "IMAGES.SITE/Isabella.jpg",
    "Monica Parente": "IMAGES.SITE/Monica.jpg",
    "Vanessa Peçanha": "IMAGES.SITE/Vanessa.jpg",
    "Carol Lydia": "IMAGES.SITE/Carol.jpg",
    "Nathália Precioso": "IMAGES.SITE/Nathália.jpg",
    "Aline Menezes": "IMAGES.SITE/Aline.jpg",
    "Dona Beta": "IMAGES.SITE/Beta.jpg",
    "Cynthia Sampaio": "IMAGES.SITE/Cynthia.jpg",
    "Lara Nantes": "IMAGES.SITE/Lara.jpg",
    "Denise Soares": "IMAGES.SITE/Denise.jpg",
    "Lilian": "IMAGES.SITE/Lilian.jpg",
    "Ana Suelen": "IMAGES.SITE/Ana Suelen.jpg",
    'Ana Paula': "IMAGES.SITE/Ana Paula.jpg",
    "Stella": "IMAGES.SITE/Stella.jpg",
    "Silvia Maria": "IMAGES.SITE/Silvia.jpg",
    "Priscila Moscoso": "IMAGES.SITE/Priscila.jpg",
    "Daniele Sampaio": "IMAGES.SITE/Daniele.jpg",
    "Marilda Porto": "IMAGES.SITE/Marilda.jpg",
    "Roberta": "IMAGES.SITE/Roberta.jpg",
    "Elizangela Cunha": "IMAGES.SITE/Elizangela.jpg",
    "Elaine Silva": "IMAGES.SITE/Elaine.jpg",
    "Leandra": "IMAGES.SITE/Leandra.jpg",
    "Evelyn Sesconi": "IMAGES.SITE/Evelyn.jpg",
    "Rafaella": "IMAGES.SITE/Rafaella.jpg",
    "Maria Albêrtina": "IMAGES.SITE/Maria Albêrtina.jpg",
    "Alvanira Mota": "IMAGES.SITE/Alvanira.jpg",
    "Maria José": "IMAGES.SITE/Maria José.jpg",
    "Rana Victória": "IMAGES.SITE/Rana.jpg",
    "Kelly Francisco": "IMAGES.SITE/Kelly.jpg",
    "Gisele Vale": "IMAGES.SITE/Gisele.jpg",
    "Michele Andrade ": "IMAGES.SITE/Michele.jpg",
    "Paula Renata": "IMAGES.SITE/Paula.jpg",
    "Renata Dias": "IMAGES.SITE/Renata.jpg",
    "Sabrina de Paula": "IMAGES.SITE/Sabrina.jpg",
    "Mirian de Castro": "IMAGES.SITE/Mirian.jpg",
    "Adriana Marinho": "IMAGES.SITE/Adriana.jpg",
    "Mariza Guimarães": "IMAGES.SITE/Mariza.jpg",

}

# Legendas correspondentes
captions = {
    "Maria de Fátima": "“O verdadeiro significado de gentileza e bondade, pois ela está sempre ajudando todos a sua volta, e isso me inspira a ser como ela.” - ~ Ana Beatriz Xavier (2003)",
    "Sheila Mota": "“Me mostrou o que é amor e foi capaz de ir muito longe apenas por me amar. Nunca conheci alguém mais forte que ela, e com um nome tão lindo.” - ~ Ana Clara Mota (2003)",
    "Isabella Medeiros": "“Me ensinou que sempre existe outra chance,outro caminho e outra oportunidade. Me inspira a seguir aquilo que acredito sem medo do que os outros podem pensar. Além de me ensinar que família não precisa ser necessariamente alguém de sangue.“ - ~ Beatriz Salgado (2003)",
    "Monica Parente": "“A mulher que me ensinou que a vida é muito melhor se tivermos um olhar mais gentil.” - ~ Lívia Parente (1003)",
    "Vanessa Peçanha": "“Trabalhou muito quando eu era criança, para que não faltasse comida em casa, me mostrando o que é ser uma mulher batalhadora de verdade.” - ~ Poliana Peçanha (2003)",
    "Carol Lydia": "“A mulher que me mostrou a força do poder feminino, uma das pessoas mais fortes que já conheci e que vou levar para a vida todo o conhecimento que me passou.” - ~ Poliana Peçanha (2003)",
    "Nathália Precioso": "“Me ensinou a acreditar nos meus sonhos e que tudo é possível, basta você acreditar, também que só quem sonha consegue alcançar, ela é minha inspiração de carreira.” - ~ Júlia Azeredo (3004)",
    "Aline Menezes": "“Minha professora que me ensinou, que sempre devemos acreditar em nós mesmos e não desistir do que almejamos” - ~ Pedro Henrique (3004)",
    "Dona Beta": "“Cuidou de mim nos momentos que eu mais precisei.” - ~ Laís Rocha (2003)",
    "Cynthia Sampaio": "“Me ensinou que vencer o câncer é acreditar na vida, mesmo quando o corpo fraqueja.” - ~ Luísa Sampaio (2003)",
    "Lara Nantes": '“Me ensinou a ser verdadeiro com os outros e a poder confiar nas pessoas, me mostrou que é muito mais que uma madrinha mas uma mãe para mim também!” - ~ Filipe Duarte (1002)',
    "Denise Soares" : "“A alma mais bondosa que eu já conheci na vida. Me ensinou e me ensina todos os dias que a humildade e a bondade são as melhores virtudes que alguém pode ter.” - ~ Maria Eduarda (2003)",
    "Lilian" : "“Ela sempre foi um exemplo vivo de mulher batalhadora e de cristã sendo a única mulher dentro de casa. Agradeço a ela por ter sido uma luz em minha jornada. “ - ~ Diego (3002)",
    "Ana Suelen" : '“A mulher que me inspira todos os dias com sua força e dedicação e que transforma desafios em lições de vida. “ - ~ Ester (3006)',
    "Ana Paula" : '“Me ensinou que ser forte não é nunca cair, mas sempre se levantar e seguir em frente, mesmo quando tudo parece difícil.” - ~ Ana Beatriz Xavier (2003)',
    "Stella" : '“Inspirou gerações de alunos com sua dedicação ao ensino e amor pela educação.” - ~ Miguel Maia (2003)',
    'Silvia Maria' : '“Terminou seus estudos com 61 anos e era a mais velha da sua sala. E ainda, realizou o curso técnico dos seus sonhos, enfermagem. Deixou um legado para todos os seus familiares e amigos que nunca é tarde para tentar e ir atrás do seu sonho.” - ~ Luisa Teixeira (3002)',
    'Priscila Moscoso' : '“Que me ensinou a crer em mim e na minha capacidade de governar o meu futuro.“ - ~ Sophia Moscoso (3006)',
    'Daniele Sampaio' : 'Me ensinou que ser forte é abraçar a fragilidade, mas nunca deixar que ela defina quem somos.” - ~ Luísa Sampaio (2003)',
    'Marilda Porto' : '“Esta mulher me ensinou as principais coisas da vida. Graças a ela aprendi a ter educação com o próximo e que devo ser uma boa pessoa para todos, independente do que aconteça.” - ~ Lara Porto (1003)',
    'Roberta': '“Me ensinou muito sobre persistência, pois mesmo lidando com diversos problemas de saúde nunca deixou de trabalhar para me dar uma boa qualidade de vida.” - ~ Fabiane (3006)',
    "Elizangela Cunha": '“Me ensinou a ser amorosa!” - ~ Khemeronn Sophia (1003)',
    "Elaine Silva": '“Me formou como pessoa e me ensinou que amor não é só falando mas também pode ser demonstrado com ações” - ~ Pedro Henrique (3004)',
    "Leandra": '“Me ensinou a ser a pessoa que eu sou hoje e cuidou de mim para que eu nunca passasse por maus momentos.” - ~ Laís Rocha (2003)',
    "Evelyn Sesconi": '“Me ensinou a fé e o valor de cada vida. Além de me mostrar que devemos persistir em algo queremos. A cada dia me ensina mais sobre o valor da família.“ - ~ Beatriz Salgado (2003)',
    "Rafaella": '“Ela me ensinou que eu não devo deixar de ser quem sou para agradar os outros.” - ~ Arthur Rocha (2004)',
    "Maria Albêrtina": '“Me ensinou que saudade é o amor que permanece, mesmo quando a presença se transforma em lembrança.” - ~ Luísa Sampaio (2003)',
    "Alvanira Mota": '”Me fez entender que a nossa trajetória é responsável por quem somos, então precisamos ser sensatos.” - ~ Ana Clara Mota (2003)',
    "Maria José": '“Me ensinou que podem tirar tudo da gente menos o conhecimento.” - ~ Ana Clara Souza (2003)',
    "Rana Victória": '“Por ter crescido comigo, me mostrou o quanto somos responsáveis pela identidade uma da outra.” - ~ Ana Clara Mota (2003)',
    "Kelly Francisco": '“Ela sempre acreditou no meu potencial!” - ~ Vinícius (2003)',
    "Gisele Vale": '“Sua resiliência e coragem são inspirações diárias para mim. Te ver vestida de noiva é a prova que Deus sempre nos honra na hora certa. Sempre por ti, te amo pra sempre!“ - ~ Kaylla (2001)',
    "Michele Andrade ": '“A única pessoa que se doa literalmente todos os dias por mim, a pessoa que fez eu me tornar a pessoa que sou hoje, trabalhando desde os 14 anos sempre empenhada, enfim te amo mãe .” - ~ João Pedro (2003)',
    "Paula Renata": '“Me ensinou a cuidar dos outros e saber se colocar no lugar do outro, não sei o que seria de mim sem os ensinamentos dela!” - ~ Filipe Duarte (1002)',
    "Renata Dias": '“A mulher mais forte que eu conheço. Sempre me impulsionando e me ensinando a persistir diante das adversidades da vida.“ - ~ Maria Eduarda (2003)',
    "Sabrina de Paula": '“Me ensinou um homem respeitoso e me ensinou o conceito de família, sou grato por ela. “ - ~ Miguel De Paula (2003)',
    "Mirian de Castro": '“Enfrenta a mais de 6 anos a batalha contra o câncer de mama.” - ~ Maria Clara (2001)',
    "Adriana Marinho": '“Tia e mãe incrível que entre todos os ensinamentos importantes, me ensinou a importância do amor.” - ~ Samuel (2003)',
    "Mariza Guimarães": '“Me ensinou a liberdade e a felicidade. Me ensinou a beleza de um amor de vó.“ - ~ Beatriz Salgado (2003)',
}

# Exibindo as imagens e legendas em uma única coluna
for name, path in images.items():
    # Criar um contêiner para centralizar o nome e a imagem
    st.markdown("<div class='imagem-container'>", unsafe_allow_html=True)
    st.markdown(f"<div class='nome'>{name}</div>", unsafe_allow_html=True)  # Exibindo o nome com estilo
    try:
        image = Image.open(path)
        st.image(image, caption="", width=150, use_column_width=True)
    except Exception as e:
        st.error(f"Erro ao carregar a imagem: {e}")

    st.markdown(styled_caption(captions[name]), unsafe_allow_html=True)  # Legenda na mesma coluna
    st.markdown("</div>", unsafe_allow_html=True)  # Fechar o contêiner

# Adiciona um espaço entre as linhas
st.markdown("<br>", unsafe_allow_html=True)


