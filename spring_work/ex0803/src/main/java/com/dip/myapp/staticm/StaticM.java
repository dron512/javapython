package com.dip.myapp.staticm;

import java.text.DateFormat;
import java.util.Date;
import java.util.Locale;

public class StaticM {
	public static String getDateFormat() {
		Date date = new Date();
		DateFormat dateFormat = DateFormat.getDateTimeInstance(DateFormat.LONG, DateFormat.LONG, Locale.KOREA);
		String formattedDate = dateFormat.format(date);
		return formattedDate;
	}
}
