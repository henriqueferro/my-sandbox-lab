# Native Spring AI & GraalVM Demo Application

[![Java](https://img.shields.io/badge/Java-22-red.svg)](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html)
[![GraalVM](https://img.shields.io/badge/GraalVM-20-darkblue.svg)](https://www.graalvm.org/)
[![SpringAI](https://img.shields.io/badge/SpringAI-0.8.1-green.svg)](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html)
[![OpenAI](https://img.shields.io/badge/OpenAI-%23412991?logo=openai&logoColor=white)](https://www.graalvm.org/)

This is a OCI learning recommendation service built with Spring AI, OpeAI, and GraalVM. The base is a regular Spring app, and the integration with OpenAI is implemented in `RecommendationLearning`. Note that the app is using `OPENAI_API_KEY`.

## Table of Contents
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Contributing](#contributing)

## Technologies Used

- **Java 22**: The project uses Java 22 as the programming language.
- **GraalVM 20**: The project uses GraalVM to execute Java bytecode.
- **Spring AI 0.8.1**: Spring AI is an application framework for AI engineering.
- **Open AI**: OpenAI is an artificial intelligence to use as Model on Spring AI.

## Prerequisites

- **GraalVM**: Install GraalVM via BREW with the following command:
  ```sh
  brew install --cask graalvm-jdk
  ```
- **OPENAI_API_KEY**: Change a valid Open API key on application.properties file:
  ```
  spring.ai.openai.api-key=${OPENAI_API_KEY}
  ```

## Features

- Demo and Test Spring AI execution
- Application example for OCI Courses and Cetifications
- Utilization of GraalVM's polyglot capabilities

## Setup Instructions
* Build the project:
  ```shell
  cd native-spring-ai

  mvn -Pnative native:compile -DskipTests
  ```
* Run the application:
  ```shell
  ./target/learningapp http://localhost:8080/
  ```
* Open into your browser the request form:
  http://localhost:8080

## Usage
After submitting your preferences, you'll get a generated recommendation – for example:

```
Here is your learning path recommendation!🤓

Based on your preferences for the role of Database Administrator and your interest in Oracle Database, I recommend the following course and certification: Course: Oracle Database Administration Workshop This course provides a comprehensive introduction to Oracle Database administration.

It covers essential concepts and techniques for managing and administering an Oracle database, including installation, configuration, backup and recovery, and performance tuning. Certification: Oracle Certified Professional, Oracle Database 12c Administrator (OCP) This certification validates your skills and knowledge in Oracle Database administration.

It demonstrates your ability to manage a robust and efficient Oracle Database infrastructure, making you a valuable asset to any organization. These options will provide you with the necessary foundation and credentials to excel in your role as a Database Administrator specializing in Oracle Database.

Enjoy your study!👋
```

## Contributing
Contributions are welcome! 
Please open an issue or submit a pull request with your improvements.
