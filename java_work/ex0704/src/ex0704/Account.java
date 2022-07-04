package ex0704;

public class Account {
	int bal = 0;

	public void deposit(int te) {
		bal += te;
	}

	public void with(int te) {
		bal -= te;
	}

	public void check() {
		System.out.println("bal = " + bal);
	}
}
