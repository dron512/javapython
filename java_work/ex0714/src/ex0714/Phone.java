package ex0714;

public class Phone {

	protected String num;
	
	public Phone(String num) {
		this.num = num;
	}
	
	public void doPrint() {
		System.out.println("num = "+ num);
	}
}
