package org.example;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class MyMain {
    public static void main(String[] args) {
        Greeter g1 = new Greeter();
        Greeter g2 = new Greeter();

        System.out.println(g1);
        System.out.println(g2);
        System.out.println(g1==g2);

        AnnotationConfigApplicationContext acac =
                new AnnotationConfigApplicationContext(AppContext.class);

        Greeter g3 = acac.getBean(Greeter.class);
        Greeter g4 = acac.getBean(Greeter.class);

        System.out.println(g3);
        System.out.println(g4);
        System.out.println(g3==g4);

        acac.close();
    }
}
