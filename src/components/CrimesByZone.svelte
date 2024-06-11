<script>
  import SilderTitle from "./SilderTitle.svelte";

  export let title;
</script>

<div class="section">
  <SilderTitle {title} />
  <div class="map-view">
    <script
      type="text/javascript"
      defer
      src="https://datawrapper.dwcdn.net/AoY5F/embed.js?v=1"
      charset="utf-8"
    ></script>
    
  </div>
</div>

<style>
  .section {
    width: 100%;
    position: relative;
    display: flex;
    overflow: hidden;
    flex-direction: column;
    height: 100vh; /* Ajusta según el contenedor padre o viewport */
  }

  .map-view {
    position: relative;
    flex-grow: 1;
    margin: 0; /* Eliminamos el margen para evitar que corte el contenido */
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .map-view script, .map-view img {
  }
</style>
