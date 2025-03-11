package Strings;

import java.util.*;
import java.io.FileWriter;
import java.io.File;
import java.io.IOException;

public class HexColorGen {
	public static LinkedList<String> hex_strings = new LinkedList<String>();
	private static String[] hex_values = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"};
	public HexColorGen() {
		for(String i : hex_values) {
			hex_strings.add(i);
		}
	}
	public static int hex_to_int(String[] hex) {
		int int_value = 0;
		int value_check = 1;
		for(int i = hex.length - 1; i >= 0; i--) {
			int_value += value_check * hex_strings.indexOf(hex[i]);
			value_check *= 16;
		}
		return int_value;
	}
	public static void main(String[] args) {
		HexColorGen z = new HexColorGen();
		try {
	    	File mainObj = new File("color_frame.py");
	    	FileWriter mainWR = new FileWriter("color_frame.py");
	    	mainWR.write("import tkinter as tk;");
	    	mainWR.write(" color_frame = tk.Tk(); color_frame.geometry("
	    			+ "\"400x400\"); "
	    			+ "color_listbox = tk.Listbox(color_frame)");
	    	for(String a : hex_strings) {
		    	for(String b : hex_strings) {
			        File stringObj = new File("color_canvas" + a + b + ".py");
			        File hashObj = new File("hash" + a + b + ".py");
		            FileWriter stringWR = new FileWriter("color_canvas" + a + b + ".py");
		            FileWriter hashWR = new FileWriter("hash" + a + b + ".py");
		            stringWR.write("import tkinter as tk\nimport hash" + a + b);
			        for(String c : hex_strings) {
			    	    for(String d : hex_strings) {
		    		        for(String e : hex_strings) {
			    		        for(String f : hex_strings) {
				    		        String final_hex = e + f + c + d + a + b;
				    		        String[] finhstr = {e, f, c, d, a, b};
				    		        hashWR.write("def hashcode" + final_hex + "():");
				    		        hashWR.write("\n    return(\"#" + final_hex + "\")");
			    		    		if (final_hex.substring(0, 4).equals("0000")) {
			    		    			stringWR.write("\ncolor_frame00 = tk.Tk()");
			    		    			stringWR.write("\ntry:\n    color_canvas.destroy()");
			    		    			stringWR.write("\nexcept:\n    pass");
			    			            stringWR.write("\ncolor_canvas = tk.Canvas("
			    			    	        	+ "color_frame00, width = 320, height = 320)");
			    		    			if (b.equals("0")) {
			    		    				mainWR.write("\n");
			    		    			}
		    	    				    mainWR.write("color_listbox.insert(" + hex_to_int(finhstr) + ", \"#" + a + b + "\", bg = \"#" + final_hex + "\"); ");
		    		    		    }
			    		    		if (b.equals("0")) {
			    		    			hashWR.write("\n");
			    		    		}
			    		    		stringWR.write("\nc" + e + f + " = tk.Button(color_frame" + a + b + ", width = 5,"
			    		    				+ " height = 5, bg = \"#" + final_hex + "\")");
			    		    				//+ " command = lambda : hash" + a + b + ".hashcode" + final_hex + "())");
				    	    	    String[] cdnums = {c, d};
					        	    String[] efnums = {e, f};
					        	    stringWR.write("; c" + e + f + ".place(x = 5*" + hex_to_int(efnums) + 
					        	    		", y = 5*" + hex_to_int(cdnums) + ")");
				    	        }
				            }
			            }
		            }
			        String[] abnums = {a, b};
			        stringWR.write("\ncolor_canvas.grid()");
		        }
			}
	    	mainWR.write("\ndef selected_color(x):"
	    			+ "\n    for i in color_listbox:\n\tif i != \"\":\n\t    return(color_listbox.get(i)");
	    	mainWR.write("\nlistbox.bind(\"<Double 1>\", lambda x: selected_item(x)");
	    	mainWR.write("\nlistbox.pack()");
		}
		catch (IOException err) {
	    	System.out.println("Error");
		    err.printStackTrace();
	    }
	}
}
