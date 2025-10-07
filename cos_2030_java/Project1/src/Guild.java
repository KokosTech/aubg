/** This class is used for the implementation of the Guilds in Proj1
 *
 *  @author  Kaloyan Doychinov
 *  @version 07/10/25
 */
public class Guild {
    private String name;
    private int members;
    private double balance;

    public Guild() {
        this.name = "";
        this.members = 0;
        this.balance = 0.0;
    }

    public String getName() {
        return this.name;
    }

    public int getMembers() {
        return this.members;
    }

    public double getBalance() {
        return this.balance;
    }

    public void setName(String guildName) {
        this.name = guildName;
    }

    public void setMembers(int numberOfMembers) {
        this.members = numberOfMembers;
    }

    public void setBalance(double payment) {
        this.balance = payment;
    }
}

