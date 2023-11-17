import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(reader.readLine());

        while (tc-- > 0) {
            StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
            BigInteger a = new BigInteger(tokenizer.nextToken());
            BigInteger b = new BigInteger(tokenizer.nextToken());
            System.out.println(a.subtract(b));
        }
    }
}
// 0.560s #1019