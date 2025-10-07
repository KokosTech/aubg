/**
 * This class is used for the implementation of the Guilds in Proj1
 *
 * @author Kaloyan Doychinov
 * @version 07/10/25
 */
public class Guild {
    private String name;
    private int members;
    private double balance;

    /* Standard constructor for objects of class Guild
     */
    public Guild() {
        this.name = "";
        this.members = 0;
        this.balance = 0.0;
    }

    /* getName - this method returns the name of the Guild
     *
     * @param nothing
     * @return String name
     */
    public String getName() {
        return this.name;
    }

    /* setName - this method sets the name of the Guild
     *
     * @param String guildName - name of the Guild
     * @return nothing
     */
    public void setName(String guildName) {
        this.name = guildName;
    }

    /* getMembers - this method returns the current number of members in the Guild
     *
     * @param nothing
     * @return int members
     */
    public int getMembers() {
        return this.members;
    }

    /* setMembers - this method sets the current number of members in the Guild
     *
     * @param int numberOfMembers - new number of members
     * @return nothing
     */
    public void setMembers(int numberOfMembers) {
        this.members = numberOfMembers;
    }

    /* getBalance - this method returns the current balance of the Guild
     *
     * @param nothing
     * @return double balance
     */
    public double getBalance() {
        return this.balance;
    }

    /* setBalance - this method sets the current balance for the Guild
     *
     * @param double payment - amount of balance left (
     * @return nothing
     */
    public void setBalance(double payment) {
        this.balance = payment;
    }
}

