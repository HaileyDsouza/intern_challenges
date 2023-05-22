import java.io.*;

public class Main {
  static void firstNonRepeated(String s) {
  	int index = -1;	
    char non_repeated = ' ';
    for (char i : s.toCharArray()) {
            if (s.indexOf(i) == s.lastIndexOf(i)) {
                non_repeated = i;
                break;
            }
            else {
                index += 1;
            }
        }
        if (index == s.length()-1) {
            System.out.println(" ");
        }
        else {
            System.out.println(non_repeated);
        }
  }

  public static void main(String[] args) {
    firstNonRepeated("hello");
    firstNonRepeated("aabcc");
    firstNonRepeated("aabbcc");
	}
}
