package ex0711;

public class Accumulator {
	
	public static int MAX =345;
	
	private int sum = 0;

	public void add(int i) {
		sum = sum + i;
	}

	public void showResult() {
		System.out.println("sum = "+sum);
		
	}


}
