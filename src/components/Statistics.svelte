<script>
  import ItemStatistic from "./ItemStatistic.svelte";
  import dataset from "../data/delitos.json";

  import { format } from "../utils/functions";

  let parsedStats = [];
  let currentHood = "RECOLETA";

  var totalHood = format(dataset.barrio[currentHood]["Robo"]);
  var totalCity = format(dataset.general["Robo"]);

  var percent = ((totalHood / totalCity) * 100).toFixed(2);

  Object.keys(dataset.general).forEach((kind) => {
    parsedStats.push({
      counter: dataset.general[kind],
      title: kind,
    });
  });

  export let title;
</script>

<div class="section">
  <div class="stats-container">
    {#each parsedStats as s}
      <ItemStatistic counter={s.counter} title={s.title} />
    {/each}
  </div>

  <div class="sub-text" style="margin-top: 64px;">
    {totalHood} Robos ocurren en <strong>{currentHood}</strong>, representando
    un {percent}% de los robos de la ciudad
  </div>
</div>

<style>
  .section {
    width: 100%;
    min-height: 100%;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 0px 16px;
  }

  .stats-container {
    height: auto;
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    align-items: center;
  }

  .sub-text {
    font-size: 50px;
    display: inline-block;
    color: #000;
    text-align: center;
  }
</style>
