FROM openjdk:22

WORKDIR /app

ENV SPRING_PROFILES_ACTIVE=local

COPY target/monkey-consulting-0.0.1-SNAPSHOT.jar /app/monkey-consulting.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "monkey-consulting.jar"]
