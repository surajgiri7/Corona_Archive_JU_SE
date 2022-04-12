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
    <button class="button" >   <a href="main_page.html" class="back"> Go back </a> </button>
    </ul>

    <h3> Registration form </h3>
    <form action="places_register.php" method="post">
    <div class="imgcontainer">
    <img src="pl.jpg" alt="Avatar" class="avatar">
    </div>
    <div class="container">
        <b>Name:<b><input type="text" name="name"><br>
        <b>Address:<b><input type="text" name="address"><br><br>
        <input type="submit" name="signup">
        </div>
    </form>

    <?php
    if (isset($_POST['signup'])) {
    $name = $_POST['name'];
    $address = $_POST['address'];
    
    if ($name == '' || $address == '') {
        echo 'Information cannot be empty';
    } elseif (!preg_match("/^[a-zA-Z ]+$/",$name)) { // Name Constraint
        echo 'Invalid name';
        error_log ("Invalid name", 0); 
    } else {

        // Insert into database
        $sql = "INSERT INTO Places (place_name, place_address) VALUES ('$name', '$address')";
        if (mysqli_query($conn, $sql)){
            header("Location:places_qrcode.html"); 
        } else {
            echo 'Failed to register';
        }
    }

    }

    ?>




</body>

</html>