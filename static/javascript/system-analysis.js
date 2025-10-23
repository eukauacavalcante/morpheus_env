async function getSystemMetrics() {
    let request = await fetch('api/v1/metrics')
    let response = await request.json()

    document.getElementById('cpu').innerHTML = `<p class="text-green-400 font-semibold">${response.data.cpu_percent} %</p>`
    document.getElementById('ram').innerHTML = `<p class="text-green-400 font-semibold">${response.data.ram_percent} % | ${response.data.ram_used} GB</p>`
    document.getElementById('ram-total').innerHTML = `<p class="text-green-400 font-semibold">${response.data.ram_total} GB</p>`
    document.getElementById('memory').innerHTML = `<p class="text-green-400 font-semibold">${response.data.memory_used} GB</p>`
    document.getElementById('total-memory').innerHTML = `<p class="text-green-400 font-semibold">${response.data.memory_total} GB</p>`
}

async function aiAnalysis() {
    const button = document.getElementById('btn')
    const result_ai = document.getElementById('ai_analysis')

    button.disabled = true
    button.innerText = 'Carregando..'
    result_ai.innerHTML = '<p class="text-xl text-yellow-500">A IA está analisando...</p>'

    try {
        const request_ai = await fetch('api/v1/ai')
        if (!request_ai.ok) {
            throw new Error(`Erro na API: ${request_ai.statusText}`);
        }
        const response_ai = await request_ai.json()
        result_ai.innerHTML = `<p class="text-xl text-white">${response_ai.ai}</p>`
    } catch (error) {
        console.error('Erro na API: ', error)
        document.getElementById('ai_analysis').innerHTML = '<p class="text-xl text-red-500">A análise por IA está indisponível no momento :(<br>Possível manutenção ocorrendo no sistema. Tente mais tarde!</p>'
    } finally {
        button.innerText = 'Análise gerada'
        button.disabled = true
    }
}

getSystemMetrics()
setInterval(getSystemMetrics, 5000)
