<h1>HealthTruth</h1>

<p>Repositório de uma aplicação web produzida para o Hackathon Visagio com o intuito de identificar FakeNews.</p>
<h2>A ideia</h2>
<p>O aplicativo consiste em um fórum em que pacientes podem tirar dúvidas com médicos quanto à veracidade de informações. Enquanto aguardam a resposta de um médico, um algoritmo de inteligência artificial prediz a veracidade. Logo que um médico responder, a predição é substituida por um veredito.</p>
<p>Seguem alguns links para auxiliar na melhor compreensão da ideia: </p>
<ul>
  <li>Link do aplicativo (dynos podem estar desativados): https://healthtruth.herokuapp.com/</li>
  <li>PDF explicativo: https://drive.google.com/file/d/1oGwvAnjhUfaU3rHSAHvCjAEKKJX2olUo/view?usp=sharing</li>
  <li>Pitch: https://www.youtube.com/embed/e5lj4ZXdcLE</li>
</ul>
<h2>Agradecimentos iniciais</h2>
  <p>Agradeço aos demais membros da equipe - Giovanna Gennari, Juliano Amadeu e Vitor Motta dos Santos - por auxiliarem em alguns pontos da criação do PDF e no planejamento do pitch.</p>
<h2>Explicação do funcionamento</h2>
  <h3>No celular</h3>
  <ol>
  <li>Clique no botão "Perguntar" para criar uma nova pergunta.</li>
  <li>Na lacuna "Pergunta", insira uma dúvida relativa à notícia que será apresentada.</li>
  <li>Na lacuna "Notícia", insira a notícia a ter sua predição realizada.</li>
  <li>Clique em "Enviar" para submeter a pergunta.</li>
  <li>Volte ao menu principal e clique em "Fórum".</li>
  <li>Selecione a pergunta que você submeteu.</li>
  <li>Você irá perceber que uma predição foi dada, que será um "placeholder" até uma resposta médica definitiva.</li>
  <li>Clique em responder.</li>
  <li>Insira os dados de um médico fictício e responda à pergunta.</li>
  <li>Selecione um veredito e submeta.</li>
  <li>Ao voltar à seção "Fórum", você irá perceber que a predição foi substituída pelo veredito. Esse veredito irá para a base de dados juntamente com a notícia, para aprimorar o algoritmo.</li>
  </ol>
  
  <h3>No computador</h3>
  <p>O funcionamento é semelhante ao celular, porém não há menu principal. A seçao perguntas já aparece de imediato.</p>
  
  
<h2>Explicação da árvore</h2>
<h3>Pasta principal</h3>
<p>Dentro da pasta principal, a pasta "env" e os demais arquivos são referentes ao ambiente virtual Python e aos pré-requisitos para que o micro-framework Flask rode no servidor.</p>
<h3>Pasta "app"</h3>
<p>Dentro da pasta "app", o módulo "views.py" cria as rotas da aplicação web e "predict.py" roda o algoritmo Naive Bayes e adiciona novas entradas à base de treino.</p>
<p>As pastas static e templates contêm os arquivos HTML/CSS/JS usados no FrontEnd.</p>
<h4>Pasta "database"</h4>
<p>A pasta "database" contém 3 arquivos:</p>
<ul>
  <li>"base_para_predicao.csv" armazena os dados que serão utilizados pelo Naive Bayes.</li>
  <li>"dados.csv" armazena os dados referentes às perguntas dos pacientes.</li>
  <li>"respostas.csv" armazena os dados referentes às respostas dos médicos.</li>
</ul>
<h5>Pasta "processDatabase"</h5>
<p>Contém 2 arquivos</p>
 <ul>
  <li>"aosFatos.py" pega as informações necessárias da base de dados do Aos Fatos fornecida pela Visagio.</li>
  <li>"factChecker.py" utiliza a API Fact Checker do Google para mais de 100 palavras-chave citadas nos títulos da base FakeHealthData.</li>
 </ul>

<img style="width: 200px;" src="https://raw.githubusercontent.com/medcompunicamp/healthtruth/master/app/static/img/logo.svg" alt="HealthTruth">
