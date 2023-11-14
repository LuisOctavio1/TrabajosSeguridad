## Objetivo

## Solución
```
Para este hice un pequeño codigo en java con los datos que estaban en el
codigo el cual quedo
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

el cual dio la bandera sin el pico, ya con el pico es:
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_1fb380}
```
## Notas adicionales
## Referencias
