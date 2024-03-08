const express = require('express');
const app = express();
const port = 3000;
const path = require('path');

// Configura el motor de plantillas EJS
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Configurar el middleware para servir archivos estáticos desde la carpeta 'public'
app.use('/styles', express.static(path.join(__dirname, '/styles')));
app.use('/scripts', express.static(path.join(__dirname, '/scripts')));

app.get("/hola", (request, response) => {
    response.send("Hola");
})

app.get('/', (req, res) => {
    // Renderiza el archivo EJS y envía como respuesta
    res.render('index.ejs', { variable: 'Valor de la variable' });
});

app.get('/name', (req, res) => {
    // Renderiza el archivo EJS y envía como respuesta
    res.render('name.ejs');
});

app.listen(port, () => {
    console.log("Puerto expuesto: ", port);
})