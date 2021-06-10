# Portfolio-Lab

<html>
<h1> Project in progtress </h1>
<div class="penguin">
	<div class="penguin-bottom">
		<div class="right-hand">
			<a href="https://www.linkedin.com/in/artur-heraskov-7a7818187/" class="fullCard">
				My linkedin: 
			</a>
		</div>
<div class="left-hand"></div>
<div class="right-feet">
</div>
<div class="left-feet"></div>
</div>
<div class="penguin-top">
	<div class="right-cheek"></div>
	<div class="left-cheek"></div>
	<div class="belly"></div>
	<div class="right-eye">
		<div class="sparkle"></div>
	</div>
<div class="left-eye">
	<div class="sparkle"></div>
</div>
<div class="blush-right"></div>
<div class="blush-left"></div>
<div class="beak-top"></div>
<div class="beak-bottom"></div>

<style>
body{
	background: rgb(60,75,150);
	background: radial-gradient(circle, rgba(60,75,150,1) 40%, rgba(10,36,33,1) 100%);
}

h1{
	color: #fff;
	text-shadow: 2px 2px #ff0000; 
	text-align: center;
}

.penguin {
	--penguin-skin: black;
	--penguin-belly: gray;
	--penguin-beak: yellow;
	position: relative;
	margin: auto;
	display: block;
	margin-top: 5%;
	width:var(--penguin-size);
	height:var(--penguin-size);
}

.penguin-top 
{
	top: 10%;
	left: 25%;
	background: var(--penguin-skin);
	width: 50%;
	height: 45%;
	border-radius: 70% 70% 60% 60% 
}

.penguin-bottom {
	top: 40%;
	left: 23.5%;
	background: var(--penguin-skin);
	width: 53%;
	height: 45%;
	border-radius: 70% 70% 100% 100%;
}

.right-hand {
	top:0%;
	left: 15%;
	background: var(--penguin-skin);
	width: 30%;
	height: 60%;
	border-radius: 30% 30% 120% 30%;
	transform: rotate(100deg);
	z-index: -1;
	animation-duration: 3s;
	animation-name: hi;
	animation-iteration-count: infinite;
	transform-origin:0% 0%;
	animation-timing-function: linear;
}

.left-hand {
	top: 0%;
	left: 75%;
	background: var(--penguin-skin);
	width: 30%;
	height: 60%;
	border-radius: 30% 30% 30% 120%;
	transform: rotate(-55deg); z-index: -1; 
}

.right-cheek { 
	top: 15%;
	left: 35%;
	background: var(--penguin-belly);
	width: 60%;
	height: 70%;
	border-radius: 70% 70% 60% 60%;
}

.left-cheek {
	top: 15%;
	left: 5%;
	background: var(--penguin-belly);
	width: 60%;
	height: 70%;
	border-radius: 70% 70% 60% 60%;
}

.belly {
	top: 60%;
	left: 2.5%;
	background: var(--penguin-belly);
	width: 95%;
	height: 100%;
	border-radius: 120% 120% 100% 100%;
}

.right-feet {
	top: 85%;
	left: 60%;
	background: var(--penguin-beak);
	width: 15%;
	height: 30%;
	border-radius: 50% 50% 50% 50%;
	transform: rotate(-80deg);
	z-index: -2222;
}

.left-feet {
	top: 85%;
	left: 25%;
	background: var(--penguin-beak);
	width: 15%;
	height: 30%;
	border-radius: 50% 50% 50% 50%;
	transform: rotate(80deg);
	z-index: -2222;
}

.right-eye {
	top: 45%;
	left: 60%;
	background: black;
	width: 15%;
	height: 17%;
	border-radius: 50%;
}

.left-eye {
	top: 45%;
	left: 25%;
	background: black;width: 15%;
	height: 17%;
	border-radius: 50%;
}
.sparkle {top: 25%;
	left: 15%;
	background: white;
	width: 35%;
	height: 35%;
	border-radius: 50%;
}

.blush-right {top: 65%;
	left: 15%;
	background: pink ;
	width: 15%;
	height: 10%;
	border-radius: 50%;
}

.blush-left {top: 65%;
	left: 70%;
	background: pink;
	width: 15%;
	height: 10%;
	border-radius: 50%;
}

.beak-top {top: 60%;
	left: 40%;
	background: var(--penguin-beak);
	width: 20%;
	height: 10%;
	border-radius: 50%;
}

.beak-bottom {top: 65%;
	left: 42%;
	background: var(--penguin-beak);
	width: 16%;
	height: 10%;
	border-radius: 50%;
}

@media (max-width: 4050px) {
	:root {--penguin-size:300px;
	--penguin-skin:varblack;
}

@keyframes hi {
	80% {
		transform: rotate(105deg);
	}
	90% {
		transform: rotate(111deg);
	}
	10% {
		transform: rotate(110deg);
	}
	90% {
		transform: rotate(111deg);
	}
}

.penguin * {
	position: absolute;
} 

.fullCard {
	width: 80px;
	border: 4px solid #ccc;
	background: white;
	border-radius: 5px;
	margin: 30px -20px 200px -10px;
	padding: 20px;
	transform: rotate(-110deg);
	border-radius: 30px;

}
.cardContent {
	padding: 10px;
}
</style>
</html>






