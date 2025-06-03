public class FibonacciComNew {

    class Result {
        final Long value;
        Result(Long v) { value = v; }
    }

    public Result fibRecursivoComNew(int n) {
        if (n <= 1)
            return new Result((long) n);

        Result f1 = fibRecursivoComNew(n - 1);
        Result f2 = fibRecursivoComNew(n - 2);

        return new Result(f1.value + f2.value);
    }

    public Result fibIterativoComNew(int n) {
        if (n <= 1)
            return new Result((long) n);

        Long a = 0L, b = 1L;
        for (int i = 2; i <= n; i++) {
            Long temp = a + b;
            a = b;
            b = temp;
        }

        return new Result(b);
    }

    public static void main(String[] args) {
        FibonacciComNew fib = new FibonacciComNew();
        int n = 1000;

        //System.out.println("Recursivo com new: " + fib.fibRecursivoComNew(n).value);
        System.out.println("Iterativo com new: " + fib.fibIterativoComNew(n).value);
    }
}
