package com.yhkee0404.spring;

import java.util.Optional;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.lang.Nullable;

@SpringBootApplication
public class BootApplication {

    private static final Logger logger = LoggerFactory.getLogger(BootApplication.class);

    @Value("${spring.application.name:#{null}}")
    @Nullable
    private String appName;

    public static void main(String[] args) {
        var context = SpringApplication.run(BootApplication.class, args);
        var app = context.getBean(BootApplication.class);
        logger.info(
                "Application name: {}",
                Optional.ofNullable(app.appName)
                        .orElse("<not set>"));
    }
}
