package com.dip.org.req;

// 유효성검사 validation
// form 저장버튼을 눌렀을시에
// 글의 내용, 글의 제목이 없을시 다시 입력받도록 유도하는기능

import lombok.Getter;
import lombok.Setter;

import javax.validation.constraints.NotEmpty;

@Getter
@Setter
public class FreeBoardReq {

    private Long id;

    @NotEmpty
    private String title;
    @NotEmpty
    private String content;

    private String regdate;

}
