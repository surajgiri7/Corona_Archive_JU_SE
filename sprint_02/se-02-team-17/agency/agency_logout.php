<!-- logging out and ending the session  -->
<?php
    session_start();
    unset($_SESSION['auser']);
    session_destroy();
    header('Location: agency_login.php');
?>