<?php

require '../vendor/autoload.php';

use Cowlab\Checker\Http;

$httpChecker = new \Cowlab\Checker\Http();

$urls = [
    'https://github.com/cowlab-lugo',
    'https://sond3.com',
    'https://nonexists.github.com/cowlab-lugo',
];

foreach ($urls as $url) {

    echo $url . ' --> ';
    echo ($httpChecker->check($url)) ? 'OK' : 'FAIL';
    echo '<br>';

}
