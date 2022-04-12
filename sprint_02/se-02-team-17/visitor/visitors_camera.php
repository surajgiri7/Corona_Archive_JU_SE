<!-- Using the session for the Visitor to get the data if the Visitor is logged in -->
<?php
session_start();
if (!isset($_SESSION['vuser'])) {
    header('Location: visitor_login.php');
} else {
?>
    <html>

    <head>
        <title>Corona Archive - Scan QR</title>
        <script src="https://rawgit.com/schmich/instascan-builds/master/instascan.min.js"></script>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/webrtc-adapter/3.3.3/adapter.min.js"></script>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/vue/2.1.10/vue.min.js"></script>
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
        <div class="hero">

            <a href="visitor_logout.php" class="back"><button class="back-btn"> Log Out </button></a>

            <div class="scanner">

            <div class="hp-text">
                <h2>
                    <label>Scan QR Code !</label>
                </h2>
            </div>

            <!-- creating the QR scanner  -->
            <div class="hp-text">
                <video id="preview"></video>
                <script type="text/javascript">
                    let scanner = new Instascan.Scanner({
                        video: document.getElementById('preview')
                    });
                    scanner.addListener('scan', function(content) {
                        document.getElementById("text").value = content
                        // window.location.replace(content); //this line redirects to the data encoded in the QR for eg. if a link in encoded then to that link
                    });
                    Instascan.Camera.getCameras().then(function(cameras) {
                        if (cameras.length > 0) {
                            scanner.start(cameras[0]);
                        } else {
                            console.error('No cameras found.');
                        }
                    }).catch(function(e) {
                        console.error(e);
                    });
                </script>
                <div class="hp-text">
                    <input type="text" name="text" id="text" readonly="" placeholder="QR Data">
                </div>

            </div>
            </div>
        </div>

    </body>

    </html>
<?php
}
?>