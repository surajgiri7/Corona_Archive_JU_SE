<html>
    
<head>
</head>

<body>

    <?php 
    
    $dbhost = 'localhost';
    $user ='seteam17';
    $pass ='XFc73r0J';
    $db ='seteam17';
    
    
    $conn= mysqli_connect('localhost', $user, $pass, $db);
    ?>

    <ul>
        <a href="test.html" class="back"> Go back </a> 
    </ul>

    <h3> Log in </h3>
    <form action="testhospital.php" method="post">
        Username:<input type="text" name="username"><br>
        Password:<input type="password" name="password"><br><br>
        <input type="submit" name="login">
    </form>

    <?php
    if (isset($_POST['login'])) {

    if (!empty($_POST['username']) && !empty($_POST['password'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    $result = mysqli_query($conn, "SELECT hospital_username, hospital_password FROM Hospital WHERE hospital_username = '$username' AND hospital_password = '$password'");

    $array = mysqli_fetch_assoc($result);

    if ($array != NULL) {
        echo "Successful Login"; 
    } else { 
        echo "Invalid Login, Please Try Again"; 
        error_log ("Invalid login", 0);
    } 


    } else { 
        echo "All Fields Are Required!"; 
        error_log ("Empty required fields", 0); 
    }

    }

    ?>




</body>

</html>