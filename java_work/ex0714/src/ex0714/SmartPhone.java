package ex0714;

public class SmartPhone extends Phone{
	
	private String ver;
	
	SmartPhone(String num,String ver){
		super(num);
//		super(num,ver);
		this.ver = ver;
	}

	@Override
	public String toString() {
		return "SmartPhone [ver=" + ver + "]";
	}

	public static void main(String[] args) {
		SmartPhone sp = new SmartPhone("1234-1234", "0.5");
		sp.doPrint();
		System.out.println(sp);
	}
}
