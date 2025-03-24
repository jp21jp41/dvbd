package Strings;

import java.util.*;
import java.io.FileWriter;
import java.io.File;
import java.io.IOException;

// HexColorGen class
public class HexColorGen {
	// LinkedList to help data loop
	public static LinkedList<String> hex_strings = new LinkedList<String>();
	// String Array to initialize hexadecimal values with
	private static String[] hex_values = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"};
	// Empty constructor function which turns array information over to LinkedList
	public HexColorGen() {
		// For-loop converting the hex values to the hex_strings LinkedList
		for(String i : hex_values) {
			hex_strings.add(i);
		}
	}
	// function to convert hexadecimal values to integers
	public static int hex_to_int(String[] hex) {
		int int_value = 0;
		int value_check = 1;
		for(int i = hex.length - 1; i >= 0; i--) {
			int_value += value_check * hex_strings.indexOf(hex[i]);
			value_check *= 16;
		}
		return int_value;
	}
	// main
	public static void main(String[] args) {
		HexColorGen z = new HexColorGen();
		try {
	    	for(String a : hex_strings) {
		    	for(String b : hex_strings) {
			        File stringObj = new File("color_canvas" + a + b + ".py");
		            FileWriter stringWR = new FileWriter("color_canvas" + a + b + ".py");
		            stringWR.write("import tkinter as tk\n");
			        for(String c : hex_strings) {
			    	    for(String d : hex_strings) {
		    		        for(String e : hex_strings) {
			    		        for(String f : hex_strings) {
				    		        String final_hex = e + f + c + d + a + b;
				    		        String[] finhstr = {e, f, c, d, a, b};
			    		    		if (final_hex.substring(0, 4).equals("0000")) {
			    		    			stringWR.write("\ndef color_canvas(fig_prof, color_holder, sep_frame):");
			    			            stringWR.write("\n    color_canvas = tk.Canvas("
			    			    	        	+ "sep_frame, width = 320, height = 320)");
		    		    		    }
			    		    		String[] cdnums = {c, d};
			    		    		String[] efnums = {e, f};
			    		    		if ((hex_to_int(cdnums) % 16 == 0) && hex_to_int(efnums) % 16 == 0) { 
			    		    			stringWR.write("\n    c" + e + f + c + d + " = tk.Button(sep_frame, width = 1,"
			    		    				+ " height = 1, bg = \"#" + final_hex + "\","
			    		    				+ " command = lambda : fig_prof.color_select(\"#" + final_hex + "\", color_holder))"); 
			    		    			stringWR.write("; c" + e + f + c + d + ".place(x = " + hex_to_int(efnums) + ", y = " + hex_to_int(cdnums) + ")");
			    		    		}
				    	        }
				            }
			            }
		            }
		    	}
	    	}
		}
		catch (IOException err) {
	    	System.out.println("Error");
		    err.printStackTrace();
		    }
	}
}
