<script>
	import townVideo from './assets/testVideo02.mp4';
	import postCard01 from './assets/post01.jpeg';
	import postCard02 from './assets/post02.jpeg';
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
	<div class="video-container">
		<video
			bind:currentTime={time}
			bind:duration
			preload="metadata"
			muted
			src={townVideo}
			type="video/mp4"
		/>
	</div>

	<div class="scroll-container">
		<div class="post01-container">
			<img class="post01" src={postCard01} alt="postCard01" />
		</div>
		<img
			class="post02"
			class:show={scrollY > 2900 && scrollY < 4900}
			src={postCard02}
			alt="postCard02"
		/>
	</div>
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
		height: 10000px;
	}

	.post01-container {
		position: absolute;
		top: 1500px;
		width: 100%;
		height: 3000px;
	}

	.post01 {
		display: block;
		top: 50px;
		position: sticky;
		position: -webkit-sticky;
		margin-left: auto;
		margin-right: auto;
	}

	.post02 {
		min-width: 100%;
		min-height: 100%;
		left: 0px;
		top: 0px;
		position: fixed;
		z-index: 2;
		visibility: hidden;
	}

	.show {
		visibility: visible;
	}
</style>
