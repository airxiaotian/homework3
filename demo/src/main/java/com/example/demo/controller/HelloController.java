package com.example.demo.controller;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/test/api")
public class HelloController {

    @RequestMapping("/hello")
    public String hello() {
        return "Hello Spring Boot1!";
    }

    @RequestMapping("/hello/{id}")
    public String hello2(@PathVariable String id) {
        return "Hello Spring Boot2!" +id;
    }

    @RequestMapping("/hello/init")
    public String hello3() {
        return "Hello Spring Boot!3";
    }
}