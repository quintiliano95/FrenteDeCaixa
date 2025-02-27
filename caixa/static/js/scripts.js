function cadastrarCliente() {
    let nome = document.getElementById("id_nome").value;
    let cpf = document.getElementById("id_cpf").value;
    let telefone = document.getElementById("id_telefone").value;
    let email = document.getElementById("id_email").value;
    let endereco = document.getElementById("id_endereco").value;

    $.ajax({
        url: "/cadastrar_cliente/",
        type: 'POST',
        contentType: 'application/json',
        headers: { "X-CSRFToken": $('input[name=csrfmiddlewaretoken]').val() },  // Pega o CSRF corretamente
        data: JSON.stringify({
            nome: nome,
            cpf: cpf,
            telefone: telefone,
            email: email,
            endereco: endereco
        }),
        success: function(response) {
            console.log("Cliente cadastrado com sucesso!", response);
            Swal.fire({
                icon: 'success',
                title: 'Sucesso!',
                showCloseButton: true,
                text: response.message || 'Cliente cadastrado com sucesso!',
                timer: 5000,  // 5000 ms = 5 segundos
                timerProgressBar: true,  // Exibe uma barra de progresso no modal
            });
            $("#formCadastro")[0].reset();
        },
        error: function(xhr) {
            let errorMessage = "Ocorreu um erro ao cadastrar o cliente.";
            try {
                let errorResponse = JSON.parse(xhr.responseText);
                if (errorResponse.message) {
                    errorMessage = errorResponse.message;
                }
            } catch (e) {
                console.error("Erro ao processar resposta do servidor:", e);
            }

            Swal.fire({
                icon: 'error',
                title: 'Erro!',
                text: errorMessage,
                timer: 5000,  // 5000 ms = 5 segundos
                timerProgressBar: true,
            });
        }
    });
}


// Função para pegar o token CSRF
function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}