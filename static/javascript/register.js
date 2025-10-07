document.addEventListener('DOMContentLoaded',
function () {
    const form = document.getElementById('form-register')
    const btn = document.getElementById('btn-register')

    form.addEventListener('submit', function() {
        btn.disabled = true
        btn.innerText = 'Carregando...'
    })
})
