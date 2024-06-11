<script>
  import { onMount } from "svelte";

  let sections = [
    { color: "#FF5733" }, // Red
    { color: "#33FF57" }, // Green
    { color: "#3357FF" }, // Blue
    { color: "#FF33A1" }, // Pink
    { color: "#A133FF" }, // Purple
    { color: "#FFD700" }, // Gold
    { color: "#00FFFF" }, // Cyan
    { color: "#FF6347" }, // Tomato
  ];

  let currentIndex = 0;

  function handleScroll() {
    const scrollPosition = window.scrollY;
    const sectionHeight = window.innerHeight;
    const newIndex = Math.round(scrollPosition / sectionHeight);

    if (newIndex !== currentIndex) {
      currentIndex = newIndex;
      updateBackgroundColor();
    }
  }

  function updateBackgroundColor() {
    const color = sections[currentIndex].color;
    document.documentElement.style.setProperty("--current-bg-color", color);
  }

  onMount(() => {
    window.addEventListener("scroll", handleScroll);
    updateBackgroundColor();
    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  });
</script>

<main>
  {#each sections as section, index}
    <section>
      <h1>Section {index + 1}</h1>
    </section>
  {/each}
</main>

<style>
  :global(html, body) {
    margin: 0;
    padding: 0;
    overflow: hidden;
    height: 100%;
    transition: background-color 1s ease;
    background-color: var(--current-bg-color, #ff6347); /* Default to Tomato */
  }
  main {
    scroll-snap-type: y mandatory;
    height: 100vh;
    overflow-y: auto;
    scroll-behavior: smooth;
  }
  section {
    scroll-snap-align: start;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 3rem;
    color: white;
  }
</style>
