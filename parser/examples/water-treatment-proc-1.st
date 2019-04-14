PROGRAM prog0
VAR_INPUT f1 , f2 : REAL; END_VAR
VAR_OUTPUT V1 , V2 , P : BOOL; END_VAR
VAR x1, x2, H1, L1, H2, L2, HH, LL, FL, e : REAL; END_VAR

IF ((f1 > ( (HH - x1) /e))) THEN    V1:= 0; ELSE
    IF (( NOT(f1 > ( (HH - x1) /e)))) THEN
        IF ((x1 < L1)) THEN    V1:= 1;
        END_IF;
    END_IF;
END_IF;
IF ((x2 < L2)) THEN    P:= 1;  V2:= 1;
END_IF;
IF (((((V1 * f1) - ((V2 * P) * f2)) < ( (LL - x1) /e)) OR ((f2 < FL) OR (((V2 * P) * f2) > ( (HH - x2) /e))))) THEN    P:= 0;  V2:= 0;
END_IF;
END_PROGRAM

CONFIGURATION Config0
    RESOURCE Res0 ON PLC
        TASK Main (INTERVAL:= T#1 s , PRIORITY := 0 ) ;
        PROGRAM Inst0 WITH Main : prog0 ;
    END_RESOURCE
END_CONFIGURATION
