package ex0707;

public class Person {
	
	private String name;
	
	// alt + shfit + s -> r setter getter
	// alt + shift + s -> o constructor
	
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String toString() {
		return "Person name = "+name;
	}
	
	public Person() {}
	public Person(String name) {
		this.name = name;
	}
}
