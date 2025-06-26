plugins {
	java
	id("org.springframework.boot") version "3.4.7"
	id("io.spring.dependency-management") version "1.1.7"
}

group = "com.yhkee0404"
version = "0.0.1-SNAPSHOT"

java {
	toolchain {
		languageVersion = JavaLanguageVersion.of(21)
	}
}

repositories {
	mavenCentral()
}

dependencies {
	implementation(project(":spring-boot"))
	implementation(project(":spring-boot-greetapi"))
}

tasks.withType<Test> {
	useJUnitPlatform()
}

springBoot {
    mainClass.set("com.yhkee0404.spring.BootApplication")
}

tasks.jar {
    enabled = false
}

tasks.bootJar {
    // enabled = false
}
