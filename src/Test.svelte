<script>
  import { slide } from "svelte/transition";
  import Scroller from "@sveltejs/svelte-scroller";
  import { onMount } from "svelte";
  import * as d3 from "d3";

  import Item from "./components/Item.svelte";
  import Section from "./components/Section.svelte";
  import Header from "./components/Header.svelte";
  import SilderTitle from "./components/SilderTitle.svelte";

  let count;
  let index;
  let offset;
  let progress;
  let top = 0;
  let threshold = 0;
  let bottom = 0.9;

  let showing_sections = false;
  let last_prog;

  let sections = [
    { title: "Estadísticas", color: "#FCDE69", pos: 0 },
    { title: "Barrios Calientes", color: "#A2DAE2", pos: 0 },
    { title: "Delitos Por Barrio", color: "#A6D6B4", pos: 0 },
    { title: "Distribución Temporal", color: "#F8BCAD", pos: 0 },
    { title: "Tasa de Mortalidad", color: "#EE404D", pos: 0 },
    { title: "Zonas Seguras", color: "#0054A8", pos: 0 },
    { title: "Conclusiones", color: "#130F52", pos: 0 },
  ];

  let backgroundColor = "#000";

  function updateBackgroundColor(color) {
    backgroundColor = color;
  }

  function scrollToSection(index) {
    const sectionElement = document.querySelectorAll(".step_foreground")[index];
    if (sectionElement) {
      sectionElement.scrollIntoView({ behavior: "smooth" });
    }
  }

  onMount(() => {
    /* d3.csv("./data/deportistas.csv", d3.autoType).then((data) => {
      deportistas = data;
      filteredDeportistas = deportistas;
    }); */
    // scrollToSection(4);
  });

  $: {
    if (!last_prog || (progress < last_prog && !showing_sections)) {
      showing_sections = true;
    } else if (progress >= last_prog && showing_sections) {
      showing_sections = false;
    }

    last_prog = progress;

    // console.log({ index });
    updateBackgroundColor(sections[index]?.color || "#ffffff");

    /* switch (index) {
      case 0:
        filteredDeportistas = deportistas;
        break;
      case 1:
        filteredDeportistas = deportistas.filter((d) => d.genero === "F");
        break;
      case 2:
        filteredDeportistas = deportistas.filter((d) => d.genero === "M");
        break;
      case 3:
        filteredDeportistas = deportistas.filter(
          (d) => d.continente === "América"
        );
        break;
      default:
        filteredDeportistas = deportistas; 
    }*/
  }
</script>

{#if showing_sections}
  <div
    class="sections-container"
    style="display: flex; z-index: 200; bottom: 0; background-color: #000000; position: fixed; height: auto; width: 100%; justify-content: space-between;"
    transition:slide
  >
    {#each sections as section, index}
      <Item
        onClick={() => scrollToSection(index + 1)}
        number={index + 1}
        title={section.title}
        background={section.color}
      />
    {/each}
  </div>
{/if}

<main>
  <Scroller
    {top}
    {threshold}
    {bottom}
    bind:count
    bind:index
    bind:offset
    bind:progress
  >
    <div
      slot="background"
      class="scroller"
      style="--background-color: {backgroundColor}"
    ></div>

    <div slot="foreground" class="foreground_container">
      <section class="step_foreground">
        <Header />
      </section>

      {#each sections as section}
        <section class="step_foreground">
          <Section title={section.title} />
        </section>
      {/each}
    </div>
  </Scroller>
</main>

<style>
  :global(body) {
    background-attachment: fixed;
    height: 100%;
    width: 100%;
    background-position: center center;
    background-repeat: no-repeat;
    background-size: cover;
    margin: 0;
  }

  .scroller {
    transition: background-color 1s ease;
    background-color: var(--background-color);
    width: 100%;
    height: 100vh;
    position: absolute;
    overflow-x: hidden;
  }

  /* Estilos para el scroller */
  .foreground_container {
    pointer-events: none;
  }

  .step_foreground {
    display: flex;
    justify-content: end;
    align-items: center;
    height: 100vh;
    border: 3px solid rgba(0, 0, 0, 1);
    color: white;
    margin: 0 0 2em 0;
  }
</style>
