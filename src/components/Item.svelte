<!-- Item.svelte -->
<script>
  export let onClick;
  export let number;
  export let title;
  export let background;
  export let text;
</script>

<main class="item" style="background-color: {background};" on:click={onClick}>
  <!-- svelte-ignore a11y-click-events-have-key-events -->
  <!-- svelte-ignore a11y-no-static-element-interactions -->
  <h2 class="text-container" style="color: {text};">{number}</h2>
  <div class="text-container" style="margin-left: 8px; color: {text};">{title}</div>
</main>

<style>
  .item {
    position: relative;
    z-index: 300;
    padding: 4px 8px;
    cursor: pointer;
    flex: 1; /* Ajustar el tamaño de los elementos para ocupar el espacio disponible */
    margin: 0; /* Eliminar el margen entre elementos */
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    /* border-top: 2px solid black;  Add a black line on the top */
  }

  .text-container {
    font-size: 20px;
    display: inline-block;
    color: red;
  }
</style>
