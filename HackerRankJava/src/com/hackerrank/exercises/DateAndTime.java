package com.hackerrank.exercises;

import java.time.LocalDate;

public class DateAndTime {

    public static String findDay(int month, int day, int year) {
        LocalDate date = LocalDate.of(year, month, day);

        return date.getDayOfWeek().toString();
    }

    public static void main(String[] args) {
        int year = 2020;
        int month = 6;
        int day = 29;

        String dayOfWeek = DateAndTime.findDay(month, day, year);
        System.out.println(dayOfWeek);
    }
}
