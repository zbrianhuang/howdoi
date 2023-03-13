<!DOCTYPE html>
<html>
<head>
	<title>My Website</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
	<header>
		<nav>
			<ul>
				<li><a href="./index.html">Home</a></li>
				<li><a href="#">About</a></li>
				<li><a href="#">Contact</a></li>
			</ul>
			<a href="#">Log In</a>
		</nav>
	</header>
	<main>
		<p>
		<?php
			$lines=array();
			$fp=fopen('./website_list.txt', 'r');
			while (!feof($fp))
			{
				$line=fgets($fp);
			
				//process line however you like
				$line=trim($line);
			
				//add to array
				$lines[]=$line;
			
			}
			fclose($fp);
			$linkTitle="filler";
			for($i= 0;$i<count($lines)-1;$i++){
				echo "<a href='",$lines[$i],"'>",$linkTitle,$i,"</a>";
				echo"<br>";
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