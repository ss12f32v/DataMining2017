import java.io.*;
import java.util.*;

public class AprioriHash extends Observable {


    public static void main(String[] args) throws Exception {
    	AprioriHash ap = new AprioriHash();
    }

    private List<int[]> itemsets ;
    private String transaFile; 
    private int numItems; 
    private int numTransactions; 
    private double minSup; 
    
    /** by default, Apriori is used with the command line interface */
    private boolean usedAsLibrary = false;

    public  AprioriHash() throws Exception{
        configure();
        go();
    }

    /** starts the algorithm after configuration */
    private void go() throws Exception {
        //start timer
        long start = System.currentTimeMillis();

        // first we generate the candidates of size 1
        createItemsetsOfSize1();        
        int itemsetNumber = 1;
        int nbFrequentSets = 0;
        
        while (itemsets.size()>0){
            calculateFrequentItemsets();

            if(itemsets.size()!=0){
                nbFrequentSets+=itemsets.size();
                createNewItemsetsFromPreviousOnes();
            }
            itemsetNumber++;
        } 

        //display the execution time
        long end = System.currentTimeMillis();
        log("Execution time is: "+((double)(end-start)/1000) + " seconds.");
    }

    /** triggers actions if a frequent item set has been found  */
    private void foundFrequentItemSet(int[] itemset, int support) {
    	if (usedAsLibrary) {
            this.setChanged();
            notifyObservers(itemset);
    	}
    	else {System.out.println(Arrays.toString(itemset) + " " +support);}
    }

    /** outputs a message in Sys.err if not used as library */
    private void log(String message) {
    	if (!usedAsLibrary) {
    		System.err.println(message);
    	}
    }

    /** computes numItems, numTransactions, and sets minSup */
    private void configure() throws Exception
    {        
        // set transafile
        transaFile = "customer.txt";
    	// set minsupport
        minSup = 100;    	
    	
    	numItems = 0;
    	numTransactions=0;
    	BufferedReader data_in = new BufferedReader(new FileReader(transaFile));
    	while (data_in.ready()) {    		
    		String line=data_in.readLine();
    		if (line.matches("\\s*")) continue;
    		numTransactions++;
    		StringTokenizer t = new StringTokenizer(line," ");
    		while (t.hasMoreTokens()) {
    			int x = Integer.parseInt(t.nextToken());
    			if (x+1>numItems) numItems=x+1;
    		}    		
    	}  
    }

	private void createItemsetsOfSize1() {
		itemsets = new ArrayList<int[]>();
        for(int i=0; i<numItems; i++)
        {
        	int[] cand = {i};
        	itemsets.add(cand);
        }
	}
	
    private void createNewItemsetsFromPreviousOnes(){
    	int currentSizeOfItemsets = itemsets.get(0).length;
    	//temporary candidates
    	HashMap<String, int[]> tempCandidates = new HashMap<String, int[]>();
    	
        // compare each pair of itemsets of size n-1
        for(int i=0; i<itemsets.size(); i++)
        {
            for(int j=i+1; j<itemsets.size(); j++)
            {
                int[] X = itemsets.get(i);
                int[] Y = itemsets.get(j);

                assert (X.length==Y.length);
                
                //make a string of the first n-2 tokens of the strings
                int [] newCand = new int[currentSizeOfItemsets+1];
                for(int s=0; s<newCand.length-1; s++) {
                	newCand[s] = X[s];
                }
                    
                int ndifferent = 0;
                // then we find the missing value
                for(int s1=0; s1<Y.length; s1++)
                {
                	boolean found = false;
                	// is Y[s1] in X?
                    for(int s2=0; s2<X.length; s2++) {
                    	if (X[s2]==Y[s1]) { 
                    		found = true;
                    		break;
                    	}
                	}
                	if (!found){ // Y[s1] is not in X
                		ndifferent++;
                		newCand[newCand.length -1] = Y[s1];
                	}
            	}
                
                // we have to find at least 1 different, otherwise it means that we have two times the same set in the existing candidates
                assert(ndifferent>0);
                
                
                if (ndifferent==1) {
                	Arrays.sort(newCand);
                	tempCandidates.put(Arrays.toString(newCand),newCand);
                }
            }
        }
        
        //set the new itemsets
        itemsets = new ArrayList<int[]>(tempCandidates.values());
    }

    private void line2booleanArray(String line, boolean[] trans) {
	    Arrays.fill(trans, false);
	    StringTokenizer stFile = new StringTokenizer(line, " ");
	    while (stFile.hasMoreTokens()){
	        int parsedVal = Integer.parseInt(stFile.nextToken());
			trans[parsedVal]=true; //if it is not a 0, assign the value to true
	    }
    }
    
    private void calculateFrequentItemsets() throws Exception{
        List<int[]> frequentCandidates = new ArrayList<int[]>();

        boolean match;
        int count[] = new int[itemsets.size()];

		BufferedReader data_in = new BufferedReader(new InputStreamReader(new FileInputStream(transaFile)));

		boolean[] trans = new boolean[numItems];
		// for each transaction
		for (int i = 0; i < numTransactions; i++) {

			// boolean[] trans = extractEncoding1(data_in.readLine());
			String line = data_in.readLine();
			line2booleanArray(line, trans);

			// check each candidate
			for (int c = 0; c < itemsets.size(); c++) {
				match = true;
				int[] cand = itemsets.get(c);
				for (int xx : cand) {
					if (trans[xx] == false) {
						match = false;
						break;
					}
				}
				if (match) {
					count[c]++;
				}
			}

		}
		data_in.close();

		for (int i = 0; i < itemsets.size(); i++) {
			if (count[i] >= minSup) {
				foundFrequentItemSet(itemsets.get(i),count[i]);
				frequentCandidates.add(itemsets.get(i));
			}
		}
        itemsets = frequentCandidates;
    }
}