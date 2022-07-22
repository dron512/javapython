package org.example;

import java.util.Calendar;

class MySingle{
    public static MySingle ms;
    public static MySingle getInstane(){
        if(ms == null){
            ms = new MySingle();
            return ms;
        }else{
            return ms;
        }
    }
    public void doA(){
        System.out.println("doA");
    }
}
public class Ex06 {
    Ex06(){
        MySingle ms1 = MySingle.getInstane();
        ms1.doA();
        MySingle ms2 = MySingle.getInstane();
        ms2.doA();
        System.out.println(ms1);
        System.out.println(ms2);

        Calendar ca = Calendar.getInstance();
    }

    public static void main(String[] args) {
        new Ex06();
    }
}








