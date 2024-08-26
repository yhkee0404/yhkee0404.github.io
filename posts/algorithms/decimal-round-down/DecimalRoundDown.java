import java.math.BigDecimal;
import java.math.MathContext;
import java.math.RoundingMode;

class DecimalRoundDown {

    public static void main(final String[] args) {

        printNaivePrimitiveDoubles();
        
        System.out.println();
        printNaiveBigDecimals(RoundingMode.DOWN);
        printNaiveBigDecimals(RoundingMode.UP);
        
        System.out.println();
        printEpsilonPrimitiveDoubles();
        
        System.out.println();
        printEpsilonBigDecimals(RoundingMode.DOWN);
        printEpsilonBigDecimals(RoundingMode.UP);

    }

    private static void printNaivePrimitiveDoubles() {

        final double five = 10. / 6 * 3;
        final double four = (7 - five) * 2;

        System.out.println(five + " " + (int) five);
        System.out.println(four + " " + (int) four);

    }

    private static void printNaiveBigDecimals(final RoundingMode divideRoundingMode) {

        BigDecimal five;
        try {
            five = new BigDecimal("10")
                    .divide(new BigDecimal("6"))
                    .multiply(new BigDecimal("3"));
        } catch (Exception e) {
            e.printStackTrace();
            five = new BigDecimal("10")
                    .divide(new BigDecimal("6"), 3, divideRoundingMode)
                    .multiply(new BigDecimal("3"));
        }
        final BigDecimal four = new BigDecimal("7")
                .subtract(five)
                .multiply(new BigDecimal("2"));

        final MathContext mc = new MathContext(2, RoundingMode.DOWN);
        System.out.println(five + " " + five.intValue() + " " + five.round(mc));
        System.out.println(four + " " + four.intValue() + " " + four.round(mc));

    }

    private static void printEpsilonPrimitiveDoubles() {

        final double EPSILON = 1e-2;

        final double five = 10. / 6 * 3;
        final double four = (7 - five) * 2 + EPSILON;

        final double fiveEpsilon = five + EPSILON;
        System.out.println(fiveEpsilon + " " + (int) fiveEpsilon);
        System.out.println(four + " " + (int) four);

    }

    private static void printEpsilonBigDecimals(final RoundingMode divideRoundingMode) {

        final BigDecimal EPSILON = new BigDecimal("1e-2");

        final BigDecimal five = new BigDecimal("10")
                .divide(new BigDecimal("6"), 3, divideRoundingMode)
                .multiply(new BigDecimal("3"));
        final BigDecimal four = new BigDecimal("7")
                .subtract(five)
                .multiply(new BigDecimal("2"))
                .add(EPSILON);

        final BigDecimal fiveEpsilon = five.add(EPSILON);
        final MathContext mc = new MathContext(2, RoundingMode.DOWN);
        System.out.println(fiveEpsilon + " " + fiveEpsilon.intValue() + " " + fiveEpsilon.round(mc));
        System.out.println(four + " " + four.intValue() + " " + four.round(mc));

    }

}