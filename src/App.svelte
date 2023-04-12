<script>
  import sequence01 from "./assets/Sequence01.webm";
  import sequence02 from "./assets/Sequence02.webm";
  import sequence03 from "./assets/Sequence03.webm";
  import sequence04 from "./assets/Sequence04.webm";
  import sequence05 from "./assets/Sequence05.webm";
  import sequence06 from "./assets/Sequence06.webm";

  import PostCard from "./lib/PostCard.svelte";
  import {
    postCardsSecuence01,
    postCardsSecuence02,
    postCardsSecuence03,
    postCardsSecuence04,
    postCardsSecuence05,
  } from "./lib/secuences";

  const VideoDurationFactor = 140;

  let scrollY;
  let duration01;
  let duration02;
  let duration03;
  let duration04;
  let duration05;
  let duration06;

  $: videoTop02 =
    duration01 * VideoDurationFactor + postCardsSecuence01.length * 1000;

  $: videoTop03 =
    videoTop02 +
    duration02 * VideoDurationFactor +
    postCardsSecuence02.length * 1000;

  $: videoTop04 =
    videoTop03 +
    duration03 * VideoDurationFactor +
    postCardsSecuence03.length * 1000;

  $: videoTop05 =
    videoTop04 +
    duration04 * VideoDurationFactor +
    postCardsSecuence04.length * 1000;

  $: videoTop06 =
    videoTop05 +
    duration05 * VideoDurationFactor +
    postCardsSecuence05.length * 1000;

  $: time01 = getVideocurrentTime(duration01, scrollY, 0);

  $: time02 = getVideocurrentTime(duration02, scrollY, videoTop02);

  $: time03 = getVideocurrentTime(duration03, scrollY, videoTop03);

  $: time04 = getVideocurrentTime(duration04, scrollY, videoTop04);

  $: time05 = getVideocurrentTime(duration05, scrollY, videoTop05);

  $: time06 = getVideocurrentTime(duration06, scrollY, videoTop06);

  function getVideocurrentTime(
    videoDuration,
    pageHeight,
    videoContainerTopDistance
  ) {
    return (
      videoDuration *
      ((pageHeight - videoContainerTopDistance) /
        (videoDuration * VideoDurationFactor))
    );
  }
</script>

<svelte:window bind:scrollY />
<main>
  {#if !sequence01 && !sequence02 && !sequence03 && !sequence04 && !sequence05}
    <div>LOADING ...</div>
  {:else}
    <div style="height: {duration01 * VideoDurationFactor}px">
      <video
        bind:currentTime={time01}
        bind:duration={duration01}
        preload="metadata"
        muted
        src={sequence01}
      />
    </div>

    {#each postCardsSecuence01 as postCard, index}
      <PostCard
        imgSrc={postCard}
        top={duration01 * VideoDurationFactor + index * 1000}
        zIndex={index + 2}
      />
    {/each}

    <div
      style="
      height: {duration02 * VideoDurationFactor}px; 
      position: absolute;
      top: {videoTop02}px; z-index: 100
    "
    >
      <video
        bind:currentTime={time02}
        bind:duration={duration02}
        preload="metadata"
        muted
        src={sequence02}
      />
    </div>

    {#each postCardsSecuence02 as postCard, index}
      <PostCard
        imgSrc={postCard}
        top={videoTop02 + duration02 * VideoDurationFactor + index * 1000}
        zIndex={index + 100 + 2}
      />
    {/each}

    <div
      style="height: {duration03 * VideoDurationFactor}px; 
      position: absolute; 
      top: {videoTop03}px; z-index: 200"
    >
      <video
        bind:currentTime={time03}
        bind:duration={duration03}
        preload="metadata"
        muted
        src={sequence03}
      />
    </div>

    {#each postCardsSecuence03 as postCard, index}
      <PostCard
        imgSrc={postCard}
        top={videoTop03 + duration03 * VideoDurationFactor + index * 1000}
        zIndex={index + 300 + 2}
      />
    {/each}

    <div
      style="height: {duration04 * VideoDurationFactor}px; 
      position: absolute; 
      top: {videoTop04}px; z-index: 400"
    >
      <video
        bind:currentTime={time04}
        bind:duration={duration04}
        preload="metadata"
        muted
        src={sequence04}
      />
    </div>

    {#each postCardsSecuence04 as postCard, index}
      <PostCard
        imgSrc={postCard}
        top={videoTop04 + duration04 * VideoDurationFactor + index * 1000}
        zIndex={index + 400 + 2}
      />
    {/each}

    <div
      style="height: {duration05 * VideoDurationFactor}px; 
    position: absolute; 
    top: {videoTop05}px; z-index: 500"
    >
      <video
        bind:currentTime={time05}
        bind:duration={duration05}
        preload="metadata"
        muted
        src={sequence05}
      />
    </div>

    {#each postCardsSecuence05 as postCard, index}
      <PostCard
        imgSrc={postCard}
        top={videoTop05 + duration05 * VideoDurationFactor + index * 1000}
        zIndex={index + 500 + 2}
      />
    {/each}

    <div
      style="height: {duration06 * VideoDurationFactor}px; 
    position: absolute; 
    top: {videoTop06}px; z-index: 600"
    >
      <video
        bind:currentTime={time06}
        bind:duration={duration06}
        preload="metadata"
        muted
        src={sequence06}
      />
    </div>
  {/if}
</main>

<style>
  video {
    height: 750px;
    position: sticky;
    position: -webkit-sticky;
    top: 0px;
  }
</style>
