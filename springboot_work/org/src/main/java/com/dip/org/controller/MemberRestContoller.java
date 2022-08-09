package com.dip.org.controller;

import com.dip.org.dto.MemberDto;
import org.mybatis.spring.SqlSessionTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("rest")
public class MemberRestContoller {

    @Autowired
    SqlSessionTemplate sqlSessionTemplate;

    // 127.0.0.1:8080/rest/member
    @GetMapping("member")
    public String member(){
        List<MemberDto> list = sqlSessionTemplate.selectList("member.select");
        System.out.println(list);
        return "member";
    }
}
