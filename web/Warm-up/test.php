<?php  
$test = '$_="`{{{"^"?<>/";${$_}[_](${$_}[__]);';

  if(!preg_match('/[A-Za-z]/is', $test) && strlen($test) <= 60) {
    echo "test!";
  }

?>

