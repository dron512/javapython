package com.dip.dip.member;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class MemberConfig {

	@Bean
	public MemberDao memberDao() {
		return new MemberDao();
	}
	
}
