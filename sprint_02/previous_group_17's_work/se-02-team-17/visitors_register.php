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

    <h3> Registration form </h3>
    <form id="formID" action="visitors_register.php" method="post">
    <div class="imgcontainer">
    <img src="vi.jpg" alt="Avatar" class="avatar">
    </div>
    <div class="container">
        <b>Name: <b> <input type="text" name="name"><br>
        <b>Address: <b><input type="text" name="address"><br>
        <b>Phone: <b> <input type="text" name="phone"><br>
        <b>E-mail: <b><input type="text" name="email"><br>
        <input type="hidden" name="deviceID" id="deviceID" value=""><br> 
        <input type="submit" name="signup">
    </div>
    </form>

    <script>
        var navigator_info = window.navigator;
        var screen_info = window.screen;
        var uid = navigator_info.mimeTypes.length;
        uid += navigator_info.userAgent.replace(/\D+/g, '');
        uid += navigator_info.plugins.length;
        uid += screen_info.height || '';
        uid += screen_info.width || '';
        uid += screen_info.pixelDepth || '';
        console.log(uid);
        //document.write(uid);
        //$('#deviceID').val(uid); 
        //$('#formID').submit();
        document.getElementById("deviceID").value = uid
    </script>

    <?php 
    if (isset($_POST['signup'])) {
    $name = $_POST['name'];
    $address = $_POST['address'];
    $phone = $_POST['phone'];
    $email = $_POST['email'];
    $deviceID = $_POST['deviceID'];

    $minDigits = 9;
    $maxDigits = 14;
    
    if ($name == '' || $address == '' || $phone == '' || $email == '' || $deviceID == '') {
        echo 'Information cannot be empty';
    } elseif (!preg_match("/^[a-zA-Z ]+$/",$name)) { // Name Constraint
        echo 'Invalid name';
        error_log ("Invalid name", 0); 
    } elseif (!preg_match('/^[\w\.]+@\w+\.\w+$/i',$email)) { // Email Constraint
        echo 'Invalid email';
        error_log ("Invalid email", 0); 
    } elseif (!preg_match('/^[0-9]{'.$minDigits.','.$maxDigits.'}\z/', $phone)) { // Phone Constraint
        echo 'Invalid phone number';
        error_log ("Invalid phone number", 0); 
    } else {

        // Insert into database
        $sql = "INSERT INTO Visitor (visitor_name, v_address, v_phone_number, v_email, device_ID, infected) VALUES ('$name', '$address', '$phone', '$email', '$deviceID', 0)";
        if (mysqli_query($conn, $sql)){
            header("Location:visitors_camera.php"); 
        } else {
            echo 'Device ID detected in database';
            header("Location:visitors_camera.php");
        }
    }

    }

    ?>




</body>

</html>