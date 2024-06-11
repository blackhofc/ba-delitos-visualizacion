<script>
    // Aquí puedes manejar la lógica de tu botón si es necesario
</script>

<style>
    .button {
        display: inline-block;
        padding: 10px 20px;
        color: white;
        background-color: #E74C3C; /* Rojo */
        text-decoration: none;
        font-weight: bold;
        z-index: 1;
        box-shadow: 5px 5px 0 #34495E; /* Sombra para simular el desplazamiento */
        cursor: pointer;
    }

    .container {
        display: inline-block;
        padding: 10px;
    }

    .container::before {
        content: "";
        display: block;
        position: absolute;
        top: 5px; 
        left: 5px;
        width: 100%;
        height: 100%;
        background-color: #34495E; /* Azul oscuro */
        z-index: -1;
    }
</style>

<div class="container">
    <a href="https://www.linkedin.com/in/bjtoledo" class="button">Visitar Linkedin</a>
</div>
