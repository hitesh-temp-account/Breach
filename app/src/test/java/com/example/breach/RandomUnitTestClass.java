package com.example.breach;

import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.MatcherAssert.assertThat;

import org.junit.Test;

public class RandomUnitTestClass {

    // @Test
    // public void verifyUtilMethod1() {
    //     int result = new TempFeatureUtils().utilMethod1();
    //     assertThat(result, is(30));
    // }
    
    @Test
    public void verifyUtilMethod2() {
        int result = new TempFeatureUtils().utilMethod2();
        assertThat(result, is(30));
    }
}
