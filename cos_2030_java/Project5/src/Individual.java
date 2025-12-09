/**
 * This class is used for the superclass Individual
 *
 * @author Kaloyan Doychinov
 * @version 02/12/25
 */
public class Individual implements Comparable<Object> {
    private String name;
    private String location;
    private String profession;

    /**
     * Standard constructor for objects of class Individual
     */
    public Individual() {
        this.name = "";
        this.location = "";
        this.profession = "";
    }

    /**
     * Parameter constructor for objects of class Wizard
     *
     * @param name       String - name for the Individual
     * @param location   String - location of the Individual
     * @param profession String - profession of the Individual
     */
    public Individual(String name, String location, String profession) {
        this.name = name;
        this.location = location;
        this.profession = profession;
    }

    /**
     * standard getter for location
     *
     * @return String - location
     */
    public String getLocation() {
        return this.location;
    }

    /**
     * overridden function from Object used to create a string from the object by concatenating profession and name
     *
     * @return String - concatenated output
     */
    @Override
    public String toString() {
        return this.profession + " " + this.name;
    }

    /**
     * overridden function from Object used to compare 2 Individuals based on name - used to implement sorting
     *
     * @param o the object to be compared.
     * @return int - number of diff
     */
    @Override
    public int compareTo(Object o) {
        if (!(o instanceof Individual)) return Integer.MIN_VALUE;
        return this.name.compareTo(((Individual) o).name);
    }
}
