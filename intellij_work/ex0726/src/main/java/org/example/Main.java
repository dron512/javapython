package org.example;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static AnnotationConfigApplicationContext acac =null;
    public static void listCommand(){
        MemberService memberService = acac.getBean(MemberService.class);
        memberService.list();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        acac =  new AnnotationConfigApplicationContext(ClassConfig.class);

        try {
            while (true) {
                System.out.println("1.list 2.new aa@naver.com 3.exit");
                String cmd = br.readLine();
                if(cmd.equalsIgnoreCase("list")){
                    listCommand();
                }
                else if(cmd.startsWith("new ")){
                    //입력
                }
                else if(cmd.equalsIgnoreCase("exit")){
                    System.out.println("종료됩니다.");
                    break;
                }
            }
        }catch (Exception e){
            e.printStackTrace();
        }
        finally {
            acac.close();
        }
//        MemberDao dao = acac.getBean(MemberDao.class);
//        dao.selectAll();
//        dao.insert(new MemberDto("홍길동","aaa@Naver.com","1234"));
//        dao.selectAll();
//        dao.insert(new MemberDto("박길동","bbb@naver.com","1234"));
//        dao.selectAll();
    }
}