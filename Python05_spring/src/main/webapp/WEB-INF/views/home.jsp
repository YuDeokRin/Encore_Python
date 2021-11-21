<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ page session="false" %>
<html>
<head>
	<title>Home</title>
	
<script type="text/javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script type="text/javascript">

	//window.onload=function(){}
	$(function(){
		var $tbody = $('#tbody');
		
		$.getJSON('http://localhost:8686/crawling', function(data){
			var movies = data.movies;
			
			
			for(var i =0; i< movies.length; i++){
				var $tr = $("<tr>")
				
				var $title = $("<td>").append(movies[i].title);
				var $star = $("<td>").append(movies[i].star);
				
				$tr.append($title);
				$tr.append($star);
				
				$tbody.append($tr);
				
			}
			
		})
		
	})

</script>	
	
</head>
<body>

	<table border="1">
		<thead>
			<tr>
				<th>Title</th>
				<th>Star</th>
			</tr>
		</thead>
		<tbody id="tbody"></tbody>
	</table>



</body>
</html>
