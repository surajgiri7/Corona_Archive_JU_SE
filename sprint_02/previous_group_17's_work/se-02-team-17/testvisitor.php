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

    <form id="formID" action="testvisitor.php" method="post">
        Name:<input type="text" name="name"><br>
        Address:<input type="text" name="address"><br>
        Phone:<input type="text" name="phone"><br>
        E-mail:<input type="text" name="email"><br>
        <input type="hidden" name="deviceID" id="deviceID" value=""><br> 
        <input type="submit" name="signup">
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
        //$('#deviceID').val(uid); //<-- this code will take a variable as value an assign it into hidden input
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
            echo "Registration successful";
        } else {
            echo "Registration failed";
        }
    }

    }

    ?>




</body>

</html>