public class vaultdoor3codi{
    public static void main(String args[]){
        String password = "jU5t_a_sna_3lpm18gb41_u_4_mfr340";
        char[]buffer=new char[32];
        int i = 0;
        for(i=0;i<8;i++){
            buffer[i]=password.charAt(i);
        }
        for(;i<16;i++){
            buffer[i]=password.charAt(23-i);
        }
        for(;i<32;i+=2){
            buffer[i]=password.charAt(46-i);
        }
        for(i=31;i>=17;i-=2){
            buffer[i]=password.charAt(i);
        }
        for (i = 0; i < 32;i++){
            System.out.print(buffer[i]);
        }
    }

}
