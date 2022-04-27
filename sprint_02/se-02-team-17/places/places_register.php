<!DOCTYPE html>
<html>

<head>
    <title>Corona Archive - Places Register</title>
    <meta name="viewport" , content="width = device-width, initial-scale=1">
    <title> Corona Archive </title>
    <link rel="stylesheet" href="../css/t.css">
    <link href='https://unpkg.com/boxicons@2.1.1/css/boxicons.min.css' rel='stylesheet'>
    <link rel="stylesheet" href="https://pro.fontawesome.com/releases/v5.10.0/css/all.css" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;700;900&display=swap" rel="stylesheet" />
</head>

<body>
    <!-- connecting to the database  -->
    <?php

    ini_set('display_errors', 1);
    ini_set('display_startup_errors', 1);
    error_reporting(E_ALL);
    include("../connect.php");
    ?>

    <div class="hero">
        <a href="../index.php" class="back"><button class="back-btn"> Home </button></a>
        <a href="../register.php" class="back"><button class="back-btn"> Go back </button></a>
        <div class="form-box-pr">
            <div class="hp-text">
                <h2>Places Registration Form</h2>
            </div>
            <div class="logo-hp">
                <img src="../images/pl.jpg">
            </div>

            <form action="places_register.php" method="post" class="input-grp">
                <input type="text" name="name" class="input-field" placeholder="Full Name">
                <input type="text" name="address" class="input-field" placeholder="Address">
                <input type="text" name="email" class="input-field" placeholder="Email">
                <input type="password" name="password" class="input-field" placeholder="password">
                <input type="hidden" name="deviceID" id="deviceID" value="">
                <input type="submit" name="signup" value="Register">
            </form>
        </div>
    </div>

    <?php


    if (isset($_POST['signup'])) {
        $name = $_POST['name'];
        $address = $_POST['address'];
        $email = $_POST['email'];
        $password = $_POST['password'];

        // display error if fields left empty 
        if ($name == '' || $address == '' || $password == '') {
            echo 'Information cannot be empty';
        } elseif (!preg_match('/^[\w\.]+@\w+\.\w+$/i', $email)) { // Email Constraints
            echo 'Invalid email';
            error_log("Invalid email", 0);
        } else {

            // Insert into database
            $sql = "INSERT INTO Places (place_name, place_address, place_email, place_password) VALUES ('$name', '$address', '$email', '$password')";
            if (mysqli_query($conn, $sql)) {
    ?>
                <!-- starting session to generate qr -->
    <?php
                session_start();
                $_SESSION['puser'] = $email;


                header("Location:places_qrcode.php");
            } else {
                echo 'Failed to register';
            }
        }
    }

    ?>




</body>

</html>