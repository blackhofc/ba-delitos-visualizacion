<!-- Item.svelte -->
<script>
  import { format } from "../utils/functions";

  export let counter;
  export let title;

  // Función para animar el contador
  function animateCounter(targetValue) {
    const duration = 1000; // Duración de la animación en milisegundos
    const interval = 10; // Intervalo entre cada paso de la animación en milisegundos
    const increment = targetValue / (duration / interval); // Incremento en cada paso de la animación

    let currentValue = 0; // Valor actual del contador
    const intervalId = setInterval(() => {
      currentValue += increment;
      if (currentValue >= targetValue) {
        currentValue = targetValue;
        clearInterval(intervalId);
      }
      // Actualiza el título con el valor actual redondeado
      counter = format(Math.round(currentValue));
    }, interval);
  }

  // Llama a la función de animación cuando el componente se monta
  animateCounter(counter);
</script>

<main>
  <div class="item-stat">
    <h1 class="title">{counter}</h1>
    <div class="text-container">{title}</div>
  </div>
</main>

<style>
  .title {
    font-size: 70px;
    display: inline-block;
    color: #000;
  }

  .text-container {
    font-size: 20px;
    display: inline-block;
    color: #000;
  }

  .item-stat {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 8px;
    margin: 4px 4px;
  }
</style>
