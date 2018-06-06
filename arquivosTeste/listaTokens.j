package pass;
import java.lang.System;
public class Series {

    public static int ARITHMETIC = 1;

    private int a; // first term
    1alo = 23;

    public Series () {
        this(1, 1, 10);
    }

    public Series(int a) {
        this.a = a;
    }

    public int computeSum(int kind) {
        int sum = a, t = a, i = n;

        while (i-- > 1) {
            if  (kind == ARITHMETIC) {
            t += d;
            }
            sum += t;
        }

        return sum;
    }

    public static void main(String [] args) {
        int a = Integer.parseInt(args [0]);

        Series s = new Series(a, d, n);

        System.out.println (" Arithmetic sum = "+ s.computeSum(Series.ARITHMETIC));
    }

}