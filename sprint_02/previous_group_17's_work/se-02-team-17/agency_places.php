<?php
    session_start();
    if(!isset($_SESSION['suser'])){
        header('Location: agency_login.php');
    } else {
?>

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

    $result = mysqli_query($conn, "SELECT * FROM Places");
    ?>

    <ul>
        <button class="button" ><a href="agency.php" class="back"> Go back </a> </button>
    </ul>

    <table id="entity_table">
        <tr> <th>Name</th> <th>Address</th> </tr>
        <?php while ($array = mysqli_fetch_assoc($result)) { ?>
        <tr><td> <?php echo $array["place_name"]; ?> </td>
        <td> <?php echo $array["place_address"]; ?> </td> </tr>
        <?php } ?>
    
    </table>



</body>

</html>

<?php
    }
?>