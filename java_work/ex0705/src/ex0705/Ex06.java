package ex0705;

public class Ex06 {

	public static void main(String[] args) {
		BankAccount a1 = new BankAccount("850511", "1234-1234", 1000);
		a1.deposit(2000);
		a1.printbal();
		
		BankAccount a2 = new BankAccount();
	}
}
