package org.example;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Import;

@Configuration
@Import(ImportConfig.class)
public class ClassConfig {
    @Bean
    public MemberService memberService(){
        MemberService ms = new MemberService();
        return ms;
    }
}
