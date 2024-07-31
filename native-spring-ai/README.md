# Native Spring AI Example

[![Java](https://img.shields.io/badge/Java-17-blue.svg)](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html)
[![GraalVM](https://img.shields.io/badge/GraalVM-22.3.r17--grl-brightgreen.svg)](https://www.graalvm.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-%23412991?logo=openai&logoColor=white)](https://www.graalvm.org/)

This project demonstrates how to implement  in GraalVM for Java applications using the Truffle API and Espresso project. It provides a secure environment for executing Java code by leveraging GraalVM's capabilities, ensuring that the execution is contained within a sandbox.

This is a OCI learning recommendation service built with Spring AI, OpeAI, and GraalVM. The base is a regular Spring app, and the integration with OpenAI is implemented in `RecommendationLearning`. Note that the app is using `OPENAI_API_KEY`.

## Change a valid Open API key on application.properties:
spring.ai.openai.api-key=${OPENAI_API_KEY}

## Build a native app with GraalVM:

```shell
mvn -Pnative native:compile -DskipTests
```

## Start the app and navigate to the learning request form:

```shell
./target/learningapp http://localhost:8080/
```

After submitting your preferences, you'll get a generated recommendation – for example:

```
Here is your learning path recommendation!🤓

Based on your preferences for the role of Database Administrator and your interest in Oracle Database, I recommend the following course and certification: Course: Oracle Database Administration Workshop This course provides a comprehensive introduction to Oracle Database administration.

It covers essential concepts and techniques for managing and administering an Oracle database, including installation, configuration, backup and recovery, and performance tuning. Certification: Oracle Certified Professional, Oracle Database 12c Administrator (OCP) This certification validates your skills and knowledge in Oracle Database administration.

It demonstrates your ability to manage a robust and efficient Oracle Database infrastructure, making you a valuable asset to any organization. These options will provide you with the necessary foundation and credentials to excel in your role as a Database Administrator specializing in Oracle Database.

Enjoy your study!👋
```
