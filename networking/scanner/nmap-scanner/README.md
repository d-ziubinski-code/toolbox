# Nmap Scanner

Simple Python script for scanning TCP ports using Nmap.

## Features

* TCP port scanning
* Nmap service detection
* Custom target host
* Open port extraction

## Requirements

* Python 3
* Nmap

## Usage

Run:

```bash
python scanner.py
```

The scanner checks ports:

```text
31000-32000
```

on:

```text
localhost
```

## Example

```text
31046/tcp open  echo
31518/tcp open  ssl/echo
31691/tcp open  echo
31790/tcp open  ssl/unknown
31960/tcp open  echo
```

## How it works

The script runs Nmap using Python's `subprocess` module, reads the output and extracts lines containing open ports.

```text
Python
  │
  ▼
Nmap
  │
  ▼
stdout
  │
  ▼
Open ports
```

## Purpose

Created while solving OverTheWire Bandit Level 16 to automate part of the network enumeration process.
