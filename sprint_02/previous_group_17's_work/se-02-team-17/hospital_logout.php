<?php
    session_start();
    unset($_SESSION['huser']);
    session_destroy();
    header('Location: hospital_login.php');
?>