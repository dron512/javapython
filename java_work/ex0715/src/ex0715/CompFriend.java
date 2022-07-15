package ex0715;

public class CompFriend extends Friend {
	private String department;
	public CompFriend(String name, String department, String phone) {
		super(name,phone);
		this.department = department;
	}
	public void showInfo() {
		super.showInfo();
		System.out.println("회사 = "+department);
	}
}
