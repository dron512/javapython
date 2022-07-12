package ex0712;

import java.util.Scanner;

public class Ex03 {

	public static void main(String[] args) {
		String a = "3\n 5 7";
		Scanner scan = new Scanner(a);

		int num1 = scan.nextInt();
		int num2 = scan.nextInt();
		int num3 = scan.nextInt();

		System.out.println(num1 + num2 + num3);
	}
}
