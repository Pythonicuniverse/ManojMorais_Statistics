def  Ttest_2sample (Variable1, Variable2):
    """
    Independent Sample or Two Sample t-test
    Module develoed by: Manoj Morais (May 5 Sunday, 2024)
    Citation: Scipy.stats ttest_ind
    Parameters: Variable1 - categorical variable or grouping variable (0, 1)
    Mean score and t test: group 1 is coded as 1 and group 2 is coded as 0
    Variable2 - continuous variable
    Example: Variable1 = data['Gender'] - column name
             Variable2 = data['Marks'] -column name
    """
  
    import pandas as pd
    import numpy as np
    
    cc = Variable1.value_counts()
    cc= len(cc)
        
    if cc>2:
        raise ValueError("Error: Variable 1 must be a list-like object containing only 0s and 1s.") 
    else:    
        group1 = Variable2[Variable1==1]
        group2= Variable2[Variable1==0]
        
    
        g1 = np.mean(group1)
        g2=np.mean(group2)
        g1s= group1.std()
        g2s=group2.std()
        from scipy.stats import ttest_ind as ist
        ts, p = ist(a=group1, b=group2)
        ts=float(ts)
        p=float(p)
        pval = f"{p:.04f}"
        n1 = len(group1)
        n2=len(group2)
        summ = n1+n2
        m = {'N': [n1, n2, summ],'Mean Score': [g1, g2, " "], 'Std Dev':[g1s, g2s, " "]}
    
        df= pd.DataFrame(m, index=['Group 1 (1)', 'Group 2 (0)', 'Count'])
        bold = "\033[1m"
        reset="\033[0m"
        text = "Group Statistics"
        print("      "f"{bold}{text}{reset}")
        display(df)
        meand = float(g1 - g2)
        t = {'T Statisic':[ts], 'P val':[pval], 'Mean diff': [meand]}
        out = pd.DataFrame(t)
        text1 = "Independent Sample t-test"
        print("  "f"{bold}{text1}{reset}")
        display(out)
        print ("...........................")
        print ("        ""\nGroup 1 is coded as 1, and Group 2 is coded as 0")
        nul = 'Null Hypothesis'
        alt = 'Alternate Hypothesis'
        print (f"\n {bold}{nul}{reset} : There are no significant differences in the mean scores between the groups")
        print (f"\n {bold}{alt}{reset}: There are significant differences in the mean scores between the groups")
        if float(pval) < (0.05):
            print ("         "   "\nDecision @ 5% level: Reject Null Hypothesis and Accept the Alternate Hypothesis")
        else:  
            print ("          " "\nDecision @ 5% level:Accept Null Hypothesis ")
    
