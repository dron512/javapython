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

    public static void newCommand(MemberDto dto){
        MemberService memberService = acac.getBean(MemberService.class);
        try {
            memberService.regist(dto);
        }catch (Exception e){
            System.out.println("email 중복됨.....넣을수 없음...");
        }
    }
    
    private static void updatecommand(String email, String oldpwd, String newpwd) {

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        acac =  new AnnotationConfigApplicationContext(ClassConfig.class);

        try {
            while (true) {
                System.out.println("1.list 2.new 3.update 4.exit");
                String cmd = br.readLine();
                if(cmd.equalsIgnoreCase("list")){
                    listCommand();
                }
                else if(cmd.startsWith("new")){
                    try {
                        String email = cmd.split(" ")[1];
                        String name = cmd.split(" ")[2];
                        String pwd = cmd.split(" ")[3];
                        MemberDto md = new MemberDto(name, email, pwd);
                        newCommand(md);
                    }catch (IndexOutOfBoundsException ie){
                        System.out.println("new aa@naver.com 김길동 1234\n이렇게 입력하세요");
                    }
                }
                else if(cmd.startsWith("update")){
                    // update aa@naver.com 1234 5678
                    try{
                        String email = cmd.split(" ")[1];
                        String oldpwd = cmd.split(" ")[2];
                        String newpwd = cmd.split(" ")[3];
                        updatecommand(email,oldpwd,newpwd);
                    }catch (Exception e){
                        System.out.println("update aa@naver.com 1234 1234\n이렇게 입력하세요");
                        System.out.println(e.toString());
                    }
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
    }


}