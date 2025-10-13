async function converter() {
    const value = document.getElementById('value').value.trim();
    const type = document.getElementById('type_converter').value;
    const resultElement = document.getElementById('result_converter');
    const button = document.getElementById('converterBtn');

    if (!value) {
        resultElement.innerHTML = `<span class="text-red-400">Por favor, digite um valor para converter.</span>`;
        return;
    }

    button.disabled = true;
    button.innerHTML = 'Calculando...';
    resultElement.innerHTML = `<span class="text-gray-400">Processando...</span>`;
    
    try {
        const request = await fetch(`v1/api/?value=${value}&type=${type}`);
        if (!request.ok) {
            throw new Error(`Erro na API: ${request.statusText}`);
        }
        const data = await request.json();
        resultElement.innerHTML = `<strong>Resultado:</strong>&nbsp; <span class="text-green-400">${data.result}</span>`;
    } catch (error) {
        console.error("Falha na conversão:", error);
        resultElement.innerHTML = `<span class="text-red-400">Ocorreu um erro. Verifique o valor e tente novamente.</span>`;
    } finally {
        button.disabled = false;
        button.innerHTML = 'Calcular';
    }
}

async function boolean() {
    const value1 = document.getElementById('value1').value.trim();
    const value2 = document.getElementById('value2').value.trim();
    const type = document.getElementById('type_boolean').value;
    const resultElement = document.getElementById('result_boolean');
    const button = document.getElementById('booleanBtn');
    
    if (!value1 || !value2) {
            resultElement.innerHTML = `<span class="text-red-400">Ambos os valores são obrigatórios.</span>`;
            return;
    }
    if (!['0', '1'].includes(value1) || !['0', '1'].includes(value2)) {
        resultElement.innerHTML = `<span class="text-red-400">Por favor, insira apenas 0 ou 1.</span>`;
        return;
    }

    button.disabled = true;
    button.innerHTML = 'Calculando...';
    resultElement.innerHTML = `<span class="text-gray-400">Processando...</span>`;

    try {
        const request = await fetch(`v1/api/?type=${type}&value1=${value1}&value2=${value2}`);
            if (!request.ok) {
            throw new Error(`Erro na API: ${request.statusText}`);
        }
        const data = await request.json();
        resultElement.innerHTML = `<strong>Resultado:</strong>&nbsp; <span class="text-green-400">${data.result}</span>`;
    } catch (error) {
        console.error("Falha na operação lógica:", error);
        resultElement.innerHTML = `<span class="text-red-400">Ocorreu um erro ao calcular.</span>`;
    } finally {
        button.disabled = false;
        button.innerHTML = 'Calcular';
    }
}