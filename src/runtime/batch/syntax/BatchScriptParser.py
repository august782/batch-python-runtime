# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 BatchScript.g 2012-11-27 16:47:28

import sys
from antlr3 import *
from antlr3.compat import set, frozenset
         
from batch.Expressions import *
from datetime import date



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
FUNCTION=8
EXPONENT=22
T__29=29
OCTAL_ESC=27
INPUT=10
FOR=7
FLOAT=18
ID=16
EOF=-1
IF=4
ESC_SEQ=28
THEN=5
IN=14
VAR=11
DIGIT=20
COMMENT=23
T__42=42
T__43=43
T__40=40
T__41=41
T__46=46
T__47=47
T__44=44
T__45=45
T__48=48
T__49=49
UNICODE_ESC=25
ELSE=6
HEX_DIGIT=26
INT=17
TRUE=12
ALPHA=21
T__30=30
T__31=31
T__32=32
WS=24
T__33=33
T__34=34
T__35=35
T__36=36
T__37=37
T__38=38
T__39=39
DATE=15
FALSE=13
OUTPUT=9
STRING=19

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "IF", "THEN", "ELSE", "FOR", "FUNCTION", "OUTPUT", "INPUT", "VAR", "TRUE", 
    "FALSE", "IN", "DATE", "ID", "INT", "FLOAT", "STRING", "DIGIT", "ALPHA", 
    "EXPONENT", "COMMENT", "WS", "UNICODE_ESC", "HEX_DIGIT", "OCTAL_ESC", 
    "ESC_SEQ", "';'", "'='", "'{'", "'}'", "'('", "')'", "'||'", "'&&'", 
    "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'+'", "'-'", "'*'", "'/'", 
    "'!'", "','", "'.'"
]




class BatchScriptParser(Parser):
    grammarFileName = "BatchScript.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 17, 2009 19:23:44")
    antlr_version_str = "3.1.3 Mar 17, 2009 19:23:44"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(BatchScriptParser, self).__init__(input, state, *args, **kwargs)






                


        



    # $ANTLR start "main"
    # BatchScript.g:27:1: main returns [value] : e= statements EOF ;
    def main(self, ):

        value = None

        e = None


        try:
            try:
                # BatchScript.g:28:5: (e= statements EOF )
                # BatchScript.g:28:9: e= statements EOF
                pass 
                self._state.following.append(self.FOLLOW_statements_in_main279)
                e = self.statements()

                self._state.following.pop()
                #action start
                value = e
                #action end
                self.match(self.input, EOF, self.FOLLOW_EOF_in_main283)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return value

    # $ANTLR end "main"


    # $ANTLR start "statements"
    # BatchScript.g:31:1: statements returns [value] : (e= statement ( ';' (es= statements )? )? | VAR x= ID '=' e= expr ';' b= statements );
    def statements(self, ):

        value = None

        x = None
        e = None

        es = None

        b = None


        try:
            try:
                # BatchScript.g:32:5: (e= statement ( ';' (es= statements )? )? | VAR x= ID '=' e= expr ';' b= statements )
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == IF or (FOR <= LA3_0 <= INPUT) or (TRUE <= LA3_0 <= FALSE) or (DATE <= LA3_0 <= STRING) or LA3_0 == 33 or LA3_0 == 47) :
                    alt3 = 1
                elif (LA3_0 == VAR) :
                    alt3 = 2
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae

                if alt3 == 1:
                    # BatchScript.g:32:9: e= statement ( ';' (es= statements )? )?
                    pass 
                    self._state.following.append(self.FOLLOW_statement_in_statements308)
                    e = self.statement()

                    self._state.following.pop()
                    #action start
                    value=e
                    #action end
                    # BatchScript.g:33:9: ( ';' (es= statements )? )?
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == 29) :
                        alt2 = 1
                    if alt2 == 1:
                        # BatchScript.g:33:11: ';' (es= statements )?
                        pass 
                        self.match(self.input, 29, self.FOLLOW_29_in_statements342)
                        # BatchScript.g:34:13: (es= statements )?
                        alt1 = 2
                        LA1_0 = self.input.LA(1)

                        if (LA1_0 == IF or (FOR <= LA1_0 <= FALSE) or (DATE <= LA1_0 <= STRING) or LA1_0 == 33 or LA1_0 == 47) :
                            alt1 = 1
                        if alt1 == 1:
                            # BatchScript.g:34:14: es= statements
                            pass 
                            self._state.following.append(self.FOLLOW_statements_in_statements359)
                            es = self.statements()

                            self._state.following.pop()
                            #action start
                            value = Seq(value,es)
                            #action end








                elif alt3 == 2:
                    # BatchScript.g:37:9: VAR x= ID '=' e= expr ';' b= statements
                    pass 
                    self.match(self.input, VAR, self.FOLLOW_VAR_in_statements415)
                    x=self.match(self.input, ID, self.FOLLOW_ID_in_statements419)
                    self.match(self.input, 30, self.FOLLOW_30_in_statements421)
                    self._state.following.append(self.FOLLOW_expr_in_statements425)
                    e = self.expr()

                    self._state.following.pop()
                    self.match(self.input, 29, self.FOLLOW_29_in_statements427)
                    self._state.following.append(self.FOLLOW_statements_in_statements431)
                    b = self.statements()

                    self._state.following.pop()
                    #action start
                    value = Let(x.getText(),e,b)
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return value

    # $ANTLR end "statements"


    # $ANTLR start "block"
    # BatchScript.g:40:1: block returns [Expression value] : ( '{' e= statements '}' | '{' '}' );
    def block(self, ):

        value = None

        e = None


        try:
            try:
                # BatchScript.g:41:5: ( '{' e= statements '}' | '{' '}' )
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 31) :
                    LA4_1 = self.input.LA(2)

                    if (LA4_1 == 32) :
                        alt4 = 2
                    elif (LA4_1 == IF or (FOR <= LA4_1 <= FALSE) or (DATE <= LA4_1 <= STRING) or LA4_1 == 33 or LA4_1 == 47) :
                        alt4 = 1
                    else:
                        nvae = NoViableAltException("", 4, 1, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae

                if alt4 == 1:
                    # BatchScript.g:41:7: '{' e= statements '}'
                    pass 
                    self.match(self.input, 31, self.FOLLOW_31_in_block454)
                    self._state.following.append(self.FOLLOW_statements_in_block458)
                    e = self.statements()

                    self._state.following.pop()
                    self.match(self.input, 32, self.FOLLOW_32_in_block460)
                    #action start
                    value =  e
                    #action end


                elif alt4 == 2:
                    # BatchScript.g:42:7: '{' '}'
                    pass 
                    self.match(self.input, 31, self.FOLLOW_31_in_block472)
                    self.match(self.input, 32, self.FOLLOW_32_in_block474)
                    #action start
                    value = Skip()
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return value

    # $ANTLR end "block"


    # $ANTLR start "statement"
    # BatchScript.g:45:1: statement returns [value] : ( FOR '(' x= ID IN e= expr ')' b= block | e= expr );
    def statement(self, ):

        value = None

        x = None
        e = None

        b = None


        try:
            try:
                # BatchScript.g:46:5: ( FOR '(' x= ID IN e= expr ')' b= block | e= expr )
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == FOR) :
                    alt5 = 1
                elif (LA5_0 == IF or (FUNCTION <= LA5_0 <= INPUT) or (TRUE <= LA5_0 <= FALSE) or (DATE <= LA5_0 <= STRING) or LA5_0 == 33 or LA5_0 == 47) :
                    alt5 = 2
                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae

                if alt5 == 1:
                    # BatchScript.g:46:9: FOR '(' x= ID IN e= expr ')' b= block
                    pass 
                    self.match(self.input, FOR, self.FOLLOW_FOR_in_statement513)
                    self.match(self.input, 33, self.FOLLOW_33_in_statement515)
                    x=self.match(self.input, ID, self.FOLLOW_ID_in_statement519)
                    self.match(self.input, IN, self.FOLLOW_IN_in_statement521)
                    self._state.following.append(self.FOLLOW_expr_in_statement525)
                    e = self.expr()

                    self._state.following.pop()
                    self.match(self.input, 34, self.FOLLOW_34_in_statement527)
                    self._state.following.append(self.FOLLOW_block_in_statement531)
                    b = self.block()

                    self._state.following.pop()
                    #action start
                    value = For(x.getText(),e,b)
                    #action end


                elif alt5 == 2:
                    # BatchScript.g:47:9: e= expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_statement547)
                    e = self.expr()

                    self._state.following.pop()
                    #action start
                    value = e
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return value

    # $ANTLR end "statement"


    # $ANTLR start "expr"
    # BatchScript.g:50:1: expr returns [value] : ( FUNCTION '(' x= ID ')' e= block | a= orexpr );
    def expr(self, ):

        value = None

        x = None
        e = None

        a = None


        try:
            try:
                # BatchScript.g:51:5: ( FUNCTION '(' x= ID ')' e= block | a= orexpr )
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == FUNCTION) :
                    alt6 = 1
                elif (LA6_0 == IF or (OUTPUT <= LA6_0 <= INPUT) or (TRUE <= LA6_0 <= FALSE) or (DATE <= LA6_0 <= STRING) or LA6_0 == 33 or LA6_0 == 47) :
                    alt6 = 2
                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # BatchScript.g:51:9: FUNCTION '(' x= ID ')' e= block
                    pass 
                    self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_expr601)
                    self.match(self.input, 33, self.FOLLOW_33_in_expr603)
                    x=self.match(self.input, ID, self.FOLLOW_ID_in_expr607)
                    self.match(self.input, 34, self.FOLLOW_34_in_expr609)
                    self._state.following.append(self.FOLLOW_block_in_expr613)
                    e = self.block()

                    self._state.following.pop()
                    #action start
                    value = Fun(x.getText(),e)
                    #action end


                elif alt6 == 2:
                    # BatchScript.g:52:9: a= orexpr
                    pass 
                    self._state.following.append(self.FOLLOW_orexpr_in_expr634)
                    a = self.orexpr()

                    self._state.following.pop()
                    #action start
                    value = a
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return value

    # $ANTLR end "expr"


    # $ANTLR start "orexpr"
    # BatchScript.g:55:1: orexpr returns [value] : a= andexpr ( '||' b= andexpr )* ;
    def orexpr(self, ):

        value = None

        a = None

        b = None


        try:
            try:
                # BatchScript.g:56:5: (a= andexpr ( '||' b= andexpr )* )
                # BatchScript.g:56:9: a= andexpr ( '||' b= andexpr )*
                pass 
                self._state.following.append(self.FOLLOW_andexpr_in_orexpr684)
                a = self.andexpr()

                self._state.following.pop()
                #action start
                value = a
                #action end
                # BatchScript.g:57:9: ( '||' b= andexpr )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == 35) :
                        alt7 = 1


                    if alt7 == 1:
                        # BatchScript.g:57:11: '||' b= andexpr
                        pass 
                        self.match(self.input, 35, self.FOLLOW_35_in_orexpr708)
                        self._state.following.append(self.FOLLOW_andexpr_in_orexpr712)
                        b = self.andexpr()

                        self._state.following.pop()
                        #action start
                        value = Or(value,b)
                        #action end


                    else:
                        break #loop7




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return value

    # $ANTLR end "orexpr"


    # $ANTLR start "andexpr"
    # BatchScript.g:61:1: andexpr returns [value] : a= comp ( '&&' b= comp )* ;
    def andexpr(self, ):

        value = None

        a = None

        b = None


        try:
            try:
                # BatchScript.g:62:5: (a= comp ( '&&' b= comp )* )
                # BatchScript.g:62:9: a= comp ( '&&' b= comp )*
                pass 
                self._state.following.append(self.FOLLOW_comp_in_andexpr753)
                a = self.comp()

                self._state.following.pop()
                #action start
                value = a
                #action end
                # BatchScript.g:63:9: ( '&&' b= comp )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == 36) :
                        alt8 = 1


                    if alt8 == 1:
                        # BatchScript.g:63:11: '&&' b= comp
                        pass 
                        self.match(self.input, 36, self.FOLLOW_36_in_andexpr777)
                        self._state.following.append(self.FOLLOW_comp_in_andexpr781)
                        b = self.comp()

                        self._state.following.pop()
                        #action start
                        value = And(value,b)
                        #action end


                    else:
                        break #loop8




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return value

    # $ANTLR end "andexpr"


    # $ANTLR start "comp"
    # BatchScript.g:67:1: comp returns [value] : a= term (op= compop b= term )* ;
    def comp(self, ):

        value = None

        a = None

        op = None

        b = None


        try:
            try:
                # BatchScript.g:68:5: (a= term (op= compop b= term )* )
                # BatchScript.g:68:9: a= term (op= compop b= term )*
                pass 
                self._state.following.append(self.FOLLOW_term_in_comp822)
                a = self.term()

                self._state.following.pop()
                #action start
                value = a
                #action end
                # BatchScript.g:69:9: (op= compop b= term )*
                while True: #loop9
                    alt9 = 2
                    LA9 = self.input.LA(1)
                    if LA9 == 37:
                        alt9 = 1
                    elif LA9 == 38:
                        alt9 = 1
                    elif LA9 == 39:
                        alt9 = 1
                    elif LA9 == 40:
                        alt9 = 1
                    elif LA9 == 41:
                        alt9 = 1
                    elif LA9 == 42:
                        alt9 = 1

                    if alt9 == 1:
                        # BatchScript.g:69:11: op= compop b= term
                        pass 
                        self._state.following.append(self.FOLLOW_compop_in_comp851)
                        op = self.compop()

                        self._state.following.pop()
                        self._state.following.append(self.FOLLOW_term_in_comp855)
                        b = self.term()

                        self._state.following.pop()
                        #action start
                        value = BinOp(op,value,b)
                        #action end


                    else:
                        break #loop9




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return value

    # $ANTLR end "comp"


    # $ANTLR start "compop"
    # BatchScript.g:73:1: compop returns [op] : ( '==' | '!=' | '<' | '<=' | '>' | '>=' );
    def compop(self, ):

        op = None

        try:
            try:
                # BatchScript.g:74:5: ( '==' | '!=' | '<' | '<=' | '>' | '>=' )
                alt10 = 6
                LA10 = self.input.LA(1)
                if LA10 == 37:
                    alt10 = 1
                elif LA10 == 38:
                    alt10 = 2
                elif LA10 == 39:
                    alt10 = 3
                elif LA10 == 40:
                    alt10 = 4
                elif LA10 == 41:
                    alt10 = 5
                elif LA10 == 42:
                    alt10 = 6
                else:
                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae

                if alt10 == 1:
                    # BatchScript.g:74:9: '=='
                    pass 
                    self.match(self.input, 37, self.FOLLOW_37_in_compop892)
                    #action start
                    op = '=='
                    #action end


                elif alt10 == 2:
                    # BatchScript.g:75:9: '!='
                    pass 
                    self.match(self.input, 38, self.FOLLOW_38_in_compop907)
                    #action start
                    op = '!='
                    #action end


                elif alt10 == 3:
                    # BatchScript.g:76:9: '<'
                    pass 
                    self.match(self.input, 39, self.FOLLOW_39_in_compop922)
                    #action start
                    op = '<'
                    #action end


                elif alt10 == 4:
                    # BatchScript.g:77:9: '<='
                    pass 
                    self.match(self.input, 40, self.FOLLOW_40_in_compop938)
                    #action start
                    op = '<='
                    #action end


                elif alt10 == 5:
                    # BatchScript.g:78:9: '>'
                    pass 
                    self.match(self.input, 41, self.FOLLOW_41_in_compop953)
                    #action start
                    op = '>'
                    #action end


                elif alt10 == 6:
                    # BatchScript.g:79:9: '>='
                    pass 
                    self.match(self.input, 42, self.FOLLOW_42_in_compop969)
                    #action start
                    op = '>='
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return op

    # $ANTLR end "compop"


    # $ANTLR start "term"
    # BatchScript.g:82:1: term returns [value] : a= factor (op= addop b= factor )* ;
    def term(self, ):

        value = None

        a = None

        op = None

        b = None


        try:
            try:
                # BatchScript.g:83:5: (a= factor (op= addop b= factor )* )
                # BatchScript.g:83:9: a= factor (op= addop b= factor )*
                pass 
                self._state.following.append(self.FOLLOW_factor_in_term999)
                a = self.factor()

                self._state.following.pop()
                #action start
                value = a
                #action end
                # BatchScript.g:84:9: (op= addop b= factor )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == 43) :
                        alt11 = 1
                    elif (LA11_0 == 44) :
                        alt11 = 1


                    if alt11 == 1:
                        # BatchScript.g:84:11: op= addop b= factor
                        pass 
                        self._state.following.append(self.FOLLOW_addop_in_term1026)
                        op = self.addop()

                        self._state.following.pop()
                        self._state.following.append(self.FOLLOW_factor_in_term1030)
                        b = self.factor()

                        self._state.following.pop()
                        #action start
                        value = BinOp(op,value,b)
                        #action end


                    else:
                        break #loop11




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return value

    # $ANTLR end "term"


    # $ANTLR start "addop"
    # BatchScript.g:88:1: addop returns [op] : ( '+' | '-' );
    def addop(self, ):

        op = None

        try:
            try:
                # BatchScript.g:89:5: ( '+' | '-' )
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == 43) :
                    alt12 = 1
                elif (LA12_0 == 44) :
                    alt12 = 2
                else:
                    nvae = NoViableAltException("", 12, 0, self.input)

                    raise nvae

                if alt12 == 1:
                    # BatchScript.g:89:9: '+'
                    pass 
                    self.match(self.input, 43, self.FOLLOW_43_in_addop1066)
                    #action start
                    op = '+'
                    #action end


                elif alt12 == 2:
                    # BatchScript.g:90:9: '-'
                    pass 
                    self.match(self.input, 44, self.FOLLOW_44_in_addop1078)
                    #action start
                    op = '-'
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return op

    # $ANTLR end "addop"


    # $ANTLR start "factor"
    # BatchScript.g:93:1: factor returns [value] : a= base (op= mulop b= base )* ;
    def factor(self, ):

        value = None

        a = None

        op = None

        b = None


        try:
            try:
                # BatchScript.g:94:5: (a= base (op= mulop b= base )* )
                # BatchScript.g:94:9: a= base (op= mulop b= base )*
                pass 
                self._state.following.append(self.FOLLOW_base_in_factor1105)
                a = self.base()

                self._state.following.pop()
                #action start
                value = a
                #action end
                # BatchScript.g:95:9: (op= mulop b= base )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == 45) :
                        alt13 = 1
                    elif (LA13_0 == 46) :
                        alt13 = 1


                    if alt13 == 1:
                        # BatchScript.g:95:11: op= mulop b= base
                        pass 
                        self._state.following.append(self.FOLLOW_mulop_in_factor1134)
                        op = self.mulop()

                        self._state.following.pop()
                        self._state.following.append(self.FOLLOW_base_in_factor1138)
                        b = self.base()

                        self._state.following.pop()
                        #action start
                        value = BinOp(op,value,b)
                        #action end


                    else:
                        break #loop13




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return value

    # $ANTLR end "factor"


    # $ANTLR start "mulop"
    # BatchScript.g:99:1: mulop returns [op] : ( '*' | '/' );
    def mulop(self, ):

        op = None

        try:
            try:
                # BatchScript.g:100:5: ( '*' | '/' )
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == 45) :
                    alt14 = 1
                elif (LA14_0 == 46) :
                    alt14 = 2
                else:
                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae

                if alt14 == 1:
                    # BatchScript.g:100:9: '*'
                    pass 
                    self.match(self.input, 45, self.FOLLOW_45_in_mulop1176)
                    #action start
                    op = '*'
                    #action end


                elif alt14 == 2:
                    # BatchScript.g:101:9: '/'
                    pass 
                    self.match(self.input, 46, self.FOLLOW_46_in_mulop1188)
                    #action start
                    op = '/'
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return op

    # $ANTLR end "mulop"


    # $ANTLR start "base"
    # BatchScript.g:104:1: base returns [value] : ( '!' e= base | e= assign | IF '(' a= expr ')' t= block ( ELSE e= block )? | x= INT | x= FLOAT | x= STRING | DATE '(' d= STRING ')' | x= TRUE | x= FALSE | '(' e= expr ')' );
    def base(self, ):

        value = None

        x = None
        d = None
        e = None

        a = None

        t = None


        try:
            try:
                # BatchScript.g:105:5: ( '!' e= base | e= assign | IF '(' a= expr ')' t= block ( ELSE e= block )? | x= INT | x= FLOAT | x= STRING | DATE '(' d= STRING ')' | x= TRUE | x= FALSE | '(' e= expr ')' )
                alt16 = 10
                LA16 = self.input.LA(1)
                if LA16 == 47:
                    alt16 = 1
                elif LA16 == OUTPUT or LA16 == INPUT or LA16 == ID:
                    alt16 = 2
                elif LA16 == IF:
                    alt16 = 3
                elif LA16 == INT:
                    alt16 = 4
                elif LA16 == FLOAT:
                    alt16 = 5
                elif LA16 == STRING:
                    alt16 = 6
                elif LA16 == DATE:
                    alt16 = 7
                elif LA16 == TRUE:
                    alt16 = 8
                elif LA16 == FALSE:
                    alt16 = 9
                elif LA16 == 33:
                    alt16 = 10
                else:
                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae

                if alt16 == 1:
                    # BatchScript.g:105:9: '!' e= base
                    pass 
                    self.match(self.input, 47, self.FOLLOW_47_in_base1213)
                    self._state.following.append(self.FOLLOW_base_in_base1217)
                    e = self.base()

                    self._state.following.pop()
                    #action start
                    value = Not(e)
                    #action end


                elif alt16 == 2:
                    # BatchScript.g:106:9: e= assign
                    pass 
                    self._state.following.append(self.FOLLOW_assign_in_base1233)
                    e = self.assign()

                    self._state.following.pop()
                    #action start
                    value = e
                    #action end


                elif alt16 == 3:
                    # BatchScript.g:107:9: IF '(' a= expr ')' t= block ( ELSE e= block )?
                    pass 
                    self.match(self.input, IF, self.FOLLOW_IF_in_base1260)
                    self.match(self.input, 33, self.FOLLOW_33_in_base1262)
                    self._state.following.append(self.FOLLOW_expr_in_base1266)
                    a = self.expr()

                    self._state.following.pop()
                    self.match(self.input, 34, self.FOLLOW_34_in_base1268)
                    self._state.following.append(self.FOLLOW_block_in_base1272)
                    t = self.block()

                    self._state.following.pop()
                    #action start
                    value = If(a,t,None)
                    #action end
                    # BatchScript.g:108:9: ( ELSE e= block )?
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == ELSE) :
                        alt15 = 1
                    if alt15 == 1:
                        # BatchScript.g:108:10: ELSE e= block
                        pass 
                        self.match(self.input, ELSE, self.FOLLOW_ELSE_in_base1286)
                        self._state.following.append(self.FOLLOW_block_in_base1290)
                        e = self.block()

                        self._state.following.pop()



                    #action start
                    value = If(a,t,e)
                    #action end


                elif alt16 == 4:
                    # BatchScript.g:109:9: x= INT
                    pass 
                    x=self.match(self.input, INT, self.FOLLOW_INT_in_base1314)
                    #action start
                    value = Data(int(x.getText()))
                    #action end


                elif alt16 == 5:
                    # BatchScript.g:110:9: x= FLOAT
                    pass 
                    x=self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_base1346)
                    #action start
                    value = Data(float(x.getText()))
                    #action end


                elif alt16 == 6:
                    # BatchScript.g:111:9: x= STRING
                    pass 
                    x=self.match(self.input, STRING, self.FOLLOW_STRING_in_base1376)
                    #action start
                    value = Data(x.getText()[1:-1].replace("\\\"","\"").replace("\\\\","\\"))
                    #action end


                elif alt16 == 7:
                    # BatchScript.g:112:9: DATE '(' d= STRING ')'
                    pass 
                    self.match(self.input, DATE, self.FOLLOW_DATE_in_base1403)
                    self.match(self.input, 33, self.FOLLOW_33_in_base1405)
                    d=self.match(self.input, STRING, self.FOLLOW_STRING_in_base1409)
                    self.match(self.input, 34, self.FOLLOW_34_in_base1411)
                    #action start
                    value = Data(d.getText())
                    #action end


                elif alt16 == 8:
                    # BatchScript.g:113:9: x= TRUE
                    pass 
                    x=self.match(self.input, TRUE, self.FOLLOW_TRUE_in_base1425)
                    #action start
                    value = Data(True)
                    #action end


                elif alt16 == 9:
                    # BatchScript.g:114:9: x= FALSE
                    pass 
                    x=self.match(self.input, FALSE, self.FOLLOW_FALSE_in_base1456)
                    #action start
                    value = Data(FALSE)
                    #action end


                elif alt16 == 10:
                    # BatchScript.g:115:9: '(' e= expr ')'
                    pass 
                    self.match(self.input, 33, self.FOLLOW_33_in_base1484)
                    self._state.following.append(self.FOLLOW_expr_in_base1488)
                    e = self.expr()

                    self._state.following.pop()
                    self.match(self.input, 34, self.FOLLOW_34_in_base1490)
                    #action start
                    value = e
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return value

    # $ANTLR end "base"


    # $ANTLR start "assign"
    # BatchScript.g:118:1: assign returns [value] : a= prim ( '=' b= expr )? ;
    def assign(self, ):

        value = None

        a = None

        b = None


        try:
            try:
                # BatchScript.g:119:5: (a= prim ( '=' b= expr )? )
                # BatchScript.g:119:9: a= prim ( '=' b= expr )?
                pass 
                self._state.following.append(self.FOLLOW_prim_in_assign1525)
                a = self.prim()

                self._state.following.pop()
                #action start
                value = a
                #action end
                # BatchScript.g:120:9: ( '=' b= expr )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == 30) :
                    alt17 = 1
                if alt17 == 1:
                    # BatchScript.g:120:11: '=' b= expr
                    pass 
                    self.match(self.input, 30, self.FOLLOW_30_in_assign1556)
                    self._state.following.append(self.FOLLOW_expr_in_assign1560)
                    b = self.expr()

                    self._state.following.pop()
                    #action start
                    value = Assign(a, b)
                    #action end







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return value

    # $ANTLR end "assign"


    # $ANTLR start "prim"
    # BatchScript.g:124:1: prim returns [value] : ( OUTPUT '(' b= STRING ',' e= expr ')' | INPUT '(' b= STRING ')' | b= ID r= access[value] );
    def prim(self, ):

        value = None

        b = None
        e = None

        r = None


        try:
            try:
                # BatchScript.g:125:5: ( OUTPUT '(' b= STRING ',' e= expr ')' | INPUT '(' b= STRING ')' | b= ID r= access[value] )
                alt18 = 3
                LA18 = self.input.LA(1)
                if LA18 == OUTPUT:
                    alt18 = 1
                elif LA18 == INPUT:
                    alt18 = 2
                elif LA18 == ID:
                    alt18 = 3
                else:
                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae

                if alt18 == 1:
                    # BatchScript.g:125:9: OUTPUT '(' b= STRING ',' e= expr ')'
                    pass 
                    self.match(self.input, OUTPUT, self.FOLLOW_OUTPUT_in_prim1599)
                    self.match(self.input, 33, self.FOLLOW_33_in_prim1601)
                    b=self.match(self.input, STRING, self.FOLLOW_STRING_in_prim1605)
                    self.match(self.input, 48, self.FOLLOW_48_in_prim1607)
                    self._state.following.append(self.FOLLOW_expr_in_prim1611)
                    e = self.expr()

                    self._state.following.pop()
                    self.match(self.input, 34, self.FOLLOW_34_in_prim1613)
                    #action start
                    value = Out(b.getText()[1:-1], e)
                    #action end


                elif alt18 == 2:
                    # BatchScript.g:126:9: INPUT '(' b= STRING ')'
                    pass 
                    self.match(self.input, INPUT, self.FOLLOW_INPUT_in_prim1626)
                    self.match(self.input, 33, self.FOLLOW_33_in_prim1629)
                    b=self.match(self.input, STRING, self.FOLLOW_STRING_in_prim1633)
                    self.match(self.input, 34, self.FOLLOW_34_in_prim1635)
                    #action start
                    value = In(b.getText()[1:-1])
                    #action end


                elif alt18 == 3:
                    # BatchScript.g:127:9: b= ID r= access[value]
                    pass 
                    b=self.match(self.input, ID, self.FOLLOW_ID_in_prim1649)
                    #action start
                    value = Var(b.getText())
                    #action end
                    self._state.following.append(self.FOLLOW_access_in_prim1676)
                    r = self.access(value)

                    self._state.following.pop()
                    #action start
                    value = r
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return value

    # $ANTLR end "prim"


    # $ANTLR start "access"
    # BatchScript.g:131:1: access[base] returns [value] : ( '.' x= ID ( '(' (a= args )? ')' )? r= access[value] | );
    def access(self, base):

        value = None

        x = None
        a = None

        r = None


        try:
            try:
                # BatchScript.g:132:5: ( '.' x= ID ( '(' (a= args )? ')' )? r= access[value] | )
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == 49) :
                    alt21 = 1
                elif (LA21_0 == EOF or (29 <= LA21_0 <= 30) or LA21_0 == 32 or (34 <= LA21_0 <= 46) or LA21_0 == 48) :
                    alt21 = 2
                else:
                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae

                if alt21 == 1:
                    # BatchScript.g:132:9: '.' x= ID ( '(' (a= args )? ')' )? r= access[value]
                    pass 
                    self.match(self.input, 49, self.FOLLOW_49_in_access1705)
                    x=self.match(self.input, ID, self.FOLLOW_ID_in_access1709)
                    #action start
                    value = Prop(base, x.getText())
                    #action end
                    # BatchScript.g:133:9: ( '(' (a= args )? ')' )?
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == 33) :
                        alt20 = 1
                    if alt20 == 1:
                        # BatchScript.g:133:11: '(' (a= args )? ')'
                        pass 
                        self.match(self.input, 33, self.FOLLOW_33_in_access1730)
                        # BatchScript.g:133:16: (a= args )?
                        alt19 = 2
                        LA19_0 = self.input.LA(1)

                        if (LA19_0 == IF or (FUNCTION <= LA19_0 <= INPUT) or (TRUE <= LA19_0 <= FALSE) or (DATE <= LA19_0 <= STRING) or LA19_0 == 33 or LA19_0 == 47) :
                            alt19 = 1
                        if alt19 == 1:
                            # BatchScript.g:133:16: a= args
                            pass 
                            self._state.following.append(self.FOLLOW_args_in_access1734)
                            a = self.args()

                            self._state.following.pop()



                        #action start
                        value = Call(base, x.getText(), a)
                        #action end
                        self.match(self.input, 34, self.FOLLOW_34_in_access1753)



                    self._state.following.append(self.FOLLOW_access_in_access1776)
                    r = self.access(value)

                    self._state.following.pop()
                    #action start
                    value = r
                    #action end


                elif alt21 == 2:
                    # BatchScript.g:137:25: 
                    pass 
                    #action start
                    value = base
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return value

    # $ANTLR end "access"


    # $ANTLR start "args"
    # BatchScript.g:140:1: args returns [arglist] : a= expr ( ',' rest= args )? ;
    def args(self, ):

        arglist = None

        a = None

        rest = None


        try:
            try:
                # BatchScript.g:141:5: (a= expr ( ',' rest= args )? )
                # BatchScript.g:141:9: a= expr ( ',' rest= args )?
                pass 
                #action start
                arglist = []
                #action end
                self._state.following.append(self.FOLLOW_expr_in_args1840)
                a = self.expr()

                self._state.following.pop()
                #action start
                arglist = [a]
                #action end
                # BatchScript.g:143:9: ( ',' rest= args )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == 48) :
                    alt22 = 1
                if alt22 == 1:
                    # BatchScript.g:143:11: ',' rest= args
                    pass 
                    self.match(self.input, 48, self.FOLLOW_48_in_args1863)
                    self._state.following.append(self.FOLLOW_args_in_args1867)
                    rest = self.args()

                    self._state.following.pop()
                    #action start
                    arglist+=rest;
                    #action end







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return arglist

    # $ANTLR end "args"


    # $ANTLR start "dateargs"
    # BatchScript.g:147:1: dateargs returns [value] : y= INT ',' m= INT ',' d= INT ;
    def dateargs(self, ):

        value = None

        y = None
        m = None
        d = None

        try:
            try:
                # BatchScript.g:148:5: (y= INT ',' m= INT ',' d= INT )
                # BatchScript.g:148:9: y= INT ',' m= INT ',' d= INT
                pass 
                y=self.match(self.input, INT, self.FOLLOW_INT_in_dateargs1905)
                self.match(self.input, 48, self.FOLLOW_48_in_dateargs1907)
                m=self.match(self.input, INT, self.FOLLOW_INT_in_dateargs1911)
                self.match(self.input, 48, self.FOLLOW_48_in_dateargs1913)
                d=self.match(self.input, INT, self.FOLLOW_INT_in_dateargs1917)
                #action start
                value = date(int(y.getText()), int(m.getText()), int(d.getText()))
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return value

    # $ANTLR end "dateargs"


    # Delegated rules


 

    FOLLOW_statements_in_main279 = frozenset([])
    FOLLOW_EOF_in_main283 = frozenset([1])
    FOLLOW_statement_in_statements308 = frozenset([1, 29])
    FOLLOW_29_in_statements342 = frozenset([1, 4, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 33, 47])
    FOLLOW_statements_in_statements359 = frozenset([1])
    FOLLOW_VAR_in_statements415 = frozenset([16])
    FOLLOW_ID_in_statements419 = frozenset([30])
    FOLLOW_30_in_statements421 = frozenset([4, 7, 8, 9, 10, 12, 13, 15, 16, 17, 18, 19, 33, 47])
    FOLLOW_expr_in_statements425 = frozenset([29])
    FOLLOW_29_in_statements427 = frozenset([4, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 33, 47])
    FOLLOW_statements_in_statements431 = frozenset([1])
    FOLLOW_31_in_block454 = frozenset([4, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 33, 47])
    FOLLOW_statements_in_block458 = frozenset([32])
    FOLLOW_32_in_block460 = frozenset([1])
    FOLLOW_31_in_block472 = frozenset([32])
    FOLLOW_32_in_block474 = frozenset([1])
    FOLLOW_FOR_in_statement513 = frozenset([33])
    FOLLOW_33_in_statement515 = frozenset([16])
    FOLLOW_ID_in_statement519 = frozenset([14])
    FOLLOW_IN_in_statement521 = frozenset([4, 7, 8, 9, 10, 12, 13, 15, 16, 17, 18, 19, 33, 47])
    FOLLOW_expr_in_statement525 = frozenset([34])
    FOLLOW_34_in_statement527 = frozenset([31])
    FOLLOW_block_in_statement531 = frozenset([1])
    FOLLOW_expr_in_statement547 = frozenset([1])
    FOLLOW_FUNCTION_in_expr601 = frozenset([33])
    FOLLOW_33_in_expr603 = frozenset([16])
    FOLLOW_ID_in_expr607 = frozenset([34])
    FOLLOW_34_in_expr609 = frozenset([31])
    FOLLOW_block_in_expr613 = frozenset([1])
    FOLLOW_orexpr_in_expr634 = frozenset([1])
    FOLLOW_andexpr_in_orexpr684 = frozenset([1, 35])
    FOLLOW_35_in_orexpr708 = frozenset([4, 7, 8, 9, 10, 12, 13, 15, 16, 17, 18, 19, 33, 47])
    FOLLOW_andexpr_in_orexpr712 = frozenset([1, 35])
    FOLLOW_comp_in_andexpr753 = frozenset([1, 36])
    FOLLOW_36_in_andexpr777 = frozenset([4, 7, 8, 9, 10, 12, 13, 15, 16, 17, 18, 19, 33, 47])
    FOLLOW_comp_in_andexpr781 = frozenset([1, 36])
    FOLLOW_term_in_comp822 = frozenset([1, 37, 38, 39, 40, 41, 42])
    FOLLOW_compop_in_comp851 = frozenset([4, 7, 8, 9, 10, 12, 13, 15, 16, 17, 18, 19, 33, 47])
    FOLLOW_term_in_comp855 = frozenset([1, 37, 38, 39, 40, 41, 42])
    FOLLOW_37_in_compop892 = frozenset([1])
    FOLLOW_38_in_compop907 = frozenset([1])
    FOLLOW_39_in_compop922 = frozenset([1])
    FOLLOW_40_in_compop938 = frozenset([1])
    FOLLOW_41_in_compop953 = frozenset([1])
    FOLLOW_42_in_compop969 = frozenset([1])
    FOLLOW_factor_in_term999 = frozenset([1, 43, 44])
    FOLLOW_addop_in_term1026 = frozenset([4, 7, 8, 9, 10, 12, 13, 15, 16, 17, 18, 19, 33, 47])
    FOLLOW_factor_in_term1030 = frozenset([1, 43, 44])
    FOLLOW_43_in_addop1066 = frozenset([1])
    FOLLOW_44_in_addop1078 = frozenset([1])
    FOLLOW_base_in_factor1105 = frozenset([1, 45, 46])
    FOLLOW_mulop_in_factor1134 = frozenset([4, 7, 8, 9, 10, 12, 13, 15, 16, 17, 18, 19, 33, 47])
    FOLLOW_base_in_factor1138 = frozenset([1, 45, 46])
    FOLLOW_45_in_mulop1176 = frozenset([1])
    FOLLOW_46_in_mulop1188 = frozenset([1])
    FOLLOW_47_in_base1213 = frozenset([4, 7, 8, 9, 10, 12, 13, 15, 16, 17, 18, 19, 33, 47])
    FOLLOW_base_in_base1217 = frozenset([1])
    FOLLOW_assign_in_base1233 = frozenset([1])
    FOLLOW_IF_in_base1260 = frozenset([33])
    FOLLOW_33_in_base1262 = frozenset([4, 7, 8, 9, 10, 12, 13, 15, 16, 17, 18, 19, 33, 47])
    FOLLOW_expr_in_base1266 = frozenset([34])
    FOLLOW_34_in_base1268 = frozenset([31])
    FOLLOW_block_in_base1272 = frozenset([1, 6])
    FOLLOW_ELSE_in_base1286 = frozenset([31])
    FOLLOW_block_in_base1290 = frozenset([1])
    FOLLOW_INT_in_base1314 = frozenset([1])
    FOLLOW_FLOAT_in_base1346 = frozenset([1])
    FOLLOW_STRING_in_base1376 = frozenset([1])
    FOLLOW_DATE_in_base1403 = frozenset([33])
    FOLLOW_33_in_base1405 = frozenset([19])
    FOLLOW_STRING_in_base1409 = frozenset([34])
    FOLLOW_34_in_base1411 = frozenset([1])
    FOLLOW_TRUE_in_base1425 = frozenset([1])
    FOLLOW_FALSE_in_base1456 = frozenset([1])
    FOLLOW_33_in_base1484 = frozenset([4, 7, 8, 9, 10, 12, 13, 15, 16, 17, 18, 19, 33, 47])
    FOLLOW_expr_in_base1488 = frozenset([34])
    FOLLOW_34_in_base1490 = frozenset([1])
    FOLLOW_prim_in_assign1525 = frozenset([1, 30])
    FOLLOW_30_in_assign1556 = frozenset([4, 7, 8, 9, 10, 12, 13, 15, 16, 17, 18, 19, 33, 47])
    FOLLOW_expr_in_assign1560 = frozenset([1])
    FOLLOW_OUTPUT_in_prim1599 = frozenset([33])
    FOLLOW_33_in_prim1601 = frozenset([19])
    FOLLOW_STRING_in_prim1605 = frozenset([48])
    FOLLOW_48_in_prim1607 = frozenset([4, 7, 8, 9, 10, 12, 13, 15, 16, 17, 18, 19, 33, 47])
    FOLLOW_expr_in_prim1611 = frozenset([34])
    FOLLOW_34_in_prim1613 = frozenset([1])
    FOLLOW_INPUT_in_prim1626 = frozenset([33])
    FOLLOW_33_in_prim1629 = frozenset([19])
    FOLLOW_STRING_in_prim1633 = frozenset([34])
    FOLLOW_34_in_prim1635 = frozenset([1])
    FOLLOW_ID_in_prim1649 = frozenset([49])
    FOLLOW_access_in_prim1676 = frozenset([1])
    FOLLOW_49_in_access1705 = frozenset([16])
    FOLLOW_ID_in_access1709 = frozenset([33, 49])
    FOLLOW_33_in_access1730 = frozenset([4, 7, 8, 9, 10, 12, 13, 15, 16, 17, 18, 19, 33, 34, 47])
    FOLLOW_args_in_access1734 = frozenset([34])
    FOLLOW_34_in_access1753 = frozenset([49])
    FOLLOW_access_in_access1776 = frozenset([1])
    FOLLOW_expr_in_args1840 = frozenset([1, 48])
    FOLLOW_48_in_args1863 = frozenset([4, 7, 8, 9, 10, 12, 13, 15, 16, 17, 18, 19, 33, 47])
    FOLLOW_args_in_args1867 = frozenset([1])
    FOLLOW_INT_in_dateargs1905 = frozenset([48])
    FOLLOW_48_in_dateargs1907 = frozenset([17])
    FOLLOW_INT_in_dateargs1911 = frozenset([48])
    FOLLOW_48_in_dateargs1913 = frozenset([17])
    FOLLOW_INT_in_dateargs1917 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("BatchScriptLexer", BatchScriptParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
