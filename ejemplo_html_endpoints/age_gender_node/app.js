const express = require('express');
const axios = require('axios');
const app = express();
const port = 3001;

// Post para recibir informacion delicada
// Delete para indicar que se debe de eliminar algo
// GET para obtener informacion
app.get("/recibirNombre", async (req, res) => {
    try{        
        const name = req.query.name;
        const country = "GT";

        const apiUrlGenero = `https://api.genderize.io?name=${name}&country_id=${country}`;
        const apiUrlEdad = `https://api.agify.io?name=${name}&country_id=${country}`;  

        const resultGenero = await axios.get(apiUrlGenero);
        const resultEdad = await axios.get(apiUrlEdad);

        const resultFinal = {
            'resultados_edad': resultEdad.data,
            'resultados_genero': resultGenero.data
        }

        res.status(200).json(resultFinal);
    }catch(error) {
        res.status(400).send("HAy error: " + error.message);
    }    
});

app.listen(port, () => {
    console.log("Servidor en el puerto: ", port);
});