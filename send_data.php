<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "counter_reader";

// Create a connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Get data from the POST request
    $value = $_POST['Value'];
    $id_user = $_POST['Id_user'];
    $timestamps = $_POST['Timestamps'];

    // Ensure values are not empty
    if (!empty($value) && !empty($id_user) && !empty($timestamps)) {
        // SQL query to insert data
        $sql = "INSERT INTO conso (Value, Id_user, Timestamps) VALUES ('$value', '$id_user', '$timestamps')";

        if ($conn->query($sql) === TRUE) {
            echo "Data inserted successfully";
        } else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }
    } else {
        echo "One or more values are empty.";
    }
} else {
    echo "Invalid request method.";
}

$conn->close();

?>
