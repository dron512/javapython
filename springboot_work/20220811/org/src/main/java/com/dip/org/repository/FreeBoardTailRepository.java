package com.dip.org.repository;

import com.dip.org.entity.FreeBoard;
import com.dip.org.entity.FreeBoardTail;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface FreeBoardTailRepository extends JpaRepository<FreeBoardTail,Long> {
}
