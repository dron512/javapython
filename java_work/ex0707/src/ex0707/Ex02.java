package ex0707;

import zoo.Duck;

public class Ex02 {
	public static int a = 10;
	Ex02(){
		zoo.Dog dog = new zoo.Dog();
		zoo.Cat cat = new zoo.Cat();
		Duck duck = new Duck();
		sound(dog, cat, duck);
	}
	public void sound(zoo.Dog dog,zoo.Cat cat,Duck duck) {
		dog.sound();
		cat.sound();
		duck.sound();
	}
	public static void main(String[] args) {
		new Ex02();
	}
	
}
