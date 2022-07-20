package org.example;

class Point implements Cloneable{
    int xPos,yPos;
    public Point(int xPos, int yPos) {
        this.xPos = xPos;
        this.yPos = yPos;
    }
    @Override
    public String toString() {
        return "Point{" +
                "xPos=" + xPos +
                ", yPos=" + yPos +
                '}';
    }
    @Override
    protected Object clone() throws CloneNotSupportedException {
        return super.clone();
    }
}

public class Ex02 {
    public static void main(String[] args) {
        Point org = new Point(10,20);
        Point cpy;

        try {
            cpy = (Point) org.clone();
        } catch (CloneNotSupportedException e) {
            throw new RuntimeException(e);
        }

        System.out.println(org);
        System.out.println(cpy);
        org.xPos = 20;
        System.out.println(org);
        System.out.println(cpy);
    }
}









