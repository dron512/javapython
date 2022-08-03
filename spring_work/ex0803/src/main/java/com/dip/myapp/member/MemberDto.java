package com.dip.myapp.member;

public class MemberDto {

	private String email;
	private String name;
	private String pwd;
	
	//기본생성자는 직접 적어야함..
	// alt + shift + s -> o 생성자
	// alt + shift + s -> r getter setter
	// alt + shift + s -> s toString
	public MemberDto() {}

	public MemberDto(String email, String name, String pwd) {
		super();
		this.email = email;
		this.name = name;
		this.pwd = pwd;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getPwd() {
		return pwd;
	}

	public void setPwd(String pwd) {
		this.pwd = pwd;
	}

	@Override
	public String toString() {
		return "MemberDto [email=" + email + ", name=" + name + ", pwd=" + pwd + "]";
	}

}
