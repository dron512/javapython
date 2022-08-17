package com.dip.dip.service;

import com.dip.dip.entity.Member;
import com.dip.dip.repository.MemberRepository;

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
