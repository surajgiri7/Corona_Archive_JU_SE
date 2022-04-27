<!-- Using the session for the agent to get the data if the agent is logged in -->
<?php
session_start();
if (!isset($_SESSION['auser'])) {
    header('Location: agency_login.php');
} else {
?>

    <html>

    <head>
        <title>Corona Archive - Visitor List</title>
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
        $result = mysqli_query($conn, "SELECT * FROM Visitor");
        ?>

        <ul>
            <button class="button"><a href="agency.php" class="back"> Go back </a> </button>
        </ul>


        <!-- displaying the data from the database in the form of table  -->
        <table id="entity_table">
            <tr>
                <th>Visitor</th>
                <th>Address</th>
                <th>Phone</th>
                <th>Email</th>
                <th>Infected</th>
            </tr>
            <?php while ($array = mysqli_fetch_assoc($result)) { ?>
                <tr>
                    <td> <?php echo $array["visitor_name"]; ?> </td>
                    <td> <?php echo $array["visitor_address"]; ?> </td>
                    <td> <?php echo $array["visitor_phone"]; ?> </td>
                    <td> <?php echo $array["visitor_email"]; ?> </td>
                    <td> <?php if ($array["infected"] = 0) {
                                echo "infected";
                            } else {
                                echo "not infected";
                            }; ?></td>
                </tr>
            <?php } ?>

        </table>



    </body>

    </html>

<?php
}
?>