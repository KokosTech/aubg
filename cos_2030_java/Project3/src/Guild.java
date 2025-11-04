public class Guild {
    private static int allCredits = 0;
    private String name;
    private int approved;
    private int carry;

    public Guild() {
        this.name = "";
        this.approved = 0;
        this.carry = 0;
    }

    public Guild(String name) {
        this();
        this.name = name;
    }

    public static int getAllCredits() {
        return allCredits;
    }

    public String getName() {
        return this.name;
    }

    public int getApproved() {
        return this.approved;
    }

    public int getCarry() {
        return this.carry;
    }

    public void addCredits(int approved) {
        if (approved < 0) {
            System.out.println("A credit must be a non-negative number!");
            return;
        }

        this.approved += approved;
        allCredits += approved;
    }

    public void addCarry(int notApproved) {
        this.carry += notApproved;
    }
}
