package iut.sae.algo;


public class Algo{
    public static String RLE(String in){
        // Provide your algo here
        StringBuffer rle = new StringBuffer() ; 
        char[] tab = in.toCharArray() ;
        int cpt = 1;
        int i = 0 ;
        while (i < in.length() - 1) {
            if (tab[i] == tab[i + 1]) {
                cpt++ ; 
                if (cpt == 10) {
                    rle.append(9) ; 
                    rle.append(tab[i]); 
                    cpt = 1 ;
                }
            } else {
                rle.append(cpt) ;
                rle.append(tab[i]) ; 
                cpt = 1 ;
            } 
           i++ ; 
        }
        rle.append(cpt) ;
        rle.append(tab[i]) ; 
        return rle.toString();
    }

    public static String RLE(String in, int iteration) throws AlgoException{
        // Provide your algo here
        return "NotYetImplemented";
    }

    public static String unRLE(String in) throws AlgoException{
        // Provide your algo here
        return "NotYetImplemented";

    }

    public static String unRLE(String in, int iteration) throws AlgoException{
        // Provide your algo here
        return "NotYetImplemented";

    }
}

