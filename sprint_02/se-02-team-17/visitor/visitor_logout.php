<!-- for logging out and ending the session  -->
<?php
    session_start();
    unset($_SESSION['vuser']);
    session_destroy();
    header('Location: visitor_login.php');
?>