/**
 * This class is used for managing the credit accounts of a guild
 *
 * @author Kaloyan Doychinov
 * @version 04/11/25
 */
public class Guild {
    private static int allCredits = 0;
    private String name;
    private int approved;
    private int carry;

    /**
     * Standard constructor for objects of class Guild
     */
    public Guild() {
        this.name = "";
        this.approved = 0;
        this.carry = 0;
    }

    /**
     * Parameter constructor for objects of class Guild
     *
     * @param name String - name for the guild
     */
    public Guild(String name) {
        this();
        this.name = name;
    }

    /**
     * this STATIC method returns the approved credit of all registered guilds
     *
     * @return int - amount of total approved credit
     */
    public static int getAllCredits() {
        return allCredits;
    }

    /**
     * this method returns the guild's name
     *
     * @return String - name of the guild
     */
    public String getName() {
        return this.name;
    }

    /**
     * this method returns the current amount of approved credit
     *
     * @return int - amount of approved credit
     */
    public int getApproved() {
        return this.approved;
    }

    /**
     * this method returns the current amount of carry credit
     *
     * @return int - amount of carry credit
     */
    public int getCarry() {
        return this.carry;
    }

    /**
     * this method adds a specified amount to the approved credit
     *
     * @param approved int - amount of newly approved credit
     */
    public void addCredits(int approved) {
        if (approved < 0) {
            System.out.println("A credit must be a non-negative number!");
            return;
        }

        this.approved += approved;
        allCredits += approved;
    }

    /**
     * this method adds a specified amount to the carry credit
     * (since we're not supposed to change anything in this class -
     * I have not added the option to choose if it's negative in order to set it to zero)
     *
     * @param notApproved int - credit to be added to carry credit
     */
    public void addCarry(int notApproved) {
        this.carry += notApproved;
    }
}
