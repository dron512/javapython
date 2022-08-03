package com.dip.myapp.member;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class MemberController {

	@Autowired
	MemberService memberService;

	@GetMapping("insert")
	public String insert() {
		memberService.regist(new MemberDto("aa@naver.com","홍길동","1234"));
		memberService.regist(new MemberDto("bb@naver.com","박길동","1234"));
		
		System.out.println("insert");
		return "insert";
	}
	
	@GetMapping("select")
	public String select() {
		System.out.println("select");
		return "select";
	}
	
}
