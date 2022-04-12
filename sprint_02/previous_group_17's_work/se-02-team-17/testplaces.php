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

    <h3> Registration form </h3>
    <form action="testplaces.php" method="post">
        Name:<input type="text" name="name"><br>
        Address:<input type="text" name="address"><br><br>
        <input type="submit" name="signup">
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
            echo "Registration successful";
        } else {
            echo "Registration failed";
        }
    }

    }

    ?>




</body>

</html>