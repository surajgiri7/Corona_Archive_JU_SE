<html>
    
<head>
<meta name = "viewport", content="width = device-width, initial-scale=1">
<link rel = "stylesheet" href = "table.css">
</head>

<body>

    <?php 
    
    
    ?>

    <ul>
    <button class="button" ><a href="main_page.html" class="back"> Go back </a> </button>
    </ul>


    <h3> Log in </h3>
    <form action="agency_login.php" method="post">
    <div class="imgcontainer">
    <img src="av.jpg" alt="Avatar" class="avatar">
  </div>

    <div class="container">
       <b> Username: <b> <input type="text" name="username"><br>
       <b> Password: <b> <input type="password" name="password"><br><br>
        <input type="submit" name="login">
    </div>
    </form>

    <?php
    if (isset($_POST['login'])) {

    if (!empty($_POST['username']) && !empty($_POST['password'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    $result = mysqli_query($conn, "SELECT agent_username, agent_password FROM Agent WHERE agent_username = '$username' AND agent_password = '$password'");

    $array = mysqli_fetch_assoc($result);

    if ($array != NULL) {
        session_start();
        $_SESSION['suser'] = $username;
        header("Location: agency.php");
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