package ex0715;

public class UniFriend extends Friend{
	private String major;
	public UniFriend(String name, String major, String phone) {
		super(name,phone);
		this.major = major;
	}
	public void showInfo() {
		super.showInfo();
		System.out.println("전공 = "+major);
	}
}
