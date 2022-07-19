package org.example;

import java.util.Scanner;

class AgeReadException extends Exception{
    public AgeReadException() {
        super("유효한 나이를 입력하세요");
    }
}
public class Main {
    Main() throws AgeReadException {
        Scanner scan = new Scanner(System.in);
        System.out.println("나이를 입력하세요");
        int age = scan.nextInt();

        if(age<0)
            throw new AgeReadException();
    }
    public static void main(String[] args) {
        try {
            new Main();
        } catch (AgeReadException e) {
            System.out.println(e);
        }
    }
}