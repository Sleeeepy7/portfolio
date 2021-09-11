<?php

$EmailFrom = "vadim@owl-design.net";
$EmailTo = "vadim@owl-design.net";
$Subject = "Subscription Signup";
$Email = trim(stripslashes($_POST['email'])); 

// validation
$validationOK=true;
if (!$validationOK) {
  print "<meta http-equiv=\"refresh\" content=\"0;URL=error.htm\">";
  exit;
}

// prepare email body text
$Body = "";
$Body .= "Email: ";
$Body .= $Email;

// send email 
$success = mail($EmailTo, $Subject, $Body, "From: <$EmailFrom>");

// redirect to success page 
if ($success){
  print "success";
}
else{
  print "error";
}
?>