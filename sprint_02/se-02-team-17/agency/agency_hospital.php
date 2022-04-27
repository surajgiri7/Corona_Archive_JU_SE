<!-- Using the session for the agent to get the data if the agent is logged in -->
<?php
    session_start();
    if(!isset($_SESSION['auser'])){
        header('Location: agency_login.php');
    } else {
?>

<html>
<head>
<title>Corona Archive - Hospital List</title>
<meta name = "viewport", content="width = device-width, initial-scale=1">
<link rel = "stylesheet" href = "../css/table.css">
</head>

<body> 
    <?php 
    ini_set('display_errors', 1);
    ini_set('display_startup_errors', 1);
    error_reporting(E_ALL);
    include("../connect.php");
    
    $result = mysqli_query($conn, "SELECT * FROM Hospital");
    ?>

    <ul>
        <button class="button" ><a href="agency.php" class="back"> Go back </a> </button>
    </ul>

    <!-- Showing the data about hospitals in the form of a table -->
    <table id="entity_table">
        <tr> <th>Hospital</th> <th>Address</th> </tr>
        <?php while ($array = mysqli_fetch_assoc($result)) { ?>
        <tr><td> <?php echo $array["hospital_username"]; ?> </td>
        <td> <?php echo $array["hospital_address"]; ?> </td> </tr>
        <?php } ?>
    
    </table>



</body>

</html>

<?php
    }
?>