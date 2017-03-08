"""
import java.util.*;

public class Solution {

	static final int[] PRIMES = new int[] {2, 3, 5, 7, 11, 13, 17};

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT.
         * Your class should be named Solution. */
    	Scanner in = new Scanner(System.in);
    	int n = in.nextInt();
    	in.close();
    	ArrayList<String> digits = new ArrayList<String>();
    	for (int i = 0; i <= n; i++) {
    		digits.add(Integer.toString(i));
    	}
    	System.out.println(generateSum(digits, ""));
    }

    public static long generateSum(ArrayList<String> digitsLeft, String current) {
    	if (digitsLeft.size() == 0) {
    		return Long.valueOf(current);
    	} else {
    		long sum = 0;
	    	for (int i = 0; i < digitsLeft.size(); i++) {
	    		String digit = digitsLeft.remove(i);
	    		current = current + digit;
	    		int l = current.length();
	    		if (l < 4 || Long.valueOf(current.substring(l - 3, l)) % PRIMES[l - 4] == 0) {
		    		sum += generateSum(digitsLeft, current);
	    		}
	    		current = current.substring(0, current.length() - 1);
	    		digitsLeft.add(i, digit);
	    	}
	    	return sum;
    	}
    }
}
"""