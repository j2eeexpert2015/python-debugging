
let score_humain = 0;
let score_ordinateur = 0;

function game(choix_humain)
{   
    let choix_ordinateur = ["pierre", "feuille", "ciseaux"][Math.floor(Math.random() * 3)];

    if (choix_humain == "pierre" && choix_ordinateur == "feuille")
    {
        score_ordinateur = score_ordinateur + 1;
        document.getElementById("score_ordinateur").innerHTML = score_ordinateur;
        document.getElementById('choix_image_humain').src = "/static/"+choix_humain+".gif";
        document.getElementById('choix_image_ordinateur').src = "/static/"+choix_ordinateur+".gif";
    }

    else if (choix_humain == "pierre" && choix_ordinateur == "ciseaux")
    {
        score_humain = score_humain + 1;
        document.getElementById("score_humain").innerHTML = score_humain;
        document.getElementById('choix_image_humain').src = "/static/"+choix_humain+".gif";
        document.getElementById('choix_image_ordinateur').src = "/static/"+choix_ordinateur+".gif";
    }
    else if (choix_humain == "feuille" && choix_ordinateur == "pierre")
    {
        score_humain = score_humain + 1;
        document.getElementById("score_humain").innerHTML = score_humain;
        document.getElementById('choix_image_humain').src = "/static/"+choix_humain+".gif";
        document.getElementById('choix_image_ordinateur').src = "/static/"+choix_ordinateur+".gif";
    }

    else if (choix_humain == "feuille" && choix_ordinateur == "ciseaux")
    {
        score_ordinateur = score_ordinateur + 1;
        document.getElementById("score_ordinateur").innerHTML = score_ordinateur;
        document.getElementById('choix_image_humain').src = "/static/"+choix_humain+".gif";
        document.getElementById('choix_image_ordinateur').src = "/static/"+choix_ordinateur+".gif";
    }

    else if (choix_humain == "ciseaux" && choix_ordinateur == "feuille")
    {
        score_humain = score_humain + 1;
        document.getElementById("score_humain").innerHTML = score_humain;
        document.getElementById('choix_image_humain').src = "/static/"+choix_humain+".gif";
        document.getElementById('choix_image_ordinateur').src = "/static/"+choix_ordinateur+".gif";
    }

    else if (choix_humain == "ciseaux" && choix_ordinateur == "pierre")
    {
        score_ordinateur = score_ordinateur + 1;
        document.getElementById("score_ordinateur").innerHTML = score_ordinateur;
        document.getElementById('choix_image_humain').src = "/static/"+choix_humain+".gif";
        document.getElementById('choix_image_ordinateur').src = "/static/"+choix_ordinateur+".gif";
    }

    else if (choix_humain == choix_ordinateur)
    {
        document.getElementById("score_humain").innerHTML = score_humain;
        document.getElementById("score_ordinateur").innerHTML = score_ordinateur;
        document.getElementById('choix_image_humain').src = "/static/"+choix_humain+".gif";
        document.getElementById('choix_image_ordinateur').src = "/static/"+choix_ordinateur+".gif";
    }
}

function rejouer()
{   
    score_humain = 0;
    score_ordinateur = 0;
    
    document.getElementById("score_ordinateur").innerHTML = score_ordinateur;
    document.getElementById("score_humain").innerHTML = score_humain;

    document.getElementById('choix_image_humain').src = "/static/zero.gif";
    document.getElementById('choix_image_ordinateur').src = "/static/zero.gif";
}