package ex0624;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class BBTemp {

	public static void main(String[] args) throws FileNotFoundException {
	
		Scanner scan = new Scanner(System.in);
		
		Scanner filescan = new Scanner(new File("src"+File.separator+"a.txt"));
		
		System.out.println("입력하세요");
		String aa = scan.nextLine();
		System.out.println("aa = "+ aa);
		
		String bb = filescan.nextLine();
		System.out.println("bb = "+ bb);
		
	}
	
}
