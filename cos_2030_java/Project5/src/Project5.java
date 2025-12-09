import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.NoSuchElementException;
import java.util.Scanner;

import static java.lang.System.exit;

/**
 * Package private class used to run the program and keep track of the file and read items
 *
 * @author Kaloyan Doychinov
 * @version 02/12/25
 */
class Runner {
    private Scanner listFile;

    // preferably it would've been a Map with Arrays as values, and locations as keys - but we haven't officially studied them
    private ArrayList<Individual> individuals;
    private ArrayList<String> locations;

    /**
     * Standard constructor for objects of class Runner
     */
    Runner() {
        this.listFile = openFile("list.txt");
        this.individuals = new ArrayList<>();
        this.locations = new ArrayList<>();
    }

    /**
     * openFile - this helper method moves the program's logic for opening files
     *
     * @param filename String - path to file
     */
    private Scanner openFile(String filename) {
        try {
            File sff = new File(filename);
            return new Scanner(sff);
        } catch (FileNotFoundException e) {
            System.out.println("The file " + filename + " does not exist. Exiting...");
            exit(-1);
            return null;
        }
    }

    /**
     * handleExit - this helper method closes gracefully the file stream before exiting the program
     *
     * @param exitCode int - pass-trough value to exit()
     */
    private void handleExit(int exitCode) {
        this.listFile.close();
        exit(exitCode);
    }

    /**
     * handleWizard - this helper method is used to read and create a Wizard
     */
    private void handleWizard() {
        try {
            String name = this.listFile.nextLine();
            String location = this.listFile.nextLine();

            String position = this.listFile.nextLine();
            int level = this.listFile.nextInt();
            this.listFile.nextLine();

            if (!locations.contains(location))
                locations.add(location);
            this.individuals.add(new Wizard(name, location, "Wizard", position, level));
        } catch (NoSuchElementException e) {
            System.out.println("Broken input for Wizard");
            handleExit(-2);
        }
    }

    /**
     * handleWitch - this helper method is used to read and create a Witch
     */
    private void handleWitch() {
        try {
            String name = this.listFile.nextLine();
            String location = this.listFile.nextLine();

            boolean active = (this.listFile.nextLine().trim()).equalsIgnoreCase("YES");
            int skill = this.listFile.nextInt();
            this.listFile.nextLine();
            int friendliness = this.listFile.nextInt();
            this.listFile.nextLine();

            if (!locations.contains(location))
                locations.add(location);
            this.individuals.add(new Witch(name, location, "Witch", active, friendliness, skill));
        } catch (NoSuchElementException e) {
            System.out.println("Broken input for Witch");
            handleExit(-3);
        }
    }

    /**
     * * handleWitch - this helper method is used to read and create an Individual with a diff profession
     *
     * @param profession String - profession only to be passed to the object creation
     */
    private void handleOthers(String profession) {
        try {
            String name = this.listFile.nextLine();
            String location = this.listFile.nextLine();

            if (!locations.contains(location))
                locations.add(location);
            this.individuals.add(new Individual(name, location, profession));
        } catch (NoSuchElementException e) {
            System.out.println("Broken input for Other Professions");
            handleExit(-4);
        }
    }

    /**
     * print - this helper method is used to beautifully print and divide by locations - individuals, wizards, and witches
     */
    private void print() {
        locations.sort(String::compareTo);
        individuals.sort(Individual::compareTo);

        System.out.println("List of friends and possible allies:");

        for (String location : locations) {
            System.out.printf("In %s:%n", location);
            for (Individual individual : individuals) {
                if (individual.getLocation().equalsIgnoreCase(location)) {
                    System.out.print(" - ");
                    if (individual instanceof Magical) {
                        ((Magical) individual).assess();
                    } else {
                        System.out.println(individual);
                    }
                }
            }
        }
    }

    /**
     * * run - this public method is used to call in the main logic within the class
     */
    public void run() {
        while (this.listFile.hasNext()) {
            String profession = this.listFile.nextLine().trim();

            if (profession.isEmpty()) handleExit(-1);

            switch (profession.toUpperCase()) {
                case "WIZARD":
                    handleWizard();
                    break;
                case "WITCH":
                    handleWitch();
                    break;
                default:
                    handleOthers(profession);
            }
        }

        print();
        handleExit(0);
    }
}

/**
 * This class is used for the implementation of Project 5 HW for COS2030 Java
 *
 * @author Kaloyan Doychinov
 * @version 02/12/25
 */
public class Project5 {
    public static void main(String[] argv) {
        Runner runner = new Runner();
        runner.run();
    }
}
