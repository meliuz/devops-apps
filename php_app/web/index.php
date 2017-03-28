<?php

define("COMPOSER_AUTOLOAD_FILE", __DIR__."/../vendor/autoload.php");

if (false === file_exists(COMPOSER_AUTOLOAD_FILE)) {
    echo "You must install the app dependencies in order to run it.";
    exit;
}

require_once COMPOSER_AUTOLOAD_FILE;

$python_address = getenv("PYTHON_APP_ADDRESS");

$client = new \GuzzleHttp\Client();
$response = $client->request("GET", $python_address);
$data = json_decode($response->getBody());

echo "PHP app executing on IP: " . gethostbyname(gethostname()) . "<br>";
echo "Python app executing on IP: " . $data->ip . "<br>";
echo "<br>";
echo "Hit counter: " . $data->counter . "<br>";
