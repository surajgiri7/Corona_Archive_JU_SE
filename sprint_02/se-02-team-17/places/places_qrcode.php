<!-- Using the session for the Places to get the data if the Places is logged in -->
<?php
session_start();
if (!isset($_SESSION['puser'])) {
    header('Location: places_register.php');
} else {
?>

    <html lang="en">

    <head>
        <link rel="stylesheet" href="../css/t.css">
        <link rel="stylesheet" href="../css/table.css">

        <link href='https://unpkg.com/boxicons@2.1.1/css/boxicons.min.css' rel='stylesheet'>
        <link rel="stylesheet" href="https://pro.fontawesome.com/releases/v5.10.0/css/all.css" />
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;700;900&display=swap" rel="stylesheet" />

    </head>

    <body>
        <div class="hero">
            <a href="places_register.php" class="back"><button class="back-btn"> Go back </button></a>

            <div class="form-box-pr">

                <!-- connecting to the database  -->
                <?php
                ini_set('display_errors', 1);
                ini_set('display_startup_errors', 1);
                error_reporting(E_ALL);
                include("../connect.php");

                $email = $_SESSION['puser'];

                // getting data from the database 
                $search = "SELECT * FROM Places WHERE place_email like '$email'";

                $result = mysqli_query($conn, $search);
                $queryResults = mysqli_num_rows($result);
                if ($queryResults > 0) {
                    while ($row = mysqli_fetch_assoc($result)) {
                        $a = $row["place_id"];
                        $b = $row["place_name"];
                        $c = $row["place_address"];
                    }
                }

                ?>

                <?php echo "<h1 style=\"color:black\">" . $b . "</h1>"; ?>
                <div class="hp-text">
                    <h2> Get the QR code by clicking "Get QR" below !</h2>
                </div>

                <!-- generating the QR code with the registration data about that place from previous page  -->
                <input type="text" value="Place ID: <?php echo $a ?>, Place: <?php echo $b ?>,  Address: <?php echo $c ?>" id="qr-data">
                <input type="submit" id="button1" onclick="generateQR()" value="Get QR">

                <div style="display: flex;justify-content:center" id="qrcode">
                    <script type="text/javascript" src="qr_generator.js"></script>
                </div>
            </div>
        </div>

    </body>

    </html>
<?php
}
?>