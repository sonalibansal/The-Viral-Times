<?php
$con=mysql_connect("localhost","root","") or die("Failed to connect with database!!!!");
mysql_select_db("graphs", $con); 
// The Chart table contains two fields: weekly_task and percentage
// This example will display a pie chart. If you need other charts such as a Bar chart, you will need to modify the code a little to make it work with bar chart and other charts
$sth = mysql_query("SELECT * FROM yoga_nooflikesonpost");


$rows = array();
//flag is not needed
$flag = true;
$table = array();
$table['cols'] = array(

    // Labels for your chart, these represent the column titles
    // Note that one column is in "string" format and another one is in "number" format as pie chart only required "numbers" for calculating percentage and string will be used for column title
    array('label' => 'year', 'type' => 'string'),
    array('label' => '1574465516175930', 'type' => 'number'),
    array('label' => '1585916271683880', 'type' => 'number'),
    array('label' => '1720598614874100', 'type' => 'number'),
    array('label' => '371809679678818', 'type' => 'number'),
    array('label' => '474672786033609', 'type' => 'number'),
    array('label' => '510119875839420', 'type' => 'number'),
    array('label' => '629664907159981', 'type' => 'number')

);

$rows = array();
while($r = mysql_fetch_assoc($sth)) {
    $temp = array();
    // the following line will be used to slice the Pie chart
    $temp[] = array('v' => (int) $r['year']); 

    // Values of each slice
    $temp[] = array('v' => (int) $r['1574465516175930']); 
    $temp[] = array('v' => (int) $r['1585916271683880']); 
    $temp[] = array('v' => (int) $r['1720598614874100']); 
    $temp[] = array('v' => (int) $r['371809679678818']);
    $temp[] = array('v' => (int) $r['474672786033609']); 
    $temp[] = array('v' => (int) $r['510119875839420']); 
    $temp[] = array('v' => (int) $r['629664907159981']); 
    $rows[] = array('c' => $temp);

}

$table['rows'] = $rows;
$jsonTable = json_encode($table);
//echo $jsonTable;
?>

<html>
  <head>
  
  <h1>  </h1>
    <!--Load the Ajax API-->
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
    <script type="text/javascript">

    // Load the Visualization API and the piechart package.
    google.load('visualization', '1', {'packages':['corechart']});

    // Set a callback to run when the Google Visualization API is loaded.
    google.setOnLoadCallback(drawChart);

    function drawChart() {

      // Create our data table out of JSON data loaded from server.
      var data = new google.visualization.DataTable(<?=$jsonTable?>);
      var options = {
           title: 'Yoga Day Pages Yearly Popularity Comparison on the basis of Number of Likes on Posts',
          is3D: 'true',
          width: 850,
          height: 800,
	hAxis:{ title: 'Year'},
	vAxis:{ title: 'Number of Likes'}
        };
      // Instantiate and draw our chart, passing in some options.
      // Do not forget to check your div ID
      var chart = new google.visualization.AreaChart(document.getElementById('chart_div'));
      chart.draw(data, options);
    }
    </script>
  </head>

  <body>
    <center>
       <!--this is the div that will hold the pie chart-->
    <div id="chart_div"></div>
    </center>
   
  </body>
</html>