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
	implementation("org.springframework.boot:spring-boot-starter-web")
	testImplementation("org.springframework.boot:spring-boot-starter-test")
	testRuntimeOnly("org.junit.platform:junit-platform-launcher")
	
	implementation(project(":spring-boot"))
	implementation(project(":spring-boot-greetapi"))
}

tasks.withType<Test> {
	useJUnitPlatform()
}

tasks.jar {
    enabled = false
}

tasks.bootJar {
    enabled = false
}

springBoot {
    mainClass = "com.yhkee0404.spring.BootApplication"
}
