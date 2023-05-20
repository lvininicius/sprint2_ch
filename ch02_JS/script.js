function Enviar() {
    let nome = document.getElementsByName("nomeS")[0].value;
    let email = document.getElementsByName("emailS")[0].value;
    let idade = document.getElementsByName("idadeS")[0].value;
    Validar(nome, email, idade);
}

function Validar(nome, email, idade) {
    if (nome === "") {
        alert("Por favor, insira seu nome.");
        return;
    }
    else if (!/^[A-Za-z]+$/.test(nome)) {
        alert("Por favor, insira um nome válido.");
        return;
    }
    else if (email === "") {
        alert("Por favor, insira seu email.");
        return;
    }
    else if (!email.includes("@"||"."))
    {
        alert('Por favor, insira um email válido.');
        return;
    }
    else if (idade === "") {
        alert("Por favor, insira sua idade.");
        return;
    }
    else {
        let info = 'Nome: ' + nome + ' ; Email: ' + email + ' ; Idade: ' + idade;
        console.log(info);
        document.getElementById("final").textContent = info
        var minhaDiv = document.getElementById("final");
        minhaDiv.style.backgroundColor = "lightgreen";
    }
}

function mudarCor() {
    var minhaDiv = document.getElementById("voltar");
    minhaDiv.style.backgroundColor = "red";
  }
function restaurarCor() {
    var minhaDiv = document.getElementById("voltar");
    minhaDiv.style.backgroundColor = "white";
}
