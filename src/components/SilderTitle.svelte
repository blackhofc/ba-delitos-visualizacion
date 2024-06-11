<!-- Item.svelte -->
<script>
  export let title;
</script>

<main>
  <div class="slider-container">
    <div class="slider">
      <div class="slide">{title}</div>
    </div>
  </div>
</main>

<style>
  .slider-container {
    width: 100%;
    overflow: hidden;
  }

  .slider {
    white-space: nowrap;
  }

  .slide {
    font-style: bold;
    color: rgba(255, 255, 255, 0.233);
    display: inline-block;
    font-size: 15vw; /* Ajusta el tamaño del texto según sea necesario */
    padding-right: 20px; /* Espaciado entre el final del texto y el comienzo del mismo */
    animation: slide 100s linear infinite; /* Controla la velocidad del desplazamiento cambiando el valor de 50s */
  }

  @keyframes slide {
    0% {
      transform: translateX(0); /* Comienza en su posición inicial */
    }
    50% {
      transform: translateX(-100%); /* Llega al final de la pantalla */
    }
    100% {
      transform: translateX(0); /* Rebota y vuelve hacia atrás */
    }
  }
</style>
