<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Home</title>
<link
	href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css"
	rel="stylesheet"
	integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx"
	crossorigin="anonymous">
<script
	src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"
	integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa"
	crossorigin="anonymous"></script>
</head>
<body>
	<div class="container">
		<h1>Hello world!</h1>
		<P>The time on the server is ${serverTime}.</P>
		<nav aria-label="breadcrumb">
			<ol class="breadcrumb">
				<li class="breadcrumb-item"><a href="/myapp/">HOME</a></li>
				<li class="breadcrumb-item active" aria-current="/myapp/insert">INSERT</li>
				<li class="breadcrumb-item"><a href="/myapp/select">SELECT</a></li>
			</ol>
		</nav>
		<div class="m-3 p-3 border">
	        <form method="post">
	            <div class="mb-3">
	                <label for="email" class="form-label">Email</label>
	                <input type="email" class="form-control" id="email" name="email" placeholder="name@example.com">
	            </div>
	            <div class="mb-3">
	                <label for="pwd" class="form-label">Password</label>
	                <input type="password" class="form-control" id="pwd" name="pwd" placeholder="****">
	            </div>
	            <div class="mb-3">
	                <label for="name" class="form-label">Name</label>
	                <input type="text" class="form-control" id="name" name="name" placeholder="Name">
	            </div>
	            <div class="d-flex justify-content-end">
	                <input type="submit" value="등록" class="btn btn-primary">
	            </div>
	        </form>
	    </div>
	</div>
</body>
</html>
