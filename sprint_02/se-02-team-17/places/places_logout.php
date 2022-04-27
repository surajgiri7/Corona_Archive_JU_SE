<!-- for logging out and ending the session  -->
<?php
    session_start();
    unset($_SESSION['puser']);
    session_destroy();
    header('Location: places_login.php');
?>