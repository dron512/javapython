package com.dip.myapp.member;

import javax.servlet.http.HttpServletRequest;

import org.mybatis.spring.SqlSessionTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import com.dip.myapp.staticm.StaticM;

@Controller
public class MemberController {

	@Autowired
	MemberService memberService;

	@Autowired
	SqlSessionTemplate sql;

	@GetMapping("insert")
	public String insert(Model model) {
		model.addAttribute("serverTime", StaticM.getDateFormat());
		return "insert";
	}

	@PostMapping("insert")
	public String pinsert(Model model, HttpServletRequest request) {
		String email = request.getParameter("email");
		String name = request.getParameter("name");
		String pwd = request.getParameter("pwd");
		model.addAttribute("serverTime", StaticM.getDateFormat());
		memberService.regist(new MemberDto(0, email, name, pwd, null));
		return "insert";
	}

	@GetMapping("select")
	public String select(Model model) {
		model.addAttribute("serverTime", StaticM.getDateFormat());
		model.addAttribute("list", sql.selectList("member.selectall"));
		return "select";
	}

}
