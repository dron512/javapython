package com.dip.org.service;

import com.dip.org.entity.FreeBoard;
import com.dip.org.repository.FreeBoardRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class FreeBoardService {

    @Autowired
    FreeBoardRepository freeBoardRepository;

    public void regist(FreeBoard freeBoard){
        freeBoardRepository.save(freeBoard);
    }

    public List<FreeBoard> selectlist() {
        return freeBoardRepository.findAll();
    }
}
