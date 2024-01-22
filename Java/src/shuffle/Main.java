package shuffle;

import java.util.Arrays;

public class Main {

	public static int[] shuffleFisherYates(int[] list) {
		int[] result = list;
		
		return result;
	}
	
	public static int[] shuffleDurstenfeld(int[] list) {
		int[] result = list;
		
		return result;
	}
	
	private static void reassign(int[] list) {
		list = new int[2];
		list[0] = 3;
		list[1] = 4;
	}

	private static void modify(int[] list) {
		list[1] = 3;
	}

	public static void main(String[] args) {
		int[] list = new int[2];
		list[0] = 1;
		list[1] = 2;
		System.out.println(Arrays.toString(list));
		reassign(list);
		System.out.println(Arrays.toString(list));
		modify(list);
		System.out.println(Arrays.toString(list));
	}

}
