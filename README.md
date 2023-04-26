# Script-Web-App
Script for automatic checking for vulnerabilities in web applications

#Script for Automatic Vulnerability Testing in Web Applications


This Python script uses the OWASP ZAP tool for automatically checking for vulnerabilities in web applications.
It can be used for security testing of web applications and detecting vulnerabilities that can be exploited by attackers.

#Usage

To use this script, you need to install the zapv2 library via pip and run the ZAP proxy locally (e.g., on port 8080).
In the "target" string, you should specify the URL of the target website that you want to test for vulnerabilities.
The script will automatically start scanning and output the results to the console.


Note that this script uses only basic scan settings, 
and additional parameters can be configured for a more comprehensive analysis, such as a list of scanners, scan depth, etc.
