const button = document.querySelector("button");
const inputNome = document.querySelector("#nome")
const inputEmail = document.querySelector("#email")
const pMensagem = document.createElement('p')


function clearForm() {
    inputNome.value = ""
    inputEmail.value = ""
}

button.addEventListener("click", function(event){
    event.preventDefault()

    // validacao

    if(inputNome.value.trim() === ""){
        pMensagem.textContent = "*Campo Obrigatorio"
        inputNome.insertAdjacentElement("afterend", pMensagem)
        pMensagem.setAttribute("class", "erro")

        return false
    }

    if(inputEmail.value.trim() === ""){
        pMensagem.textContent = "*Campo Obrigatorio"
        inputEmail.insertAdjacentElement("afterend", pMensagem)
        pMensagem.setAttribute("class", "erro")

        return false
    }

    // logica


    pMensagem.classList.add("esconder")
    clearForm()
})


