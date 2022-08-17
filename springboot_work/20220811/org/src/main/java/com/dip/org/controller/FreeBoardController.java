package com.dip.org.controller;

import com.dip.org.entity.FreeBoard;
import com.dip.org.req.FreeBoardReq;
import com.dip.org.service.FreeBoardService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;

import javax.validation.Valid;
import java.io.File;
import java.time.LocalDateTime;
import java.util.List;

@Controller
public class FreeBoardController {

    @Autowired
    private FreeBoardService freeBoardService;

    @GetMapping("freeboard")
    public String freeboard(Model model){

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

        List<FreeBoard> list =
                freeBoardService.selectlist();

        model.addAttribute("list",list);
        System.out.println(list);

        return "freeboard/freeboard";
    }

    @GetMapping("freeboard/write")
    public String write(FreeBoardReq freeBoardReq){
        return "freeboard/write";
    }

    @PostMapping("freeboard/write")
    public String pwrite(@Valid FreeBoardReq freeBoardReq, BindingResult bindingResult,@RequestParam("file") MultipartFile file){

        if(bindingResult.hasErrors()){
            return "freeboard/write";
        }

        freeBoardService.regist(
                FreeBoard.builder()
//                        .id(-1L)
                        .content(freeBoardReq.getContent())
                        .title(freeBoardReq.getTitle())
                        .regdate(LocalDateTime.now().toString())
                        .build()
        );

        String fileName = file.getOriginalFilename();
        try {
            file.transferTo( new File("D:\\upload\\" + fileName));
        } catch (Exception e) {
            e.printStackTrace();
        }

        return "redirect:/freeboard";
    }
}
