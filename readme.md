<h1> Criando um portifólio de pequenos projetos </h1>

<h3>Projeto Nuvem de Palavras </h3>
<p>Esse projeto foi feito para pegar relatórios em PDF e gerar uma nuvem de palavras para auxiliar na analise destes.</p>
<p>Esse projeto foi feito em jupyter notebook usando python e usou as seguintes bibliotecas: </p>
<ul>
<li>wordcloud</li>
<li>fitz</li>
<li>matplotlib.pyplot</li>
<li>matplotlib.color (Pra usar as cores da logo da empresa)</li>
<li>os</li>
</ul>
<p>Talvez seja necessário instalar algumas das bibliotecas, rode os codigos abaixo para isso:</p>

```
! pip install pymupdf
! pip install wordcloud
```

<h3>Classificador Oftalmologia</h3>
<p>Separa procedimentos médicos que são referentes a oftalmologia de outras especialidades. <br/> 
Foi feito para acelerar os relatórios de agendas ofertadas ao SUS.
</p>


<h3>Machine Learning para prever a sobrevivencia no Titanic</h3>
<p>Desafio do Kaggle que usa Random Forest para tentar prever se uma pessoa sobreviveria ao naufragio do Titanic.</p>
<ul>
<li>pandas</li>
<li>statistics</li>
<li>RandomForestClassifier do sklearn.ensemble</li>
<li>accuracy_score, confusion_matrix, classification_report do sklearn.metrics</li>
<li>train_test_split do sklearn.model_selection</li>
</ul>


<h3>F1 rede neural</h3>
<p>Feito para o TCC de Data Science e Analytics da USP<br/> 
O intuito era prever o grid de largada de monza 2024. Porém devido a poucas informações e a competitividade da F1 não foi possível prever corretamente, porém o erro do tempo previsto é de menos de 5% (ou 4 segundos), porém é muito para um F1 onde o primeiro e o ultimo estão em uma diferença de 1 segundo
</p>
