<script>
  export let imgSrc;
  export let top;
  export let zIndex;

  let counter = 0;
  counter += 1;
</script>

<div>{counter}</div>
<div class="post-card" style="top: {top}px; z-index: {zIndex}">
  <img src={imgSrc} alt={imgSrc} />
</div>

<style>
  img {
    top: 0;
    height: 750px;
    position: sticky;
  }

  .post-card {
    height: 3000px;
    position: absolute;
  }
</style>
