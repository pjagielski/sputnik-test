class TestFile2 {
    public String foo() {
        return "bar";
    }

    private static void incorrectAssignmentInIfCondition() {
        boolean value = false;
        if (value = true) {
            //do Something
            value = false;
        }
        if (value = false) {
          int x = 1;
        }
    }
}
