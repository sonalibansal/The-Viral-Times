<?php
$con=mysql_connect("localhost","root","") or die("Failed to connect with database!!!!");
mysql_select_db("jlf_db", $con); 

// The Chart table contain two fields: Date and PercentageChange
$queryData = mysql_query("
	SELECT
		year,
		page1,
		page2
	FROM (
		SELECT
			a.year,
			a.post_count AS page1,
			b.post_count
		 AS page2
		FROM riapost_474 AS a
		LEFT JOIN riapost_6181872 AS b ON (a.year = b.year)
		UNION
		SELECT
			b.year,
			a.post_count AS page1,
			b.post_count AS page2
		FROM riapost_474 AS a
		RIGHT JOIN riapost_6181872 AS b ON (a.year = b.year)
	) AS x
	ORDER BY year ASC
");

$table = array();
$table['cols'] = array(
    array('label' => 'Year', 'type' => 'string'),
    array('label' => 'Page 1', 'type' => 'number'),
    array('label' => 'Page 2', 'type' => 'number')
);

//First Series
$rows = array();
while($r = mysql_fetch_assoc($queryData)) {
	$temp = array();
	// the following line will used to slice the Pie chart
	$temp[] = array('v' => (int) $r['year']); 

	//Values of the each slice
	$temp[] = array('v' => (int) $r['page1']); 
	$temp[] = array('v' => (int) $r['page2']); 
	$rows[] = array('c' => $temp);
}

$table['rows'] = $rows;
$jsonTable = json_encode($table);
?>
<!DOCTYPE html>
<html>
<head>
    <!--Load the AJAX API-->
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
    <script type="text/javascript">
		// Load the Visualization API and the chart package.
		google.load('visualization', '1', {'packages':['corechart']});

		// Set a callback to run when the Google Visualization API is loaded.
		google.setOnLoadCallback(drawChart);

		function drawChart() {
			// Create our data table out of JSON data loaded from server.
			var data = new google.visualization.DataTable(<?=$jsonTable?>);
			var options = {
				title: 'Jaipur Literature Festival Pages Popularity Comparison on Basis of Number Of Posts Yearly',
				width: 800,
				height: 600,
hAxis: {
          title: 'Year'
        },
        vAxis: {
          title: 'Number of posts',
     
        }
			};
			// Instantiate and draw our chart, passing in some options.
			var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
			chart.draw(data, options);
		}
    </script>
</head>

<body>
	<!--Div that will hold the pie chart-->
	<div id="chart_div"></div>
</body>
</html>