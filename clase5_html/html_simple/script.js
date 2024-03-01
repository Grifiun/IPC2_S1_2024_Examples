// script.js
function multiplicar() {
    // Obtener los valores de los campos de entrada
    var numero1 = parseFloat(document.getElementById("numero1").value);
    var numero2 = parseFloat(document.getElementById("numero2").value);

    // Verificar si los valores son números válidos
    if (isNaN(numero1) || isNaN(numero2)) {
        alert("Por favor, ingrese números válidos.");
        return;
    }

    // Realizar la multiplicación
    var resultado = numero1 * numero2;

    // Mostrar el resultado en el párrafo con id "resultado"
    document.getElementById("resultado").innerText = "Resultado: " + resultado;
}
