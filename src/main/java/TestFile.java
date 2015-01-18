class TestFile {
    public String foo() {
        return "bar";
    }

    private static void incorrectAssignmentInIfCondition() {
        boolean value = false;
        if (value = true) {
            //do Something
        } else {
            //else Do Something
        }
    }
}
