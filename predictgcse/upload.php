<?php

$target_dir = "/Upload";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);

$host = "host = ec2-176-34-113-15.eu-west-1.compute.amazonaws.com";
$port = "port = 5432";
$dbname = "dbname = d4on6pdtb6ivkq";
$credentials = "user = enetzncoupodfd password=e7adb8885773bea9ff108fce3755858014e70d487b8476e79ea33671c14ce35d";

$db = pg_connect( "$host $port $dbname $credentials"  );
if(!$db) {
   echo "Error : Unable to open database\n";
   } 
   else {
      echo "Opened database successfully\n";
   }

$query = "INSERT INTO school_data VALUES ('$_POST[schoolid]','$_POST[target_file]',  
'$_POST[price]','$_POST[dop]')";  
$result = pg_query($query); 
$test_data = pg_fetch_all($result);

$fieldname = pg_field_name($test_data);//names of columns

?>