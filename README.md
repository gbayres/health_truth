
Repositório de uma aplicação web produzida para o Hackathon Visagio com o intuito de identificar FakeNews.

Acesse o aplicativo em: https://healthtruth.herokuapp.com/

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
