plugins {
	java
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

tasks.jar {
    enabled = false
}
