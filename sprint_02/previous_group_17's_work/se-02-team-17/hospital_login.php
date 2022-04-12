<html>
    
<head>
<meta name = "viewport", content="width = device-width, initial-scale=1">
<link rel = "stylesheet" href = "table.css">
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
    <button class="button" ><a href="main_page.html" class="back"> Go back </a> </button>
    </ul>

    <h3> Log in </h3>

    <form action="hospital_login.php" method="post">
    <div class="imgcontainer">
    <img src="doc.jpg" alt="Avatar" class="avatar">
    </div>
    <div class="container">
        <b>Username:<b><input type="text" name="username"><br>
        <b>Password:<b><input type="password" name="password"><br><br>
        <input type="submit" name="login">
        </div>
    </form>

    <?php
    if (isset($_POST['login'])) {

    if (!empty($_POST['username']) && !empty($_POST['password'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    $result = mysqli_query($conn, "SELECT hospital_username, hospital_password FROM Hospital WHERE hospital_username = '$username' AND hospital_password = '$password'");

    $array = mysqli_fetch_assoc($result);

    if ($array != NULL) {
        session_start();
        $_SESSION['huser'] = $username;
        header("Location: hospital.php");
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