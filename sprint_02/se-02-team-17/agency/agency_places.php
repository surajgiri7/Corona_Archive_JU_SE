<!-- Using the session for the agent to get the data if the agent is logged in -->
<?php
session_start();
if (!isset($_SESSION['auser'])) {
    header('Location: agency_login.php');
} else {
?>

    <html>

    <head>
        <title>Corona Archive - Places List</title>
        <meta name="viewport" , content="width = device-width, initial-scale=1">
        <link rel="stylesheet" href="../css/table.css">
    </head>

    <body>

        <!-- connecting to the database  -->
        <?php
        ini_set('display_errors', 1);
        ini_set('display_startup_errors', 1);
        error_reporting(E_ALL);
        include("../connect.php");

        // getting data from the database 
        $result = mysqli_query($conn, "SELECT * FROM Places");
        ?>

        <ul>
            <button class="button"><a href="agency.php" class="back"> Go back </a> </button>
        </ul>

        <table id="entity_table">
            <tr>
                <th>Place</th>
                <th>Address</th>
            </tr>
            <?php while ($array = mysqli_fetch_assoc($result)) { ?>
                <tr>
                    <td> <?php echo $array["place_name"]; ?> </td>
                    <td> <?php echo $array["place_address"]; ?> </td>
                </tr>
            <?php } ?>

        </table>



    </body>

    </html>

<?php
}
?>