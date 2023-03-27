<script>
  import sequence01 from "./assets/sequence01.mp4";
  import sequence02 from "./assets/Sequence02.mp4";
  import sequence03 from "./assets/Sequence03.mp4";
  import sequence04 from "./assets/Sequence04.mp4";
  import sequence05 from "./assets/Sequence05.mp4";
  import sequence06 from "./assets/Sequence06.mp4";

  import ansichtkaart1 from "./assets/ansichtkaart1.jpg";
  import ansichtkaart2 from "./assets/ansichtkaart2.jpg";
  import ansichtkaart3 from "./assets/ansichtkaart3.jpg";
  import ansichtkaart4 from "./assets/ansichtkaart4.jpg";
  import ansichtkaart5 from "./assets/ansichtkaart5.jpg";
  import ansichtkaart6 from "./assets/ansichtkaart6.jpg";
  import ansichtkaart7 from "./assets/ansichtkaart7.jpg";
  import ansichtkaart8 from "./assets/ansichtkaart8.jpg";
  import ansichtkaart9 from "./assets/ansichtkaart9.jpg";
  import ansichtkaart10 from "./assets/ansichtkaart10.jpg";
  import ansichtkaart11 from "./assets/ansichtkaart11.jpg";
  import ansichtkaart12 from "./assets/ansichtkaart12.jpg";
  import ansichtkaart13 from "./assets/ansichtkaart12.jpg";
  import ansichtkaart14 from "./assets/ansichtkaart14.jpg";
  import ansichtkaart15 from "./assets/ansichtkaart15.jpg";
  import ansichtkaart16 from "./assets/ansichtkaart16.jpg";
  import ansichtkaart17 from "./assets/ansichtkaart17.jpg";
  import ansichtkaart18 from "./assets/ansichtkaart18.jpg";
  import ansichtkaart19 from "./assets/ansichtkaart19.jpg";
  import ansichtkaart20 from "./assets/ansichtkaart20.jpg";
  import ansichtkaart21 from "./assets/ansichtkaart21.jpg";
  import ansichtkaart22 from "./assets/ansichtkaart22.jpg";
  import ansichtkaart23 from "./assets/ansichtkaart23.jpg";
  import ansichtkaart24 from "./assets/ansichtkaart24.jpg";

  let scrollY;
  let duration01;
  let duration02;
  let duration03;
  let duration04;
  let duration05;
  let duration06;

  $: time01 = duration01 * (scrollY / 4000);
  $: time02 = duration02 * ((scrollY - 16000) / 8000);
  $: time03 = duration03 * ((scrollY - 48000) / 4000);
  $: time04 = duration04 * ((scrollY - 76000) / 4000);
  $: time05 = duration05 * ((scrollY - 90000) / 800);
  $: time06 = duration06 * ((scrollY - 105800) / 4000);
</script>

<svelte:window bind:scrollY />
<main>
  <div class="secuence01-container">
    <video
      bind:currentTime={time01}
      bind:duration={duration01}
      preload="metadata"
      muted
      src={sequence01}
      type="video/mp4"
    />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart1} alt="ansichtkaart1" />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart2} alt="ansichtkaart2" />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart3} alt="ansichtkaart3" />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart4} alt="ansichtkaart4" />
  </div>

  <div class="secuence02-container">
    <video
      bind:currentTime={time02}
      bind:duration={duration02}
      preload="metadata"
      muted
      src={sequence02}
      type="video/mp4"
    />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart5} alt="ansichtkaart5" />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart6} alt="ansichtkaart6" />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart7} alt="ansichtkaart7" />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart8} alt="ansichtkaart8" />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart9} alt="ansichtkaart9" />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart10} alt="ansichtkaart10" />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart11} alt="ansichtkaart11" />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart12} alt="ansichtkaart12" />
  </div>

  <div class="secuence03-container">
    <video
      bind:currentTime={time03}
      bind:duration={duration03}
      preload="metadata"
      muted
      src={sequence03}
      type="video/mp4"
    />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart13} alt="ansichtkaart13" />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart14} alt="ansichtkaart14" />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart15} alt="ansichtkaart14" />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart16} alt="ansichtkaart16" />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart17} alt="ansichtkaart17" />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart18} alt="ansichtkaart18" />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart19} alt="ansichtkaart19" />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart20} alt="ansichtkaart20" />
  </div>

  <div class="secuence04-container">
    <video
      bind:currentTime={time04}
      bind:duration={duration04}
      preload="metadata"
      muted
      src={sequence04}
      type="video/mp4"
    />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart21} alt="ansichtkaart21" />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart22} alt="ansichtkaart22" />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart23} alt="ansichtkaart23" />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart24} alt="ansichtkaart24" />
  </div>

  <div class="secuence05-container">
    <video
      bind:currentTime={time05}
      bind:duration={duration05}
      preload="metadata"
      muted
      src={sequence05}
      type="video/mp4"
    />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart21} alt="ansichtkaart21" />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart22} alt="ansichtkaart22" />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart23} alt="ansichtkaart23" />
  </div>

  <div class="ansichtkaart-container">
    <img class="post-card" src={ansichtkaart24} alt="ansichtkaart24" />
  </div>

  <div class="secuence05-container">
    <video
      bind:currentTime={time06}
      bind:duration={duration06}
      preload="metadata"
      muted
      src={sequence06}
      type="video/mp4"
    />
  </div>
</main>

<style>
  video {
    width: 100%;
    position: sticky;
    position: -webkit-sticky;
    top: 0px;
  }

  .post-card {
    top: 0;
    width: 100%;
    position: sticky;
  }
  .secuence01-container {
    height: 4000px;
  }

  .secuence02-container {
    height: 8000px;
  }

  .secuence03-container {
    height: 4000px;
  }

  .secuence04-container {
    height: 3000px;
  }

  .secuence05-container {
    height: 800px;
  }

  .secuence05-container {
    height: 4000px;
  }

  .ansichtkaart-container {
    height: 3000px;
  }
</style>
