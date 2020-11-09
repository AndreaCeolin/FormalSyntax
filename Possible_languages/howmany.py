import sys



def check(P):

    #this function records the position of the parameters in a list
    size = len(P)-1
    for num in range(len(P), 95):
        P = P + '?'
    x = [P[0]]
    FGM = P[1]
    FGA = P[2]
    FGK = P[3]
    SPK = P[4]
    FGP = P[5]
    FSP = P[6]
    FGN = P[7]
    GCO = P[8]
    PLS = P[9]
    FSN = P[10]
    FNN = P[11]
    FGT = P[12]
    FGG = P[13]
    FSG = P[14]
    CGB = P[15]
    FPC = P[16]
    DGR = P[17]
    DGP = P[18]
    CGR = P[19]
    NWD = P[20]
    DGD = P[21]
    DPQ = P[22]
    DCN = P[23]
    DNN = P[24]
    DIN = P[25]
    FGC = P[26]
    FGE = P[27]
    FCN = P[28]
    HMP = P[29]
    ARR = P[30]
    GFP = P[31]
    GFN = P[32]
    CSE = P[33]
    CAL = P[34]
    GAL = P[35]
    EAL = P[36]
    DMP = P[37]
    DMG = P[38]
    GCN = P[39]
    GUN = P[40]
    GAD = P[41]
    GFS = P[42]
    GFO = P[43]
    PGO = P[44]
    GGS = P[45]
    GSI = P[46]
    ALP = P[47]
    GST = P[48]
    GEI = P[49]
    GNR = P[50]
    GIT = P[51]
    UST = P[52]
    GPC = P[53]
    PSC = P[54]
    PCA = P[55]
    RHM = P[56]
    FRC = P[57]
    NRC = P[58]
    DOR = P[59]
    LKA = P[60]
    LKP = P[61]
    LKO = P[62]
    FFP = P[63]
    NUP = P[64]
    PNP = P[65]
    NUD = P[66]
    NUC = P[67]
    NM1 = P[68]
    NM2 = P[69]
    NUA = P[70]
    NGO = P[71]
    EAF = P[72]
    ACM = P[73]
    DSN = P[74]
    DSA = P[75]
    DOC = P[76]
    NEX = P[77]
    PEX = P[78]
    FEX = P[79]
    PDC = P[80]
    ACL = P[81]
    NCL = P[82]
    APO = P[83]
    WAP = P[84]
    AGE = P[85]
    OPK = P[86]
    TSP = P[87]
    TDP = P[88]
    TDC = P[89]
    TAR = P[90]
    TAD = P[91]
    TND = P[92]
    TDA = P[93]
    TNL = P[94]

    #This list stores the conditional implications of the parameters
    par = [[FGM, True],
           [FGA, FGM == "+"],
           [FGK, FGM == "+"],
           [SPK, FGK == "+"],
           [FGP, FGM == "+"],
           [FSP, FGP != "+"],
           [FGN, FGP == "+"],
           [GCO, FGM == '+' and FGN != "+"],
           [PLS, FGM == "+" and FGN != "+"],
           [FSN, FGN == "+"],  #10
           [FNN, FSN == "+"],
           [FGT, True],
           [FGG, FGN == "+"],
           [FSG, FGN == "+"],
           [CGB, True],
           [FPC, True],
           [DGR, FPC == "-" and FGN == "+"],
           [DGP, DGR != "+"],
           [CGR, CGB == "-" and DGR == "+"],
           [NWD, FGP == "+" and (FSN == '-' or DGR == "+")],  #P20
           [DGD, DGR == "+" or FSN == "-"],
           [DPQ, FNN == "+" and CGB == "-"],
           [DCN, DGR == "+" or FSN == "-"],
           [DNN, DCN == "-"],
           [DIN, FSN == "+"],
           [FGC, FGN != "+"],
           [FGE, FGM == '-' and FGC =='+'],
           [FCN, FGP == "+"],
           [HMP, True],  #P30
           [ARR, True],
           [GFP, FGP == '+'],
           [GFN, GFP == '+'],
           [CSE, True],
           [CAL, CSE == '+' and GFN != "+"],
           [GAL, CSE == "+" and CAL != "-"],
           [EAL, CSE == "+" and CAL != "-"],
           [DMP, DCN == "+"],
           [DMG, DMP == "+"],
           [GCN, GFP !='+'], #40
           [GUN, FGK == "+" and CSE == '+' and GAL != '-'],
           [GAD, FGM == "+" and (FGK == "-" or GUN == "-")],
           [GFS, FGP == '+' and DGR != '+' and NWD != '-' and EAL != '+' and GFN != '+' and GUN != '+'],
           [GFO, CSE == "+" and GAL != '-' and GUN != '+'],
           [PGO, GFO == "-"],
           [GGS, CGR =='-' and NWD =='+'],
           [GSI, True],
           [ALP, GSI =='-'], #50
           [GST, GSI =='+'],
           [GEI, GFN == "+"],
           [GNR, GFP == "+" and DGR == "-" and GSI =='-'],
           [GIT, True],
           [UST, ARR == "+"],
           [GPC, FGG == "+"],
           [PSC, FSN == "+" and UST != "+" and GPC != "+"],
           [PCA, PSC == "-"],
           #[PMN, FGP == "+" and GFP == "+"],
           [RHM, FGP == "+"],
           [FRC, True], #60
           [NRC, FRC == "+"],
           [DOR, DGR == "+" and FRC == "+"],
           [LKA, True],
           [LKP, True],
           [LKO, LKA == "-"],
           [FFP, FGN == "+" and (LKA == "+" or LKP =="+" or LKO =="+" or GAD =="+") and GFP != '+'],
           [NUP, FGP == "+" and (CSE == "+" or LKA == "+" or LKO == "+")],
           [PNP, FGP == "+" and (CSE =='-' or NUP == '-')],
           [NUD, FGP == "+"],
           [NUC, UST != "+" and PNP =="+" and NUD == "+"],
           [NM1, NUC == "+"],
           [NM2, NM1 == "+"],
           [NUA, NM2 == "+"],
           [NGO, PGO != "-" and NUA == "+"],
           [EAF, NM1 == "-"],
           [ACM, ARR == "-" and NGO == "-"],
           [DSN, DCN == "+"],
           [DSA, (DGR == "+" or DGP =="+") and (ARR =="+" or (NUA != "+" and PNP == "+"))],
           [DOC, NWD=="-" and DCN=="+" and NUC=="+"],
           [NEX, (FSN == "-" or CGR == "-") and NWD == "-" and NUA != "+"], #80
           [PEX, NEX == "+"],
           [FEX, PEX =="+"] ,
           [PDC, DGR == "+" and (CGR == "+" or NWD == "-") and GFP != "+"],
           [ACL, FGP == "+" and DMP != "+" and GFP != "+" and PDC != "+" and UST != "+"],
           [NCL, ACL == '-'],
           [APO, GFP != "+" and UST != '+' and CAL == '-' and FGM == '+'],
           [WAP, PDC == "-" and DMP != '+' and  (APO == "-" or (NM1 == "-" and APO == "+"))],
           [AGE, APO == "+"],
           [OPK, DGR == "+" and GSI =='-'],
           [TSP, FSN == "-" or DGR == "+"], #90
           [TDP, TSP == "+"],
           [TDC, TSP == "-"],
           [TAR, ARR == "+"],
           [TAD, ARR == "-"],
           [TND, CGR == "+" and (TAR == "+" or TAD =="+")],
           [TDA, (DSN == "+" or DSA =="+") and (TAR =="+" or TAD =="+")],
           [TNL, TDC != "+" and TAR != "+" and TAD != "+"]]

    #this part of the function determines if the current string is compatible with the implicational structure
    for parameter, impl in par[:size]:
        if parameter != "0" and impl:
            continue
        elif parameter == "0" and not impl:
            continue
        else:
            return False
    return True


def count(num):
    #this is the set that contains the current grammars
    solutions = {'*'}
    for parameter in range(num):
        temp_solutions = set()
        candidates = set()
        #this iteration adds three potential grammars to the set examined (every possible grammar + one of the three symbols)
        for lang in solutions:
            candidates.add(lang + '+')
            candidates.add(lang + '-')
            candidates.add(lang + '0')
        #this iteration checks if the new grammars are compatible with the implications
        for cand in candidates:
            if check(cand) == True:
                temp_solutions.add(cand)
            else:
                pass
            solutions = temp_solutions
        print(parameter+1, len(solutions))
    return len(solutions)


if __name__ == '__main__':
    print(count(int(sys.argv[1])))


