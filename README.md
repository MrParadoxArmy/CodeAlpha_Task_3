# Secure Coding Review
&nbsp;
&nbsp;

## Overview
This project is a Flask web application that demonstrates common security vulnerabilities and their mitigations. It serves as a guide for developers to understand secure coding practices.
&nbsp;
&nbsp;

## Table of Contents
- [Technologies Used](#technologies-used)
- [Vulnerabilities Demonstrated](#vulnerabilities-demonstrated)
  - [SQL Injection](#sql-injection)
  - [Command Injection](#command-injection)
  - [Cross-Site Scripting (XSS)](#cross-site-scripting-xss)
  - [Cross-Site Request Forgery (CSRF)](#cross-site-request-forgery-csrf)
  - [Insecure Deserialization](#insecure-deserialization)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
&nbsp;
&nbsp;

## Technologies Used
- Python
- Flask
- Flask-WTF (for CSRF protection)
- SQLAlchemy (for database interactions)
&nbsp;
&nbsp;

## Vulnerabilities Demonstrated
&nbsp;
&nbsp;

### SQL Injection
- **Vulnerable Code**: 
  ```python
  query = "SELECT * FROM users WHERE id = {}".format(user_input)  # BAD
