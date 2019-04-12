PROGRAM prog0
VAR_INPUT x1 , x2 , f1 , f2 : REAL; END_VAR
VAR_OUTPUT V1 , V2 , P : BOOL; END_VAR

IF ( x1 >= H1 ) THEN V1 := 0 ; ELSE
IF ( x1 <= L1 ) THEN V1 := 1 ; END_IF ;
END_IF ;
IF ( x2 <= L2 ) THEN P : = 1 ; V2 : = 1 ; END_IF ;
IF ( x1 <= LL OR f2 <= FL OR x2 >= H2 ) THEN
P := 0 ; V2 := 0 ; END_IF ;

END_PROGRAM

CONFIGURATION Config0
    RESOURCE Res0 ON PLC
        TASK Main (INTERVAL: = T#1 s , PRIORITY : = 0 ) ;
        PROGRAM Inst0 WITH Main : prog0 ;
    END_RESOURCE
END_CONFIGURATION
