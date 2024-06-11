<script>
  import SilderTitle from "./SilderTitle.svelte";

  export let title;
</script>

<div class="section">
  <SilderTitle {title} />
</div>

<style>
  .section {
    width: 100%;
    min-height: 100%;
    position: relative;
    overflow: hidden;
  }
</style>
