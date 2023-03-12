<script>
	import sequence from './assets/sequence01.mp4';
	import postCard01 from './assets/postCard01.jpg';
  import postCard02 from './assets/postCard02.jpg';
  import postCard03 from './assets/postCard03.jpg';
  import postCard04 from './assets/postCard04.jpg';
	
  import postCard05 from './assets/postCard05.jpg';
  import postCard06 from './assets/postCard06.jpg';
  import postCard07 from './assets/postCard07.jpg';
  import postCard08 from './assets/postCard08.jpg';
  import postCard09 from './assets/postCard09.jpg';
  import postCard10 from './assets/postCard10.jpg';
  import postCard11 from './assets/postCard11.jpg';
  import postCard12 from './assets/postCard12.jpg';

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
			src={sequence}
			type="video/mp4"
		/>
	</div>

	<div class="scroll-container">
		<div class="post-card-container post01-container">
			<img class="post-card" src={postCard01} alt="postCard01" />
		</div>

    <div class="post-card-container post02-container">
			<img class="post-card" src={postCard02} alt="postCard02" />
		</div>

    <div class="post-card-container post03-container">
			<img class="post-card" src={postCard03} alt="postCard03" />
		</div>

    <div class="post-card-container post04-container">
			<img class="post-card" src={postCard04} alt="postCard04" />
		</div>

    
    <div class="post-card-container post05-container">
			<img class="post-card" src={postCard06} alt="postCard06" />
		</div>

    <div class="post-card-container post06-container">
			<img class="post-card" src={postCard06} alt="postCard06" />
		</div>

    <div class="post-card-container post07-container">
			<img class="post-card" src={postCard07} alt="postCard07" />
		</div>

    <div class="post-card-container post08-container">
			<img class="post-card" src={postCard08} alt="postCard08" />
		</div>

    <div class="post-card-container post09-container">
			<img class="post-card" src={postCard09} alt="postCard09" />
		</div>

    <div class="post-card-container post10-container">
			<img class="post-card" src={postCard10} alt="postCard10" />
		</div>

    <div class="post-card-container post11-container">
			<img class="post-card" src={postCard11} alt="postCard11" />
		</div>

    <div class="post-card-container post12-container">
			<img class="post-card" src={postCard12} alt="postCard12" />
		</div>

		<!-- <img
			class="post02"
			class:show={scrollY > 2900 && scrollY < 4900}
			src={postCard02}
			alt="postCard02"
		/> -->
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

  .post-card {
    width: 100%;
		top: 0px;
		position: sticky;
		position: -webkit-sticky;
	}

  .post-card-container {
    position: absolute;
    left: 0px;
  }

	.post01-container {
		top: 1500px;
    height: 3000px;
	}

  .post02-container {
		top: 3000px;
    height: 3000px;
	}

  .post03-container {
		top: 4500px;
    height: 3000px;
	}

  .post04-container {
		top: 6000px;
    height: 2000px;
	}


  .post05-container {
		top: 10000px;
    height: 3000px;
	}

  .post06-container {
		top: 12500px;
    height: 3000px;
	}

  .post07-container {
		top: 15000px;
    height: 3000px;
	}

  .post08-container {
		top: 17500px;
    height: 3000px;
	}

  .post09-container {
		top: 20000px;
    height: 3000px;
	}

  .post10-container {
		top: 22500px;
    height: 3000px;
	}

  .post11-container {
		top: 25000px;
    height: 3000px;
	}

  .post12-container {
		top: 27600px;
    height: 2000px;
	}

	

	/* .post02 {
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
	} */
</style>
