<script>
	let scrollY;
	let time;
	let duration;

	$: {
		const totalScroll = document.documentElement.scrollHeight - window.innerHeight;
		time = duration * (scrollY / totalScroll);
	}
</script>

<svelte:window bind:scrollY />
<main>
	<div class="scroll-container" />

	<div class="video-container">
		<video
			bind:currentTime={time}
			bind:duration
			preload="metadata"
			muted
			src="src/assets/testVideo.mp4"
		/>
	</div>

	<h1>Hola Ingrid</h1>
</main>

<style>
	.video-container {
		position: absolute;
		top: 0;
		bottom: 0;
		overflow: hidden;
	}

	.video-container video {
		min-width: 100%;
		min-height: 100%;
		width: auto;
		height: auto;
		position: fixed;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
	}

	.scroll-container {
		height: 15000px;
	}
</style>
