package org.example;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ImportConfig {

    @Bean
    public MemberDao memberDao(){
        return new MemberDao();
    }
    @Bean MemberPrinter memberPrinter(){
        return new MemberPrinter("1.0");
    }
}
