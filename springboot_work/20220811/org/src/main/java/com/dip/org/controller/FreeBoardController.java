package com.dip.org.controller;

import com.dip.org.entity.FreeBoard;
import com.dip.org.service.FreeBoardService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

import java.time.LocalDateTime;

@Controller
public class FreeBoardController {

    @Autowired
    private FreeBoardService freeBoardService;

    @GetMapping("freeboard")
    public String freeboard(){

        freeBoardService.regist(
                FreeBoard.builder()
                        .id(1L)
                        .title("제목제목")
                        .content("내용")
                        .regdate(LocalDateTime.now().toString())
                        .build()
        );

        freeBoardService.regist(
                FreeBoard.builder()
                        .id(2L)
                        .title("123제목123제목")
                        .content("내용22")
                        .regdate(LocalDateTime.now().toString())
                        .build()
        );


        return "freeboard/freeboard";
    }

}
