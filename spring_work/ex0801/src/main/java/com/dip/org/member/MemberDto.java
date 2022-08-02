package com.dip.org.member;

public class MemberDto {
	private String name;
	private String email;
	private String pwd;
	
	@Override
	public String toString() {
		return "MemberDto [name=" + name + ", email=" + email + ", pwd=" + pwd + "]";
	}
	// 기본생성자는 직접 적어야함...
	public MemberDto() {}
	
	public MemberDto(String name, String email, String pwd) {
		super();
		this.name = name;
		this.email = email;
		this.pwd = pwd;
	}
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public String getPwd() {
		return pwd;
	}
	public void setPwd(String pwd) {
		this.pwd = pwd;
	}
	
	//alt+ shfit +s ->r , o , s

	
}
