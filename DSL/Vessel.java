public class Vessel {

	//public toString method which will be used to demonstrate details of the Vessel object when called
	public String toString() {
		return "Name of vessel is " + this.name + ".\nThe vessel has a length of " + this.length + " metres.\nIts make is " + this.make + " and its year of manufacture was " + this.year + ".\n";
	}

	//Declare private String name along with appropriate getter and setter
	private String name;

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	//Declare private int length along with appropriate getter and setter
	private double length;

	public double getLength() {
		return length;
	}

	public void setLength(double length) {
		this.length = length;
	}

	//Declare private String make along with appropriate getter and setter
	private String make;

	public String getMake() {
		return make;
	}

	public void setMake(String make) {
		this.make = make;
	}

	//Declare private int year along with appropriate getter and setter
	private int year;

	public int getYear() {
		return year;
	}

	public void setYear(int year) {
		this.year = year;
	}
}
