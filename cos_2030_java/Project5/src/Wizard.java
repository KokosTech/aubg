/**
 * This class is used for the Wizard - subclass of Individual, which also implements the Magical interface
 *
 * @author Kaloyan Doychinov
 * @version 02/12/25
 */
public class Wizard extends Individual implements Magical {
    private String title;
    private int level;

    /**
     * Standard constructor for objects of class Wizard
     */
    public Wizard() {
        super();
        this.title = "";
        this.level = 0;
    }

    /**
     * Parameter constructor for objects of class Wizard
     *
     * @param name       String - name for the wizard
     * @param location   String - location of the wizard
     * @param profession String - profession of the wizard
     * @param title      String - title of the wizard
     * @param level      int - level of the Wizard
     */
    public Wizard(String name, String location, String profession, String title, int level) {
        super(name, location, profession);
        this.title = title;
        this.level = level;
    }

    /**
     * this method overrides the Magical interface to output the info of the wizard
     */
    @Override
    public void assess() {
        System.out.printf("Level %d %s, %s%n", this.level, super.toString(), this.title);
    }
}
