import java.util.Arrays;
import java.util.LinkedList;
import java.util.Map;

public class Quiz8910 {
    public static void main(String[] args) {
        //P1: write code to reverse a String
        System.out.println("\nP1: reverse:");
        String s = "balloon";
        System.out.println("\toriginal string: " + s);
        System.out.println("\treversed string: " + reverse(s));
        s = "velociraptor";
        System.out.println("\toriginal string: " + s);
        System.out.println("\treversed string: " + reverse(s));

        //P2: write code to swap two numbers without a third variable
        System.out.println("\nP2: swap:");
        swap(25, 35);

        //P3: write code to print all substrings of a string
        System.out.println("\nP3: all substrings:");
        System.out.print("\t all subs of hello: ");
        allsubs("hello");
        System.out.print("\t all subs of velociraptor: ");
        allsubs("velociraptor");
        System.out.print("\t all subs of gargantuan: ");
        allsubs("gargantuan");

        //P4: write code to check if vowels are present in a String
        System.out.println("\nP4: vowels:");
        String word = "sequoia";
        System.out.printf("\tvowels present in %s: %b%n", word, vowels(word));
        word = "hymn";
        System.out.printf("\tvowels present in %s: %b%n", word, vowels(word));

        //P5: write code to separate an array of 0s and 1s into an array of the 0s and then the 1s
        System.out.println("\nP5: zeros and ones:");
        int[] z = {0, 1, 1, 1, 0, 0, 1, 0, 1};
        System.out.printf("\t%s -> %s%n", Arrays.toString(z), Arrays.toString(zerosandones(z)));
        z = new int[]{0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1};
        System.out.printf("\t%s -> %s%n", Arrays.toString(z), Arrays.toString(zerosandones(z)));

        //P6: write code to check if a list contains only odd numbers
        System.out.println("\nP6: odds:");
        odds(new int[]{16, 4, 53, 12, 50923, 23, -394, 213});
        odds(new int[]{35, 71, 99, 5821, -43});

        //P7: write code to find the missing number in an array starting at 1, no duplicates
        System.out.println("\nP7: missing:");
        int[] arry = {7, 5, 6, 1, 4, 2};
        System.out.printf("\tmissing number from %s: %d%n", Arrays.toString(arry), missing(arry));
        arry = new int[]{5, 3, 1, 2};
        System.out.printf("\tmissing number from %s: %d%n", Arrays.toString(arry), missing(arry));
        arry = new int[]{5, 12, 3, 1, 2, 4, 8, 6, 7, 9, 10, 14, 11};
        System.out.printf("\tmissing number from %s: %d%n", Arrays.toString(arry), missing(arry));

        //P8: write code to check if a string is a palindrome
        System.out.println("\nP8: palindrome:");
        String p = "oozy rat in a sanitary zoo";
        System.out.println("\t" + p + (palindrome(p) ? " is a palindrome" : " is not a palindrome"));
        p = "ufos tofu";
        System.out.println("\t" + p + (palindrome(p) ? " is a palindrome" : " is not a palindrome"));

        //P9: write code to calculate the factorial of a number
        System.out.println("\nP9: factorial:");
        int num = 6;
        System.out.println("\tfactorial of " + num + " is " + factorial(num));
        num = 12;
        System.out.println("\tfactorial of " + num + " is " + factorial(num));

        //P10: write code to reverse a linked list
        System.out.println("\nP10: reverse ll:");
        LinkedList<Integer> ll = new LinkedList<>();
        ll.add(12);
        ll.add(31);
        ll.add(482);
        ll.add(-4);
        ll.add(34);
        System.out.println("\toriginal list " + ll);
        LinkedList<Integer> rev = llreverse(ll);
        System.out.println("\treversed list " + rev);

        //P11: write code to check if two arrays only contain the same elements, duplicates are allowed
        System.out.println("\nP11: same elements:");
        same(new Integer[]{3, 5, 1, 3, 7, 0, 9}, new Integer[]{3, 5, 1, 7});
        same(new Integer[]{3, 5, 1, 3, 7, 0, 9}, new Integer[]{9, 9, 0, 3, 5, 1, 7});

        //P12: write code to find the first and last occurrence of an element in an array
        System.out.println("\nP12: first and last");
        int[] arr = {2, 3, 4, 5, 2, 3, 5, 2, 1, 2, 2, 4, 4, 3, 5, 5, 6, 7, 3, 4, 6, 7, 2, 3, 3, 5, 7, 8, 3, 0, 1, 2, 4, 2, 0, 0};
        System.out.println("\tin " + Arrays.toString(arr));
        firstandlast(arr, 5);
        firstandlast(arr, 2);
        firstandlast(arr, 0);
        firstandlast(arr, 7);
        firstandlast(arr, 9);
        firstandlast(arr, 8);

        //P13: write code to find a pair in an array whose sum is closest to 0
        System.out.println("\nP13: closest to zero:");
        int[] a = {1, 3, -5, 7, 8, 20, -40, 6};
        System.out.print("\tin " + Arrays.toString(a) + " pair of elements with sum closes to to zero: ");
        closesttozero(a);
        a = new int[]{10, 13, 35, 7, 28, 20, 40, -23, 16};
        System.out.print("\tin " + Arrays.toString(a) + " pair of elements with sum closes to to zero: ");
        closesttozero(a);

        //P14: write code to find the second largest number in an array
        System.out.println("\nP14: second largest:");
        int[] l1 = new int[]{16, 4, 53, 12, 50923, 23, -394, 213};
        int[] l2 = new int[]{35, 71, 99, 5821, -43};
        System.out.println("\t" + second(l1) + " is the second largest number in " + Arrays.toString(l1));
        System.out.println("\t" + second(l2) + " is the second largest number in " + Arrays.toString(l2));

        //P15: write code to output an n x n matrix row-wise and column-wise
        System.out.println("\nP15: matrix rows and columns:");
        int[][] trix = {{3, 4, 6}, {9, 3, 1}, {9, 2, 4}};
        for (int i = 0; i < trix.length; i++) System.out.println("\t" + Arrays.toString(trix[i]));
        matrix(trix);
        trix = new int[][]{{3, 1, 4, 6}, {0, 6, 3, 8}, {1, 6, 2, 3}, {9, 2, 4, 7}};
        for (int i = 0; i < trix.length; i++) System.out.println("\t" + Arrays.toString(trix[i]));
        matrix(trix);

        //P16: write code to output an n x n matrix as a wave (see example output)
        System.out.println("\nP16: matrix wave:");
        int[][] trix2 = {{1, 6, 7}, {2, 5, 8}, {3, 4, 9}};
        for (int i = 0; i < trix2.length; i++) System.out.println("\t" + Arrays.toString(trix2[i]));
        matrixwave(trix2);
        trix2 = new int[][]{{1, 6, 5, 8, 7}, {2, 0, 1, 5, 8}, {1, 3, 6, 4, 9}};
        for (int i = 0; i < trix2.length; i++) System.out.println("\t" + Arrays.toString(trix2[i]));
        matrixwave(trix2);

        //P17: write code to calculate the frequency of a digit in an int
        System.out.println("\nP17: frequency of digits:");
        System.out.printf("\t%d shows up %d times in %d%n", 5, digits(-4255235, 5), -4255235);
        System.out.printf("\t%d shows up %d times in %d%n", 0, digits(0, 0), 0);
        System.out.printf("\t%d shows up %d times in %d%n", 4, digits(9318051, 4), 9318051);
        System.out.printf("\t%d shows up %d times in %d%n", 1, digits(901211718, 1), 901211718);

        //P18: write code that toggles the case of every alpha-character in a string
        System.out.println("\nP18: toggle:");
        System.out.println("\t\"APpLe\" toggled is \"" + toggle("APpLe") + "\"");
        System.out.println("\t\"7 elePHAntS, 18 LEGS\" toggled is \"" + toggle("7 elePHAntS, 18 LEGS") + "\"");

        //P19: write code to output the sorted list of distinct characters and their count from a string
        System.out.println("\nP19: count chars:");
        System.out.println("\tshe seemed to be looking at something other than what she looked as if she was looking at");
        Map<String, Integer> chars = counts("she seemed to be looking at something other than what she looked as if she was looking at");
        System.out.println("\tcontains " + chars);
        System.out.println("\tfoqifh-sdxjfh.lihfsdanldiha");
        chars = counts("foqifh-sdxjfh.lihfsdanldiha");
        System.out.println("\tcontains " + chars);

        //P20: write code to find the max-sum contiguous subarray
        System.out.println("\nP20: max-sum contiguous subarray:");
        int[] ar = {1, 8, -3, -7, 2, 7, -1, -9};
        System.out.println("\tin " + Arrays.toString(ar) + " -> " + contiguous(ar));
        ar = new int[]{16, 3, 2, -1, -4, 12, 3, 0};
        System.out.println("\tin " + Arrays.toString(ar) + " -> " + contiguous(ar));

        //P21: write code to output an inverted pyramid given user input
        System.out.println("\nP21: pyramid:");
        pyramid(12);
        pyramid(3);
        pyramid(7);
        pyramid(5);

        //P22: write code to check if a number is an Armstrong number
        //an Armstrong number is number which is the sum of each of its digits to the power of the number of digits
        //e.g. 153 = 1*1*1 + 5*5*5 + 3*3*3 = 1 + 125 + 27 = 153
        //e.g. 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4 = 1 + 1296 + 81 + 256 = 1634
        //e.g 92727 = 9*9*9*9*9 + 2*2*2*2*2 + 7*7*7*7*7 + 2*2*2*2*2 + 7*7*7*7*7 = 59049 + 32 + 16807 + 32 + 16807 = 92727
        System.out.println("\nP22: armstrong number: ");
        System.out.println("\t" + 371 + (armstrong(371) ? " is an armstrong number" : " is not an armstrong number"));
        System.out.println("\t" + 1741725 + (armstrong(1741725) ? " is an armstrong number" : " is not an armstrong number"));
        System.out.println("\t" + 154 + (armstrong(154) ? " is an armstrong number" : " is not an armstrong number"));
    }

    private static String reverse(String s) {
        //write code to reverse the string s
        String ns = "";
        for (int i = s.length() - 1; i >= 0; --i) {
            ns += s.charAt(i);
        }

        return ns;
    }

    private static boolean vowels(String word) {
        //write code to check if vowels are present in word

        for (int i = 0; i < word.length(); i++) {
            if (word.charAt(i) == 'a' ||
                    word.charAt(i) == 'e' ||
                    word.charAt(i) == 'o' ||
                    word.charAt(i) == 'u' ||
                    word.charAt(i) == 'i'
            )
                return true;
        }
        return false;
    }

    private static void swap(int a, int b) {
        System.out.printf("\ta = %d, b = %d%n", a, b);

        //write code to swap a and b without a third variable
        a = a ^ b;
        b = a ^ b;
        a = a ^ b;

        System.out.printf("\ta = %d, b = %d%n", a, b);
    }

    private static void allsubs(String s) {
        //write code to print all substrings of a string
        for (int i = 0; i < s.length(); ++i) {
            for (int j = i + 1; j <= s.length(); ++j) {
                System.out.print(s.substring(i, j) + " ");
            }
        }

        System.out.println();

    }

    private static int[] zerosandones(int[] list) {
        //write code to separate an array of 0s and 1s into an array of the 0s and then the 1s

        int[] count = new int[2];
        for (int i : list)
            ++count[i];


        for (int i = 0; i < list.length; ++i) {
            if (count[0]-- > 0) {
                list[i] = 0;
            } else {
                list[i] = 1;
            }
        }

        return list;
    }

    private static void odds(int[] list) {
        // write code to check if a list contains only odd numbers
        boolean odd = true;

        for (int i : list) {
            if (i % 2 == 0) {
                odd = false;
                break;
            }
        }

        if (odd) {
            System.out.println("\tonly odds number in " + Arrays.toString(list));
        } else {
            System.out.println("\teven number present in " + Arrays.toString(list));

        }
    }

    private static int missing(int[] a) {
        //write code to find the missing number in an array starting at 1, no duplicates
        int missingNumber = 1;
        boolean flag = false;

        for (int i = 0; i < a.length; i++) {
            flag = false;
            for (int j = 0; j < a.length; j++) {
                if (a[j] == missingNumber) {
                    flag = true;
                    break;
                }
            }
            if (flag == false) {
                break;
            }
            missingNumber++;
        }

        return missingNumber;
    }

    private static boolean palindrome(String p) {
        //write code to check if a string is a palindrome
        p = p.replaceAll("\s", "");
        for (int i = 0; i < p.length(); ++i) {
            if (p.charAt(i) != p.charAt(p.length() - 1 - i)) {
                return false;
            }
        }

        return true;
    }

    private static int factorial(int num) {
        //write code to calculate the factorial of a number
        int res = 1;

        while (num > 0) {
            res *= num--;
        }

        return res;
    }

    private static LinkedList<Integer> llreverse(LinkedList<Integer> ll) {
        //write code to reverse a linked list

        LinkedList<Integer> newll = new LinkedList<>();
        while (!ll.isEmpty()) {
            newll.add(ll.removeLast());
        }

        return newll;
    }

    private static void same(Integer[] a, Integer[] b) {
        //write code to check if two arrays only contain the same elements, duplicates are allowed
        boolean flag = false;

        for (int i = 0; i < a.length; i++) {
            flag = false;
            for (int j = 0; j < b.length; j++) {
                if (a[i] == b[j]) {
                    flag = true;
                    break;
                }
            }
            if (flag == false) break;
        }

        if (flag == false)
            System.out.println("\t" + Arrays.toString(a) + " and " + Arrays.toString(b) + " don't have the same elements");
        else
            System.out.println("\t" + Arrays.toString(a) + " and " + Arrays.toString(b) + " have the same elements");
    }

    private static void firstandlast(int[] a, int el) {
        //write code to find the first and last occurrence of an element in an array
        int first = 0, last = 0;

        int[] elIndexes = new int[]{0, 0};

        for (int i = 0; i < a.length; i++) {
            if (a[i] == el && elIndexes[0] == 0) {
                elIndexes[0] = i;
            } else if (a[i] == el) {
                elIndexes[1] = i;
            }
        }
        if (elIndexes[0] == 0 && elIndexes[1] == 0)
            System.out.println("\t" + el + " not found");
        else
            System.out.printf("\tfirst index of %d: %d, last index of %d: %d%n", el, elIndexes[0], el, elIndexes[1]);
    }


    private static void closesttozero(int[] a) {
        //write code to find a pair in an array whose sum is closest to 0
        int[] closest = new int[a.length / 2];
        for (int i = 0; i < a.length - 1; i += 2) {
            closest[i / 2] = a[i] + a[i + 1];
        }

        int closestIndex = 0;
        int closestToZero = Math.abs(closest[0]);

        for (int i = 1; i < closest.length; ++i) {
            if (Math.abs(closest[i]) < closestToZero) {
                closestIndex = i;
                closestToZero = Math.abs(closest[i]);
            }
        }

        System.out.printf("%d and %d%n", a[closestIndex], a[closestIndex + 1]);
    }

    private static int second(int[] list) {
        //write code to find the second largest number in an array


        return 0;
    }

    private static void matrix(int[][] m) {
        //write code to output an nxn matrix row-wise and column-wise


    }

    private static void matrixwave(int[][] m) {
        //write code to output an nxn matrix as a wave


    }

    private static int digits(int num, int digit) {
        //write code to calculate the frequency of a user defined digit in an int


        return 0;
    }

    private static String toggle(String crazy) {
        //write code that toggles the case of every alpha-character in a string


        return "";
    }

    private static Map<String, Integer> counts(String seq) {
        //write code to output the list of distinct characters and their count from a string


        return null;
    }

    private static boolean armstrong(int num) {
        //write code to check if a number is an Armstrong number


        return false;
    }

    private static int contiguous(int[] list) {
        //write code to find the max-sum contiguous subarray


        return 0;
    }

    private static void pyramid(int rows) {
        //write code to output an inverted pyramid given user input


    }
}