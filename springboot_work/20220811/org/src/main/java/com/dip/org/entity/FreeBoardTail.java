package com.dip.org.entity;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;

@Entity
@Getter
@Setter
public class FreeBoardTail {

    private long board_id;

    @Id
    @Column(name = "id", nullable = false)
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String t_name;
    @Column(columnDefinition = "TEXT")
    private String t_content;

}
