# Native Spring AI

This is a learning recommendation service built with Spring AI, OpeAI, and GraalVM. The base is a regular Spring app, and the integration with OpenAI is implemented in `RecommendationLearning`. Note that the app is using `OPENAI_API_KEY`.

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
