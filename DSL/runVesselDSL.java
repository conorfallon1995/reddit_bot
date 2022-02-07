public class runVesselDSL {

	public static void main(String[] args) {

		//Constructor for boat1, which is a vessel
		final String name = "The Flying Sheep";
		final int year = 1642;
		final String make = "Harland & Wolff";
		final int length = 182;


		Vessel boat1 = new Vessel();
		boat1.setName(name);
		boat1.setYear(year);
		boat1.setMake(make);
		boat1.setLength(length);
		String details1 = boat1.toString();
		System.out.println(details1);

	}

}