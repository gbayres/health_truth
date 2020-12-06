var $btnMenu = document.querySelector("#btn-menu");
var $btnPerguntar = document.querySelector("#btn-perguntar");
var $btnForum = document.querySelector('#btn-forum'); 
var $btnResponder1 = document.querySelector("#btn-responder-1")
var $btnLandscape = document.querySelector("#btn-landscape")
var $formPergunta = document.querySelector(".form-pergunta")
var $btnVoltarForum = document.querySelector("#btn-voltar-forum")
var $indexPerguntaSelecionada = document.querySelector("#index_pergunta_selecionada")

var $pgNumber = document.querySelector("#pg_number")
var $prevBtn = document.querySelector("#prev-btn")
var $nextBtn = document.querySelector("#next-btn")

var $forumMessages = document.querySelectorAll(".forum-message")

var $formResponder = document.querySelector("#form-resposta")
var $forum = document.querySelector("#fórum")

var $vOuF = document.querySelectorAll(".v-ou-f")
    
for (let item of $vOuF){

    if (item.textContent === "Verdadeiro"){
        item.style.color = "green"
    } else{
        item.style.color = "red"
    }

}




$btnResponder1.addEventListener("click", () => {
 
    $formPergunta.classList.add("no-display-mobile")
    $formPergunta.classList.add("no-display-pc")
    
    $forum.classList.add("no-display-mobile")
    $forum.classList.add("no-display-pc")
    
    $formResponder.classList.remove("no-display-mobile")
    $formResponder.classList.remove("no-display-pc")
    
})

$btnVoltarForum.addEventListener("click", () => {

    $formPergunta.classList.add("no-display-mobile")
    $formPergunta.classList.add("no-display-pc")
    
    $forum.classList.remove("no-display-mobile")
    $forum.classList.remove("no-display-pc")
    
    $formResponder.classList.add("no-display-mobile")
    $formResponder.classList.add("no-display-pc")

})


$btnMenu.addEventListener("click", () => {
    closeHeader();
    $formResponder.classList.add("no-display-mobile");
    $formPergunta.classList.add("no-display-mobile");
    $forum.classList.add("no-display-mobile");

})

$btnPerguntar.addEventListener("click", () => {
    closeHeader();
    $formResponder.classList.add("no-display-mobile")
    $formPergunta.classList.remove("no-display-mobile");
    $forum.classList.add("no-display-mobile");
})


$btnForum.addEventListener("click", () => {
    closeHeader();
    $formPergunta.classList.add("no-display-mobile")
    $formResponder.classList.add("no-display-mobile")
    $forum.classList.remove("no-display-mobile")

    })

$btnLandscape.addEventListener("click", () => {
  
    if ($btnLandscape.textContent === "Fórum") {
        $btnLandscape.textContent = "Perguntar";

        $formPergunta.classList.add("no-display-mobile")
        $formPergunta.classList.add("no-display-pc")
        
        $forum.classList.remove("no-display-mobile")
        $forum.classList.remove("no-display-pc")
        
        $formResponder.classList.add("no-display-mobile")
        $formResponder.classList.add("no-display-pc")
    
    } else {
        $btnLandscape.textContent = "Fórum";

        $formPergunta.classList.remove("no-display-mobile")
        $formPergunta.classList.remove("no-display-pc")
        
        $forum.classList.add("no-display-mobile")
        $forum.classList.add("no-display-pc")
        
        $formResponder.classList.add("no-display-mobile")
        $formResponder.classList.add("no-display-pc")
    }
})


function closeHeader(){
    $header = document.querySelector("header");
    $header.classList.toggle("header-closed");
    
    $main = document.querySelector("main");
    $main.classList.toggle("main-opened");

    $navAndFooter = document.querySelector(".nav-and-footer");
    $navAndFooter.classList.toggle("close-nav-and-footer");

}

function abrir_responder(){
    $formResponder.classList.remove("no-display-pc")
    $forum.classList.add("no-display-pc")
    $formPergunta.classList.add("no-display-pc");
    $forum.classList.add("no-display-mobile")
    
}

function mudar(n){

    for (var msg of $forumMessages){
        msg.classList.remove("forum-msg-orange");
        msg.classList.add("forum-msg-blue");
    }


    if ($forumMessages[n - 1].classList.contains("forum-msg-orange")){
        $forumMessages[n - 1].classList.remove("forum-msg-orange");
        $forumMessages[n - 1].classList.add("forum-msg-blue");
    } else{
        $forumMessages[n - 1].classList.add("forum-msg-orange");
        $forumMessages[n - 1].classList.remove("forum-msg-blue");
        $indexPerguntaSelecionada.setAttribute("value", n);
        
    }

    $btnResponder1.removeAttribute("disabled");
}