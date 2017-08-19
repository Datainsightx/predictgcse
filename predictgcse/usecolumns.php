<?php

   $host        = "host = ec2-176-34-113-15.eu-west-1.compute.amazonaws.com";
   $port        = "port = 5432";
   $dbname      = "dbname = d4on6pdtb6ivkq";
   $credentials = "user = enetzncoupodfd password=e7adb8885773bea9ff108fce3755858014e70d487b8476e79ea33671c14ce35d";

   $db = pg_connect( "$host $port $dbname $credentials"  );
   if(!$db) {
      echo "Error : Unable to open database\n";
   } else {
      echo "Opened database successfully\n";
   }
?>