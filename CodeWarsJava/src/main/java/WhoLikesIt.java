public class WhoLikesIt {
    public static String whoLikesIt(String... names) {
        String likesResult;
        switch (names.length) {
            case 0:
                likesResult = "no one likes this";
                break;
            case 1:
                likesResult = String.format("%s likes this", names[0]);
                break;
            case 2:
                likesResult = String.format("%s and %s like this", names[0], names[1]);
                break;
            case 3:
                likesResult = String.format("%s, %s and %s like this", names[0], names[1], names[2]);
                break;
            default:
                likesResult = String.format("%s, %s and %d others like this", names[0], names[1], names.length - 2);
                break;
        }
        return likesResult;
    }
}
