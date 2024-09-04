class harac{
    public static void main(String args[]){
        String s="10002";
        for(int i=0;i<s.length();i++){
            int a=Character.getNumericValue(s.charAt(i));
            System.out.print(a);
        }
    }
}