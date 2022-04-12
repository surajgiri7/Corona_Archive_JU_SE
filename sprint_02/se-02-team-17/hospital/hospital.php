<!-- Using the session for the hospital to get the data if the hospital is logged in -->
<?php
session_start();
if (!isset($_SESSION['huser'])) {
    header('Location: hospital_login.php');
} else {
?>

    <html>

    <head>
        <title>Corona Archive - Hospital Stats</title>
        <meta name="viewport" , content="width = device-width, initial-scale=1">
        <link rel="stylesheet" href="../css/table.css">
    </head>

    <body>
        <ul>
            <li> <button class="button"> <a href="hospital_logout.php" class="back"> Log out </a> </button> </li>
        </ul>

        <h1> Citizens list </h4>
            <br>

            <!-- connecting to the database  -->
            <?php
            ini_set('display_errors', 1);
            ini_set('display_startup_errors', 1);
            error_reporting(E_ALL);
            include("../connect.php");

            // getting data from the database 
            $result = mysqli_query($conn, "SELECT * FROM Visitor");
            ?>

            <!-- showing the data from the database in the form of tables  -->
            <table id="entity_table">
                <tr>
                    <th>Name</th>
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
                        <td> <?php if ($array["infected"] == 0) {
                                    echo "not infected";
                                ?>
                                <button type="button" onclick="">Mark Infected</button>
                                <?php
                                $array["infected"] ==0;
                                ?>
                            <?php
                                } else {
                                    echo "infected";
                            ?>
                                <button type="button">Mark Not Infected</button>
                            <?php
                                }; ?>
                        </td>
                    </tr>
                <?php } ?>

            </table>
    </body>
    </html>
<?php
}
?>