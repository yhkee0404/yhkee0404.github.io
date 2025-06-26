rootProject.name = "yhkee0404"

include("spring-boot")
project(":spring-boot").projectDir = file("bases/spring-boot")
include("spring-boot-greetapi")
project(":spring-boot-greetapi").projectDir = file("components/spring-boot-greetapi")

include("spring-boot-greet-project")
project(":spring-boot-greet-project").projectDir = file("projects/spring-boot-greet-project")
