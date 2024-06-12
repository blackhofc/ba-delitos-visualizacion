<!-- Header.svelte -->
<script>
  import Button from './Button.svelte'
</script>

<div class="section">
  <div class="top-container">
    <div style="background-color: #0055aa; width: 120px; height: 80px; display: flex; padding: 8px 16px;">
      <img src="/images/utdt.png" alt="UTDT" style="object-fit: contain; width: 100%; height: 100%;">
    </div>
    <Button/>
  </div>

  <div class="middle-container">
    <h3 class="custom-sub">VISUALIZACION DE DATOS</h3>
    <h1 style="margin-top: 20px; font-size: 100px; color: #130f54">
      DELITOS BUENOS AIRES <br /> <span>2020-2022</span>
    </h1>
  </div>

  <div class="bottom-container">
    <img src="/images/scroll.svg" alt="Scroll SVG" />
    <div class="text-container">
      Deslize hacia abajo para descubrir el Informe anual de los delitos en la
      ciudad en el año 2022.
    </div>
  </div>
</div>

<style>
  .section {
    position: relative;
    background-image: url("/images/background.png");
    background-position: center center;
    width: 100%;
    height: 100%;
    overflow: hidden;
    background-repeat: no-repeat;
    background-size: cover;
    background-color: #FCDE69;
  }

  .custom-sub {
    display: inline-block;
    background-color: #ef404e;
    padding: 4px 8px;
  }

  .top-container {
    margin: 1% 10%;
    display: flex;
    justify-content: space-between;
    flex-direction: row;
    align-items: center;
  }

  .middle-container {
    margin-left: 10%;
    margin-top: 10%;
    display: flex;
    justify-content: space-around;
    flex-direction: column;
    align-items: flex-start;
  }

  .bottom-container {
    position: absolute;
    bottom: 0;
    width: 100%;
    display: flex;
    justify-content: center; /* Centra horizontalmente el contenido del contenedor */
    align-items: center; /* Centra verticalmente el contenido del contenedor */
    padding: 20px;
  }

  .bottom-container img {
    margin-right: 20px; /* Añade espacio entre la imagen y el texto */
  }

  .text-container {
    font-size: 20px;
    color: #000;
    flex: 1; /* Permite que el texto ocupe el espacio restante */
    display: flex;
    align-items: center; /* Centra verticalmente el texto con respecto a la imagen */
    flex-wrap: wrap; /* Permite que el texto se envuelva si es necesario */
    max-width: 450px;
  }
</style>
