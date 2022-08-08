<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ page session="false"%>
<html>
<head>
<title>Home</title>
</head>
<body>
	<h1>Hello world!</h1>

	<P>The time on the server is ${serverTime}.</P>
	<h1>
		<a href="member">member</a>
	</h1>
	<h1>
		<a href="memberselect">memberselect</a>
	</h1>
	<p>
		${myvar}
	</p>
</body>
</html>
