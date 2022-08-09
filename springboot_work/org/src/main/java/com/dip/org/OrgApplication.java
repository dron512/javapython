package com.dip.org;

import com.dip.org.components.AA;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class OrgApplication {

	@Bean
	public AA aa(){
		return new AA();
	}

	public static void main(String[] args) {
		SpringApplication.run(OrgApplication.class, args);
	}

}
