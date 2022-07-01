package ex0701;

public class Ex10 {
	/*
	 * factorial(3)
	 * 3*factorial(2)
	 * 3*2*factorial(1)
	 * 3*2*1
	 * 
	 * factorial(6)
	 * 6*factorial(5)
	 * 6*5*factorial(4)
	 * 6*5*4*factorial(3)
	 * 6*5*4*3*factorial(2)
	 * 6*5*4*3*2*factorial(1)
	 * 6*5*4*3*2*1
	 */
	
	public static int factorial(int n) {
		if (n == 1) {
			return 1;
		} else {
			return n * factorial(n - 1);
		}
	}

	public static void main(String[] args) {
		System.out.println(factorial(3));
		System.out.println(factorial(6));
	}
}
