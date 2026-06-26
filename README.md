Port Scanner 🔍

Description
 A lightweight, custom-built Port Scanner written entirely in Python. This tool allows users to scan a specific IP address for open TCP ports within a user-defined range. It was built from scratch to demonstrate core networking concepts, socket programming, and input validation without relying on massive external network-scanning libraries.

Features
1.Custom Target Selection: Users can input any valid IPv4 address.
2.Flexible Port Ranges: Supports scanning from port 1 all the way up to 65,535.
3.Robust Input Validation: Uses the ipaddress module and Regex to ensure users enter properly formatted targets and ranges before initiating the scan.
4.Graceful Error Handling: Implements timeouts and try-except blocks to prevent the script from crashing when connections are dropped or filtered.
