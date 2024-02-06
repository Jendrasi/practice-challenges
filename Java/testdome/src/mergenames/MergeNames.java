package mergenames;

import java.util.HashSet;
import java.util.Set;

public class MergeNames {
    
    public static String[] uniqueNames(String[] names1, String[] names2) {
        Set<String> uniqueNames = new HashSet<String>();
        int i = 0;
        while (i < names1.length) {
            uniqueNames.add(names1[i]);
            i++;
        }
        i = 0;
        while (i < names2.length) {
            uniqueNames.add(names2[i]);
            i++;
        }
        return uniqueNames.stream().toArray(String[]::new);
    }
    
    public static void main(String[] args) {
        String[] names1 = new String[] {"Ava", "Emma", "Olivia"};
        String[] names2 = new String[] {"Olivia", "Sophia", "Emma"};
        System.out.println(String.join(", ", MergeNames.uniqueNames(names1, names2))); // should print Ava, Emma, Olivia, Sophia
    }

}