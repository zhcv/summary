import java.util.List;
import java.util.ArrayList;
import java.util.Collections;


public class Main {

    public static void main(String ... args) {
        List<String> list = new ArrayList();
        list.add("C");
        list.add("C++");
        list.add("java");

        list = Collections.unmodifiableList(list);
        System.out.println(list);

    }

}
