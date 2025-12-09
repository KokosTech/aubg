/**
 * This class is used for the Witch - subclass of Individual, which also implements the Magical interface
 *
 * @author Kaloyan Doychinov
 * @version 02/12/25
 */
public class Witch extends Individual implements Magical {
    private boolean active;
    private int skill;
    private int friendly;

    /**
     * Standard constructor for objects of class Witch
     */
    public Witch() {
        super();

        this.active = false;
        this.skill = 0;
        this.friendly = 0;
    }


    /**
     * Parameter constructor for objects of class Witch
     *
     * @param name       String - name for the Witch
     * @param location   String - location of the Witch
     * @param profession String - profession of the Witch
     * @param active     boolean - whether it's active or not - printing depends on it
     * @param friendly   int - measures how friendly the witch is
     * @param skill      int - how skillful the witch is
     */
    public Witch(String name, String location, String profession, boolean active, int friendly, int skill) {
        super(name, location, profession);

        this.active = active;
        this.skill = skill;
        this.friendly = friendly;
    }

    /**
     * this method overrides the Magical interface to output the info of the witch
     */
    @Override
    public void assess() {
        String status = "";

        if (this.active) {
            if (this.friendly > 0) {
                status = "friendly";
            } else if (this.friendly < 0) {
                status = "hostile";
            } else {
                status = "may need convincing";
            }
        } else {
            status = "not active";
        }

        System.out.printf("(%s) skill level %d/10 %s%n", status, this.skill, super.toString());
    }
}
