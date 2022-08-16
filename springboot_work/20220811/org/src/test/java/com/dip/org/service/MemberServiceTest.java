package com.dip.org.service;

import com.dip.org.entity.FreeBoard;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import javax.transaction.Transactional;
import java.time.LocalDateTime;

@SpringBootTest
@Transactional
public class MemberServiceTest {

    @Autowired
    MemberService memberService;

    @Autowired
    FreeBoardService freeBoardService;

    @Test
    @DisplayName("회원가입테스트")
    public void saveMemberTest(){
        freeBoardService.regist(
                FreeBoard.builder()
                        .id(1L)
                        .title("제목제목")
                        .content("내용")
                        .regdate(LocalDateTime.now().toString())
                        .build()
        );
    }
}
