# Inactive Switchport Report

A tool that displays cisco switchport not used for a days period defined

## Installation

Require's Python & Netmiko
```
apt-get update
apt-get install python -y
apt-get install build-essential libssl-dev libffi-dev -y
apt-get install python-pip -y
pip install cryptography
pip install netmiko
```

## Usage

Pretty simple to run, as per the following - 

```
$ ./portsinactive.py

Enter your username: ivan
Password:
Enter IP address: 192.168.1.10
Enter days of inactive port: 90
```

## Development

## References

## To do
