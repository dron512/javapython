package ex0711;

public class BB {

	int a = 10;
	BB(){
		this(20);
		System.out.println("기본생성자");
	}
	
	BB(int a){
		System.out.println("a생성자");
		this.a = a;
	}

	@Override
	public String toString() {
		return "BB [a=" + this.a + "]";
	}

	// alt +shift + s -> s
	
	
}
