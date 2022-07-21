package org.example;

import java.util.Arrays;

public class Ex05 {

    public static void main(String[] args) {
        int a[] = {10, 20, 30, 40, 50};
        int b[] = Arrays.copyOf(a, 3);

        for (int item : a) {
            System.out.println(item);
        }
        System.out.println("a출력끝");
        for (int item : b) {
            System.out.println(item);
        }
        System.out.println("b출력끝");

        Arrays.stream(a).forEach(item -> System.out.println(item));


    }
}
