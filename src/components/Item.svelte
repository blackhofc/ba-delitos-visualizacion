<!-- Item.svelte -->
<script>
  export let onClick;
  export let number;
  export let title;
  export let background;
</script>

<main>
  <!-- svelte-ignore a11y-click-events-have-key-events -->
  <!-- svelte-ignore a11y-no-static-element-interactions -->
  <div class="item" style="background-color: {background}" on:click={onClick}>
    <div class="text-container">{number}</div>
    <div class="text-container">{title}</div>
  </div>
</main>

<style>
  .item {
    position: relative;
    z-index: 300;
    padding: 4px 8px;
    cursor: pointer;
    flex: 1; /* Ajustar el tamaño de los elementos para ocupar el espacio disponible */
    margin: 0; /* Eliminar el margen entre elementos */
  }

  .text-container {
    font-size: 20px;
    display: inline-block;
    color: #000;
  }
</style>
