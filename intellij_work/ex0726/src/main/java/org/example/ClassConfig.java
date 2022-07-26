package org.example;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ClassConfig {

    @Bean
    public MemberDao memberDao(){
        return new MemberDao();
    }

    // 생성자에 의한 DI방식
//    @Bean
//    public MemberService memberService(){
//        return new MemberService(memberDao());
//    }
    // setter에 의한 DI 방식
    @Bean
    public MemberService memberService(){
        MemberService ms = new MemberService();
        ms.setMemberDao(memberDao());
        return ms;
    }
}
