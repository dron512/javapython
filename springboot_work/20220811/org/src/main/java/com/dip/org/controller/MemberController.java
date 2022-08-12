package com.dip.org.controller;

import com.dip.org.entity.Member;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("member")
public class MemberController {

    @GetMapping("")
    public String index(){
        return "member/member";
    }

    @PostMapping("insert")
    public String insert(Member member){
        System.out.println("일로온다...");
        System.out.println(member);
        return "index";
    }
}
