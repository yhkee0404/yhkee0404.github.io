import java.math.BigDecimal;
import java.util.HashSet;
import java.util.Set;
import java.util.SortedSet;
import java.util.TreeSet;

class Adequality implements Comparable<Adequality> {

    private String name;
    private float value;

    Adequality(final String name) {
        this.name = name;
        this.value = 1.f;
    }

    @Override
    public int compareTo(Adequality o) {
        return 1;
    }

    @Override
    public boolean equals(Object obj) {
        return true;
    }
    
    @Override
    public String toString() {
        this.value /= 10;
        return String.format("%s%.7f", this.name, this.value);
    }

    public static void main(String[] args) {

        final Adequality adequality = new Adequality("a");
        final BigDecimal fourPointZero = new BigDecimal("4.0");
        final BigDecimal fourPointDoubleZero = new BigDecimal("4.00");

        final Set<Adequality> adequalitySet = new HashSet<>();
        final Set<BigDecimal> bigDecimalSet = new HashSet<>();
        final SortedSet<Adequality> adequalitySortedSet = new TreeSet<>();
        final SortedSet<BigDecimal> bigDecimalSortedSet = new TreeSet<>();
        final SortedSet<Adequality> nullableAdequalitySortedSet = new TreeSet<>((a, b) -> 1);
        final SortedSet<BigDecimal> nullableBigDecimalSortedSet = new TreeSet<>(
            (a, b) -> a == null && b == null ? 0
            		: a == null ? -1
                    : b == null ? 1
                    : a.compareTo(b)
        );

        adequalitySet.add(adequality);
        adequalitySet.add(adequality);
        bigDecimalSet.add(fourPointZero);
        bigDecimalSet.add(fourPointDoubleZero);
        System.out.println(adequalitySet + "\t\t\t\t" + bigDecimalSet);

        adequalitySortedSet.add(adequality);
        adequalitySortedSet.add(adequality);
        bigDecimalSortedSet.add(fourPointZero);
        bigDecimalSortedSet.add(fourPointDoubleZero);
        System.out.println(adequalitySortedSet + "\t\t" + bigDecimalSortedSet);

        nullableAdequalitySortedSet.add(adequality);
        nullableAdequalitySortedSet.add(adequality);
        nullableBigDecimalSortedSet.add(fourPointZero);
        nullableBigDecimalSortedSet.add(fourPointDoubleZero);
        System.out.println(nullableAdequalitySortedSet + "\t\t" + nullableBigDecimalSortedSet);

        adequalitySet.add(null);
        adequalitySet.add(null);
        bigDecimalSet.add(null);
        bigDecimalSet.add(null);
        System.out.println(adequalitySet + "\t\t\t" + bigDecimalSet);
        
        try {
            adequalitySortedSet.add(null);
        } catch (NullPointerException e) {
            System.out.print(e);
        }
        try {
            bigDecimalSortedSet.add(null);
        } catch (NullPointerException e) {
            System.out.println("\t\t" + e);
        }

        nullableAdequalitySortedSet.add(null);
        nullableAdequalitySortedSet.add(null);
        nullableBigDecimalSortedSet.add(null);
        nullableBigDecimalSortedSet.add(null);
        System.out.println(nullableAdequalitySortedSet + "\t" + nullableBigDecimalSortedSet);

    }

}