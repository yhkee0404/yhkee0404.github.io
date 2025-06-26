package com.yhkee0404.spring.greetapi;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GreetApiController {

    @GetMapping("/hello")
    public String helloWorld() {
        return "HELLO WORLD";
    }
}
