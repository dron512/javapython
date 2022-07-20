package org.example;

import java.util.Objects;

class INum{
    int num;
    // alt + insert
    public INum(int num) {
        this.num = num;
    }
    public int getNum() {
        return num;
    }
    public void setNum(int num) {
        this.num = num;
    }
    @Override
    public boolean equals(Object o) {
        INum iNum = (INum) o;
        return this.num == iNum.num;
    }
}
public class Ex01 {
    public static void main(String[] args) {
        INum iNum1 = new INum(10);
        INum iNum2 = new INum(10);
        INum iNum3 = new INum(12);
        System.out.println(iNum1==iNum2);
        System.out.println(iNum1);
        System.out.println(iNum2);

        System.out.println(iNum1.equals(iNum2));
        System.out.println(iNum1.equals(iNum3));
    }
}
