package com.dip.org.service;

import com.dip.org.entity.Member;
import com.dip.org.repository.MemberRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;

@Service
public class MemberService {

    @Autowired
    MemberRepository memberRepository;

    public void regist(Member member) {
        member.setRegdate(LocalDateTime.now());
        memberRepository.save(member);
    }
}
