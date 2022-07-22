package org.example;

import org.springframework.stereotype.Component;

import java.util.Random;

@Component
public class Ex03 {
    public static void main(String[] args) {
        System.out.println(System.currentTimeMillis());
        Random random = new Random();
        System.out.println("밀리세컨드 랜덤 시작");
        for (int i =0; i<10;i++){
            System.out.println(random.nextInt(100));
        }
        System.out.println("밀리세컨드 랜덤 끝");

        Random randomseed = new Random(42);
        System.out.println("씨드 랜덤 시작");
        for (int i =0; i<10;i++){
            System.out.println(randomseed.nextInt(100));
        }
        System.out.println("씨드 랜덤 끝");

    }
}
