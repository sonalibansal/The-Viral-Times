<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>The Viral Times</title>

    <!-- Bootstrap Core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="font-awesome-4.6.3/css/font-awesome.min.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="css/yoga.css" rel="stylesheet">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

</head>

<body>

<nav class="navbar navbar-inverse navbar-fixed-top">
  		<div class="container-fluid">
  			<button type="button" class="navbar-toggle"
  				data-toggle="collapse"
  				data-target=".navbar-collapse">
				<span class="sr-only">Toggle variation</span> 
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
  			</button>

  			<div class="navbar-collapse collapse">
  				<ul class="nav navbar-nav navbar-right">
  					<li class="active" ><a href=""><i class="fa fa-home" aria-hidden="true"></i> Home </a></li>
  					<li class=""><a href="events.html"> Events</a></li>
  					<li class="" ><a href="team.html"><i class="fa fa-users" aria-hidden="true"></i> Team</a></li>
  				</ul>
  			</div>
  	
  		 </div>
	</nav>
<br><br>
    <!-- Full Width Image Header -->
    <header class="header-image" style="background-image:"yoga.png" ; background-size: cover; background-position: center; height: 200px">
        <div class="headline">
            <div class="container">
                <h2>International Yoga Day</h2>
                
                <br>
                <i>
                <p class="paragraph box-shadow">
                    <strong>"</strong>


                   International Day of Yoga  (Antarāshtriya Yog Divas),is celebrated annually on June 21 since its inception in 2015. An international day for yoga was declared by the United Nations General Assembly (UNGA) on December 11, 2014 unanimously.Celebrated with great enthusiasm, the event today stands as one of the prominent events which are aimed at creating health awareness. This year saw mass participation across the country.


                    <strong>"</strong>
                      
                </p>
                
                </i>
                   
            </div>
        </div>
    </header>
<br>
<hr>

<br>

<div class="container">
<div class="row">
<div class="col-md-8">
    <strong><p> Select the graph you want to view from the adjacent dropdown menu.</p></strong>
</div>
<div class="col-md-4">
<div class="dropdown ">
    <button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
    Choose a chart
    <span class="caret"></span>
    </button>
    <ul class="dropdown-menu" aria-labelledby="dropdownMenu1">
    <li class="dropdown-header">For each page</li>
    <li ><a href="yoga.php">Fan count</a></li>
    <li><a href="yoga_checkin.php">Checkins</a></li>
    <li><a href="yoga_peopletalking.php">People Talking</a></li>
    <li role="separator" class="divider"></li>
    <li class="dropdown-header">Cumulative (Year wise)</li>
    <li><a href="yoga_posts.php">Number of posts</a></li>
    <li><a href="yoga_likes.php">Number of likes on posts</a></li>
    <li class="active"><a href="yoga_comments.php">Number of Comments on posts</a></li>
    </ul>
</div>
</div>        
</div>
</div>
<br><br>




<div class="container">
    
            <?php include("php/yoga_noofcomments.php"); ?>
              
      
 </div>



























<hr>























    


    <footer>
    <div class="container">
            <div class="navbar-text pull-left">
            <p><i class="fa fa-copyright" aria-hidden="true"></i> IGDTUW 2016 </p>
            </div>

            <div class="navbar-text pull-right">
            <a href="#"><i class="fa fa-facebook " aria-hidden="true"></i></a>
            <a href="#"><i class="fa fa-instagram " aria-hidden="true"></i></a>
            <a href="#"><i class="fa fa-twitter" aria-hidden="true"></i></a>
            <a href="#"><i class="fa fa-google-plus-official" aria-hidden="true"></i></a>
            <a href="#"><i class="fa fa-linkedin" aria-hidden="true"></i></a>
  
                </div>
            </div>
        </footer>

   
    <!-- /.container -->

    <!-- jQuery -->
    <script src="js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="js/bootstrap.min.js"></script>

</body>

</html>
