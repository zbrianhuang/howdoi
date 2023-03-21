<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>My Website</title>
	<link rel="stylesheet" type="text/css" href="./website/style.css">
	<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9528643461359358"
    crossorigin="anonymous"></script>
</head>
<body>
	<header>
		<nav>
			<ul>
				<li><a href="./index.html">Home</a></li>
				<li><a href="./about.html">About</a></li>
				<li><a href="#">Contact</a></li>
			</ul>
			<a href="#">Log In</a>
		</nav>
	</header>
	<main>
		<p>
			<?php
			$siteLinks=array();
			$fp=fopen('./website_list.txt', 'r');
			while (!feof($fp))
			{
				$line=fgets($fp);
			
				//process line however you like
				$line=trim($line);
			
				//add to array
				$siteLinks[]=$line;
			
			}
			fclose($fp);
			$siteTitles=array();
			$fp=fopen('./website_titles.txt', 'r');
			while (!feof($fp))
			{
				$line=fgets($fp);
			
				//process line however you like
				$line=trim($line);
			
				//add to array
				$siteTitles[]=$line;
			
			}
			fclose($fp);
			for($i= 0;$i<count($siteLinks)-1;$i++){
				echo "<a class='button' href='",$siteLinks[$i],"'>",$siteTitles[$i],"</a>";
				echo"<br><br><br>";
			}
			?>
			
		</p>
		<!--
			<article>
			<h2>Welcome to my website</h2>
			<p>This is some sample text for the main content area.</p>
		</article>
		<article>
			<h2>About me</h2>
			<p>Here's some information about me.</p>
		</article>
		<article>
			<h2>Contact me</h2>
			<p>Feel free to contact me using the form below.</p>
		</article>
		-->
	</main>
	<footer>
		<p>&copy; 2023 My Website. All rights reserved.</p>
	</footer>
</body>
</html>