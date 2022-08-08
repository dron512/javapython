package com.dip.myapp.member;

public class MemberDto {

	private int id;
	private String email;
	private String name;
	private String password;
	private String regdate;
	
	public MemberDto() {}

	public MemberDto(int id, String email, String name, String password, String regdate) {
		super();
		this.id = id;
		this.email = email;
		this.name = name;
		this.password = password;
		this.regdate = regdate;
	}

	@Override
	public String toString() {
		return "MemberDto [id=" + id + ", email=" + email + ", name=" + name + ", password=" + password + ", regdate="
				+ regdate + "]";
	}



	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
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

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public String getRegdate() {
		return regdate;
	}

	public void setRegdate(String regdate) {
		this.regdate = regdate;
	}

	

}
