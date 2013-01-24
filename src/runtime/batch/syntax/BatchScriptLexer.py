# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 BatchScript.g 2012-11-27 16:47:28

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


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
IN=14
THEN=5
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


class BatchScriptLexer(Lexer):

    grammarFileName = "BatchScript.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 17, 2009 19:23:44")
    antlr_version_str = "3.1.3 Mar 17, 2009 19:23:44"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(BatchScriptLexer, self).__init__(input, state)


        self.dfa10 = self.DFA10(
            self, 10,
            eot = self.DFA10_eot,
            eof = self.DFA10_eof,
            min = self.DFA10_min,
            max = self.DFA10_max,
            accept = self.DFA10_accept,
            special = self.DFA10_special,
            transition = self.DFA10_transition
            )

        self.dfa20 = self.DFA20(
            self, 20,
            eot = self.DFA20_eot,
            eof = self.DFA20_eof,
            min = self.DFA20_min,
            max = self.DFA20_max,
            accept = self.DFA20_accept,
            special = self.DFA20_special,
            transition = self.DFA20_transition
            )






    # $ANTLR start "IF"
    def mIF(self, ):

        try:
            _type = IF
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:7:4: ( 'if' )
            # BatchScript.g:7:6: 'if'
            pass 
            self.match("if")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IF"



    # $ANTLR start "THEN"
    def mTHEN(self, ):

        try:
            _type = THEN
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:8:6: ( 'then' )
            # BatchScript.g:8:8: 'then'
            pass 
            self.match("then")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "THEN"



    # $ANTLR start "ELSE"
    def mELSE(self, ):

        try:
            _type = ELSE
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:9:6: ( 'else' )
            # BatchScript.g:9:8: 'else'
            pass 
            self.match("else")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ELSE"



    # $ANTLR start "FOR"
    def mFOR(self, ):

        try:
            _type = FOR
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:10:5: ( 'for' )
            # BatchScript.g:10:7: 'for'
            pass 
            self.match("for")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FOR"



    # $ANTLR start "FUNCTION"
    def mFUNCTION(self, ):

        try:
            _type = FUNCTION
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:11:10: ( 'function' )
            # BatchScript.g:11:12: 'function'
            pass 
            self.match("function")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FUNCTION"



    # $ANTLR start "OUTPUT"
    def mOUTPUT(self, ):

        try:
            _type = OUTPUT
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:12:8: ( 'OUTPUT' )
            # BatchScript.g:12:10: 'OUTPUT'
            pass 
            self.match("OUTPUT")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OUTPUT"



    # $ANTLR start "INPUT"
    def mINPUT(self, ):

        try:
            _type = INPUT
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:13:7: ( 'INPUT' )
            # BatchScript.g:13:9: 'INPUT'
            pass 
            self.match("INPUT")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INPUT"



    # $ANTLR start "VAR"
    def mVAR(self, ):

        try:
            _type = VAR
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:14:5: ( 'var' )
            # BatchScript.g:14:7: 'var'
            pass 
            self.match("var")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "VAR"



    # $ANTLR start "TRUE"
    def mTRUE(self, ):

        try:
            _type = TRUE
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:15:6: ( 'true' )
            # BatchScript.g:15:8: 'true'
            pass 
            self.match("true")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TRUE"



    # $ANTLR start "FALSE"
    def mFALSE(self, ):

        try:
            _type = FALSE
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:16:7: ( 'false' )
            # BatchScript.g:16:9: 'false'
            pass 
            self.match("false")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FALSE"



    # $ANTLR start "IN"
    def mIN(self, ):

        try:
            _type = IN
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:17:4: ( 'in' )
            # BatchScript.g:17:6: 'in'
            pass 
            self.match("in")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IN"



    # $ANTLR start "DATE"
    def mDATE(self, ):

        try:
            _type = DATE
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:18:6: ( 'date' )
            # BatchScript.g:18:8: 'date'
            pass 
            self.match("date")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DATE"



    # $ANTLR start "T__29"
    def mT__29(self, ):

        try:
            _type = T__29
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:19:7: ( ';' )
            # BatchScript.g:19:9: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__29"



    # $ANTLR start "T__30"
    def mT__30(self, ):

        try:
            _type = T__30
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:20:7: ( '=' )
            # BatchScript.g:20:9: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__30"



    # $ANTLR start "T__31"
    def mT__31(self, ):

        try:
            _type = T__31
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:21:7: ( '{' )
            # BatchScript.g:21:9: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__31"



    # $ANTLR start "T__32"
    def mT__32(self, ):

        try:
            _type = T__32
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:22:7: ( '}' )
            # BatchScript.g:22:9: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__32"



    # $ANTLR start "T__33"
    def mT__33(self, ):

        try:
            _type = T__33
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:23:7: ( '(' )
            # BatchScript.g:23:9: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__33"



    # $ANTLR start "T__34"
    def mT__34(self, ):

        try:
            _type = T__34
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:24:7: ( ')' )
            # BatchScript.g:24:9: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__34"



    # $ANTLR start "T__35"
    def mT__35(self, ):

        try:
            _type = T__35
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:25:7: ( '||' )
            # BatchScript.g:25:9: '||'
            pass 
            self.match("||")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__35"



    # $ANTLR start "T__36"
    def mT__36(self, ):

        try:
            _type = T__36
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:26:7: ( '&&' )
            # BatchScript.g:26:9: '&&'
            pass 
            self.match("&&")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__36"



    # $ANTLR start "T__37"
    def mT__37(self, ):

        try:
            _type = T__37
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:27:7: ( '==' )
            # BatchScript.g:27:9: '=='
            pass 
            self.match("==")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__37"



    # $ANTLR start "T__38"
    def mT__38(self, ):

        try:
            _type = T__38
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:28:7: ( '!=' )
            # BatchScript.g:28:9: '!='
            pass 
            self.match("!=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__38"



    # $ANTLR start "T__39"
    def mT__39(self, ):

        try:
            _type = T__39
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:29:7: ( '<' )
            # BatchScript.g:29:9: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__39"



    # $ANTLR start "T__40"
    def mT__40(self, ):

        try:
            _type = T__40
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:30:7: ( '<=' )
            # BatchScript.g:30:9: '<='
            pass 
            self.match("<=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__40"



    # $ANTLR start "T__41"
    def mT__41(self, ):

        try:
            _type = T__41
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:31:7: ( '>' )
            # BatchScript.g:31:9: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__41"



    # $ANTLR start "T__42"
    def mT__42(self, ):

        try:
            _type = T__42
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:32:7: ( '>=' )
            # BatchScript.g:32:9: '>='
            pass 
            self.match(">=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__42"



    # $ANTLR start "T__43"
    def mT__43(self, ):

        try:
            _type = T__43
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:33:7: ( '+' )
            # BatchScript.g:33:9: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__43"



    # $ANTLR start "T__44"
    def mT__44(self, ):

        try:
            _type = T__44
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:34:7: ( '-' )
            # BatchScript.g:34:9: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__44"



    # $ANTLR start "T__45"
    def mT__45(self, ):

        try:
            _type = T__45
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:35:7: ( '*' )
            # BatchScript.g:35:9: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__45"



    # $ANTLR start "T__46"
    def mT__46(self, ):

        try:
            _type = T__46
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:36:7: ( '/' )
            # BatchScript.g:36:9: '/'
            pass 
            self.match(47)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__46"



    # $ANTLR start "T__47"
    def mT__47(self, ):

        try:
            _type = T__47
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:37:7: ( '!' )
            # BatchScript.g:37:9: '!'
            pass 
            self.match(33)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__47"



    # $ANTLR start "T__48"
    def mT__48(self, ):

        try:
            _type = T__48
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:38:7: ( ',' )
            # BatchScript.g:38:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__48"



    # $ANTLR start "T__49"
    def mT__49(self, ):

        try:
            _type = T__49
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:39:7: ( '.' )
            # BatchScript.g:39:9: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__49"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):

        try:
            # BatchScript.g:152:9: ( '0' .. '9' )
            # BatchScript.g:152:13: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "DIGIT"



    # $ANTLR start "ALPHA"
    def mALPHA(self, ):

        try:
            # BatchScript.g:155:9: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) )
            # BatchScript.g:155:13: ( 'a' .. 'z' | 'A' .. 'Z' | '_' )
            pass 
            if (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "ALPHA"



    # $ANTLR start "ID"
    def mID(self, ):

        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:157:9: ( ALPHA ( ALPHA | DIGIT )* | ( '*' ) )
            alt2 = 2
            LA2_0 = self.input.LA(1)

            if ((65 <= LA2_0 <= 90) or LA2_0 == 95 or (97 <= LA2_0 <= 122)) :
                alt2 = 1
            elif (LA2_0 == 42) :
                alt2 = 2
            else:
                nvae = NoViableAltException("", 2, 0, self.input)

                raise nvae

            if alt2 == 1:
                # BatchScript.g:157:13: ALPHA ( ALPHA | DIGIT )*
                pass 
                self.mALPHA()
                # BatchScript.g:157:19: ( ALPHA | DIGIT )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((48 <= LA1_0 <= 57) or (65 <= LA1_0 <= 90) or LA1_0 == 95 or (97 <= LA1_0 <= 122)) :
                        alt1 = 1


                    if alt1 == 1:
                        # BatchScript.g:
                        pass 
                        if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop1


            elif alt2 == 2:
                # BatchScript.g:158:13: ( '*' )
                pass 
                # BatchScript.g:158:13: ( '*' )
                # BatchScript.g:158:14: '*'
                pass 
                self.match(42)





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ID"



    # $ANTLR start "INT"
    def mINT(self, ):

        try:
            _type = INT
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:161:9: ( ( DIGIT )+ )
            # BatchScript.g:161:13: ( DIGIT )+
            pass 
            # BatchScript.g:161:13: ( DIGIT )+
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((48 <= LA3_0 <= 57)) :
                    alt3 = 1


                if alt3 == 1:
                    # BatchScript.g:161:13: DIGIT
                    pass 
                    self.mDIGIT()


                else:
                    if cnt3 >= 1:
                        break #loop3

                    eee = EarlyExitException(3, self.input)
                    raise eee

                cnt3 += 1



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INT"



    # $ANTLR start "FLOAT"
    def mFLOAT(self, ):

        try:
            _type = FLOAT
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:162:9: ( ( DIGIT )+ '.' ( DIGIT )* ( EXPONENT )? | '.' ( DIGIT )+ ( EXPONENT )? | ( DIGIT )+ EXPONENT )
            alt10 = 3
            alt10 = self.dfa10.predict(self.input)
            if alt10 == 1:
                # BatchScript.g:162:13: ( DIGIT )+ '.' ( DIGIT )* ( EXPONENT )?
                pass 
                # BatchScript.g:162:13: ( DIGIT )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if ((48 <= LA4_0 <= 57)) :
                        alt4 = 1


                    if alt4 == 1:
                        # BatchScript.g:162:13: DIGIT
                        pass 
                        self.mDIGIT()


                    else:
                        if cnt4 >= 1:
                            break #loop4

                        eee = EarlyExitException(4, self.input)
                        raise eee

                    cnt4 += 1
                self.match(46)
                # BatchScript.g:162:24: ( DIGIT )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if ((48 <= LA5_0 <= 57)) :
                        alt5 = 1


                    if alt5 == 1:
                        # BatchScript.g:162:24: DIGIT
                        pass 
                        self.mDIGIT()


                    else:
                        break #loop5
                # BatchScript.g:162:31: ( EXPONENT )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 69 or LA6_0 == 101) :
                    alt6 = 1
                if alt6 == 1:
                    # BatchScript.g:162:31: EXPONENT
                    pass 
                    self.mEXPONENT()





            elif alt10 == 2:
                # BatchScript.g:162:43: '.' ( DIGIT )+ ( EXPONENT )?
                pass 
                self.match(46)
                # BatchScript.g:162:47: ( DIGIT )+
                cnt7 = 0
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if ((48 <= LA7_0 <= 57)) :
                        alt7 = 1


                    if alt7 == 1:
                        # BatchScript.g:162:47: DIGIT
                        pass 
                        self.mDIGIT()


                    else:
                        if cnt7 >= 1:
                            break #loop7

                        eee = EarlyExitException(7, self.input)
                        raise eee

                    cnt7 += 1
                # BatchScript.g:162:54: ( EXPONENT )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == 69 or LA8_0 == 101) :
                    alt8 = 1
                if alt8 == 1:
                    # BatchScript.g:162:54: EXPONENT
                    pass 
                    self.mEXPONENT()





            elif alt10 == 3:
                # BatchScript.g:162:66: ( DIGIT )+ EXPONENT
                pass 
                # BatchScript.g:162:66: ( DIGIT )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if ((48 <= LA9_0 <= 57)) :
                        alt9 = 1


                    if alt9 == 1:
                        # BatchScript.g:162:66: DIGIT
                        pass 
                        self.mDIGIT()


                    else:
                        if cnt9 >= 1:
                            break #loop9

                        eee = EarlyExitException(9, self.input)
                        raise eee

                    cnt9 += 1
                self.mEXPONENT()


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FLOAT"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):

        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:164:9: ( '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' | '/*' ( options {greedy=false; } : . )* '*/' )
            alt14 = 2
            LA14_0 = self.input.LA(1)

            if (LA14_0 == 47) :
                LA14_1 = self.input.LA(2)

                if (LA14_1 == 47) :
                    alt14 = 1
                elif (LA14_1 == 42) :
                    alt14 = 2
                else:
                    nvae = NoViableAltException("", 14, 1, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 14, 0, self.input)

                raise nvae

            if alt14 == 1:
                # BatchScript.g:164:13: '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
                pass 
                self.match("//")
                # BatchScript.g:164:18: (~ ( '\\n' | '\\r' ) )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if ((0 <= LA11_0 <= 9) or (11 <= LA11_0 <= 12) or (14 <= LA11_0 <= 65535)) :
                        alt11 = 1


                    if alt11 == 1:
                        # BatchScript.g:164:18: ~ ( '\\n' | '\\r' )
                        pass 
                        if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop11
                # BatchScript.g:164:32: ( '\\r' )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == 13) :
                    alt12 = 1
                if alt12 == 1:
                    # BatchScript.g:164:32: '\\r'
                    pass 
                    self.match(13)



                self.match(10)
                #action start
                _channel=HIDDEN;
                #action end


            elif alt14 == 2:
                # BatchScript.g:165:13: '/*' ( options {greedy=false; } : . )* '*/'
                pass 
                self.match("/*")
                # BatchScript.g:165:18: ( options {greedy=false; } : . )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == 42) :
                        LA13_1 = self.input.LA(2)

                        if (LA13_1 == 47) :
                            alt13 = 2
                        elif ((0 <= LA13_1 <= 46) or (48 <= LA13_1 <= 65535)) :
                            alt13 = 1


                    elif ((0 <= LA13_0 <= 41) or (43 <= LA13_0 <= 65535)) :
                        alt13 = 1


                    if alt13 == 1:
                        # BatchScript.g:165:46: .
                        pass 
                        self.matchAny()


                    else:
                        break #loop13
                self.match("*/")
                #action start
                _channel=HIDDEN;
                #action end


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:168:9: ( ( ' ' | '\\t' | '\\r' | '\\n' ) )
            # BatchScript.g:168:13: ( ' ' | '\\t' | '\\r' | '\\n' )
            pass 
            if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            #action start
            _channel=HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    # $ANTLR start "STRING"
    def mSTRING(self, ):

        try:
            _type = STRING
            _channel = DEFAULT_CHANNEL

            # BatchScript.g:171:9: ( '\"' ( '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' ) | UNICODE_ESC | ~ ( '\\\\' | '\"' ) )* '\"' )
            # BatchScript.g:171:13: '\"' ( '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' ) | UNICODE_ESC | ~ ( '\\\\' | '\"' ) )* '\"'
            pass 
            self.match(34)
            # BatchScript.g:171:17: ( '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' ) | UNICODE_ESC | ~ ( '\\\\' | '\"' ) )*
            while True: #loop15
                alt15 = 4
                LA15_0 = self.input.LA(1)

                if (LA15_0 == 92) :
                    LA15_2 = self.input.LA(2)

                    if (LA15_2 == 34 or LA15_2 == 39 or LA15_2 == 92 or LA15_2 == 98 or LA15_2 == 102 or LA15_2 == 110 or LA15_2 == 114 or LA15_2 == 116) :
                        alt15 = 1
                    elif (LA15_2 == 117) :
                        alt15 = 2


                elif ((0 <= LA15_0 <= 33) or (35 <= LA15_0 <= 91) or (93 <= LA15_0 <= 65535)) :
                    alt15 = 3


                if alt15 == 1:
                    # BatchScript.g:171:19: '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' )
                    pass 
                    self.match(92)
                    if self.input.LA(1) == 34 or self.input.LA(1) == 39 or self.input.LA(1) == 92 or self.input.LA(1) == 98 or self.input.LA(1) == 102 or self.input.LA(1) == 110 or self.input.LA(1) == 114 or self.input.LA(1) == 116:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                elif alt15 == 2:
                    # BatchScript.g:171:63: UNICODE_ESC
                    pass 
                    self.mUNICODE_ESC()


                elif alt15 == 3:
                    # BatchScript.g:171:77: ~ ( '\\\\' | '\"' )
                    pass 
                    if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop15
            self.match(34)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STRING"



    # $ANTLR start "EXPONENT"
    def mEXPONENT(self, ):

        try:
            # BatchScript.g:175:13: ( ( 'e' | 'E' ) ( '+' | '-' )? ( DIGIT )+ )
            # BatchScript.g:175:17: ( 'e' | 'E' ) ( '+' | '-' )? ( DIGIT )+
            pass 
            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # BatchScript.g:175:27: ( '+' | '-' )?
            alt16 = 2
            LA16_0 = self.input.LA(1)

            if (LA16_0 == 43 or LA16_0 == 45) :
                alt16 = 1
            if alt16 == 1:
                # BatchScript.g:
                pass 
                if self.input.LA(1) == 43 or self.input.LA(1) == 45:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            # BatchScript.g:175:38: ( DIGIT )+
            cnt17 = 0
            while True: #loop17
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if ((48 <= LA17_0 <= 57)) :
                    alt17 = 1


                if alt17 == 1:
                    # BatchScript.g:175:38: DIGIT
                    pass 
                    self.mDIGIT()


                else:
                    if cnt17 >= 1:
                        break #loop17

                    eee = EarlyExitException(17, self.input)
                    raise eee

                cnt17 += 1




        finally:

            pass

    # $ANTLR end "EXPONENT"



    # $ANTLR start "HEX_DIGIT"
    def mHEX_DIGIT(self, ):

        try:
            # BatchScript.g:178:13: ( ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' ) )
            # BatchScript.g:178:17: ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' )
            pass 
            if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70) or (97 <= self.input.LA(1) <= 102):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "HEX_DIGIT"



    # $ANTLR start "ESC_SEQ"
    def mESC_SEQ(self, ):

        try:
            # BatchScript.g:181:13: ( | UNICODE_ESC | OCTAL_ESC )
            alt18 = 3
            LA18_0 = self.input.LA(1)

            if (LA18_0 == 92) :
                LA18_2 = self.input.LA(2)

                if (LA18_2 == 117) :
                    alt18 = 2
                elif ((48 <= LA18_2 <= 55)) :
                    alt18 = 3
                else:
                    nvae = NoViableAltException("", 18, 2, self.input)

                    raise nvae

            else:
                alt18 = 1
            if alt18 == 1:
                # BatchScript.g:182:13: 
                pass 

            elif alt18 == 2:
                # BatchScript.g:182:17: UNICODE_ESC
                pass 
                self.mUNICODE_ESC()


            elif alt18 == 3:
                # BatchScript.g:183:17: OCTAL_ESC
                pass 
                self.mOCTAL_ESC()



        finally:

            pass

    # $ANTLR end "ESC_SEQ"



    # $ANTLR start "OCTAL_ESC"
    def mOCTAL_ESC(self, ):

        try:
            # BatchScript.g:187:13: ( '\\\\' ( '0' .. '3' ) ( '0' .. '7' ) ( '0' .. '7' ) | '\\\\' ( '0' .. '7' ) ( '0' .. '7' ) | '\\\\' ( '0' .. '7' ) )
            alt19 = 3
            LA19_0 = self.input.LA(1)

            if (LA19_0 == 92) :
                LA19_1 = self.input.LA(2)

                if ((48 <= LA19_1 <= 51)) :
                    LA19_2 = self.input.LA(3)

                    if ((48 <= LA19_2 <= 55)) :
                        LA19_4 = self.input.LA(4)

                        if ((48 <= LA19_4 <= 55)) :
                            alt19 = 1
                        else:
                            alt19 = 2
                    else:
                        alt19 = 3
                elif ((52 <= LA19_1 <= 55)) :
                    LA19_3 = self.input.LA(3)

                    if ((48 <= LA19_3 <= 55)) :
                        alt19 = 2
                    else:
                        alt19 = 3
                else:
                    nvae = NoViableAltException("", 19, 1, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 19, 0, self.input)

                raise nvae

            if alt19 == 1:
                # BatchScript.g:187:17: '\\\\' ( '0' .. '3' ) ( '0' .. '7' ) ( '0' .. '7' )
                pass 
                self.match(92)
                # BatchScript.g:187:22: ( '0' .. '3' )
                # BatchScript.g:187:23: '0' .. '3'
                pass 
                self.matchRange(48, 51)



                # BatchScript.g:187:32: ( '0' .. '7' )
                # BatchScript.g:187:33: '0' .. '7'
                pass 
                self.matchRange(48, 55)



                # BatchScript.g:187:42: ( '0' .. '7' )
                # BatchScript.g:187:43: '0' .. '7'
                pass 
                self.matchRange(48, 55)





            elif alt19 == 2:
                # BatchScript.g:188:17: '\\\\' ( '0' .. '7' ) ( '0' .. '7' )
                pass 
                self.match(92)
                # BatchScript.g:188:22: ( '0' .. '7' )
                # BatchScript.g:188:23: '0' .. '7'
                pass 
                self.matchRange(48, 55)



                # BatchScript.g:188:32: ( '0' .. '7' )
                # BatchScript.g:188:33: '0' .. '7'
                pass 
                self.matchRange(48, 55)





            elif alt19 == 3:
                # BatchScript.g:189:17: '\\\\' ( '0' .. '7' )
                pass 
                self.match(92)
                # BatchScript.g:189:22: ( '0' .. '7' )
                # BatchScript.g:189:23: '0' .. '7'
                pass 
                self.matchRange(48, 55)






        finally:

            pass

    # $ANTLR end "OCTAL_ESC"



    # $ANTLR start "UNICODE_ESC"
    def mUNICODE_ESC(self, ):

        try:
            # BatchScript.g:193:13: ( '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT )
            # BatchScript.g:193:17: '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
            pass 
            self.match(92)
            self.match(117)
            self.mHEX_DIGIT()
            self.mHEX_DIGIT()
            self.mHEX_DIGIT()
            self.mHEX_DIGIT()




        finally:

            pass

    # $ANTLR end "UNICODE_ESC"



    def mTokens(self):
        # BatchScript.g:1:8: ( IF | THEN | ELSE | FOR | FUNCTION | OUTPUT | INPUT | VAR | TRUE | FALSE | IN | DATE | T__29 | T__30 | T__31 | T__32 | T__33 | T__34 | T__35 | T__36 | T__37 | T__38 | T__39 | T__40 | T__41 | T__42 | T__43 | T__44 | T__45 | T__46 | T__47 | T__48 | T__49 | ID | INT | FLOAT | COMMENT | WS | STRING )
        alt20 = 39
        alt20 = self.dfa20.predict(self.input)
        if alt20 == 1:
            # BatchScript.g:1:10: IF
            pass 
            self.mIF()


        elif alt20 == 2:
            # BatchScript.g:1:13: THEN
            pass 
            self.mTHEN()


        elif alt20 == 3:
            # BatchScript.g:1:18: ELSE
            pass 
            self.mELSE()


        elif alt20 == 4:
            # BatchScript.g:1:23: FOR
            pass 
            self.mFOR()


        elif alt20 == 5:
            # BatchScript.g:1:27: FUNCTION
            pass 
            self.mFUNCTION()


        elif alt20 == 6:
            # BatchScript.g:1:36: OUTPUT
            pass 
            self.mOUTPUT()


        elif alt20 == 7:
            # BatchScript.g:1:43: INPUT
            pass 
            self.mINPUT()


        elif alt20 == 8:
            # BatchScript.g:1:49: VAR
            pass 
            self.mVAR()


        elif alt20 == 9:
            # BatchScript.g:1:53: TRUE
            pass 
            self.mTRUE()


        elif alt20 == 10:
            # BatchScript.g:1:58: FALSE
            pass 
            self.mFALSE()


        elif alt20 == 11:
            # BatchScript.g:1:64: IN
            pass 
            self.mIN()


        elif alt20 == 12:
            # BatchScript.g:1:67: DATE
            pass 
            self.mDATE()


        elif alt20 == 13:
            # BatchScript.g:1:72: T__29
            pass 
            self.mT__29()


        elif alt20 == 14:
            # BatchScript.g:1:78: T__30
            pass 
            self.mT__30()


        elif alt20 == 15:
            # BatchScript.g:1:84: T__31
            pass 
            self.mT__31()


        elif alt20 == 16:
            # BatchScript.g:1:90: T__32
            pass 
            self.mT__32()


        elif alt20 == 17:
            # BatchScript.g:1:96: T__33
            pass 
            self.mT__33()


        elif alt20 == 18:
            # BatchScript.g:1:102: T__34
            pass 
            self.mT__34()


        elif alt20 == 19:
            # BatchScript.g:1:108: T__35
            pass 
            self.mT__35()


        elif alt20 == 20:
            # BatchScript.g:1:114: T__36
            pass 
            self.mT__36()


        elif alt20 == 21:
            # BatchScript.g:1:120: T__37
            pass 
            self.mT__37()


        elif alt20 == 22:
            # BatchScript.g:1:126: T__38
            pass 
            self.mT__38()


        elif alt20 == 23:
            # BatchScript.g:1:132: T__39
            pass 
            self.mT__39()


        elif alt20 == 24:
            # BatchScript.g:1:138: T__40
            pass 
            self.mT__40()


        elif alt20 == 25:
            # BatchScript.g:1:144: T__41
            pass 
            self.mT__41()


        elif alt20 == 26:
            # BatchScript.g:1:150: T__42
            pass 
            self.mT__42()


        elif alt20 == 27:
            # BatchScript.g:1:156: T__43
            pass 
            self.mT__43()


        elif alt20 == 28:
            # BatchScript.g:1:162: T__44
            pass 
            self.mT__44()


        elif alt20 == 29:
            # BatchScript.g:1:168: T__45
            pass 
            self.mT__45()


        elif alt20 == 30:
            # BatchScript.g:1:174: T__46
            pass 
            self.mT__46()


        elif alt20 == 31:
            # BatchScript.g:1:180: T__47
            pass 
            self.mT__47()


        elif alt20 == 32:
            # BatchScript.g:1:186: T__48
            pass 
            self.mT__48()


        elif alt20 == 33:
            # BatchScript.g:1:192: T__49
            pass 
            self.mT__49()


        elif alt20 == 34:
            # BatchScript.g:1:198: ID
            pass 
            self.mID()


        elif alt20 == 35:
            # BatchScript.g:1:201: INT
            pass 
            self.mINT()


        elif alt20 == 36:
            # BatchScript.g:1:205: FLOAT
            pass 
            self.mFLOAT()


        elif alt20 == 37:
            # BatchScript.g:1:211: COMMENT
            pass 
            self.mCOMMENT()


        elif alt20 == 38:
            # BatchScript.g:1:219: WS
            pass 
            self.mWS()


        elif alt20 == 39:
            # BatchScript.g:1:222: STRING
            pass 
            self.mSTRING()







    # lookup tables for DFA #10

    DFA10_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA10_eof = DFA.unpack(
        u"\5\uffff"
        )

    DFA10_min = DFA.unpack(
        u"\2\56\3\uffff"
        )

    DFA10_max = DFA.unpack(
        u"\1\71\1\145\3\uffff"
        )

    DFA10_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\3"
        )

    DFA10_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA10_transition = [
        DFA.unpack(u"\1\2\1\uffff\12\1"),
        DFA.unpack(u"\1\3\1\uffff\12\1\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #10

    class DFA10(DFA):
        pass


    # lookup tables for DFA #20

    DFA20_eot = DFA.unpack(
        u"\1\uffff\10\32\1\uffff\1\53\6\uffff\1\55\1\57\1\61\3\uffff\1\64"
        u"\1\uffff\1\65\1\uffff\1\67\2\uffff\1\70\1\71\12\32\20\uffff\3\32"
        u"\1\107\4\32\1\114\1\32\1\116\1\117\1\120\1\uffff\4\32\1\uffff\1"
        u"\125\3\uffff\1\32\1\127\1\32\1\131\1\uffff\1\32\1\uffff\1\133\1"
        u"\uffff\1\32\1\uffff\1\135\1\uffff"
        )

    DFA20_eof = DFA.unpack(
        u"\136\uffff"
        )

    DFA20_min = DFA.unpack(
        u"\1\11\1\146\1\150\1\154\1\141\1\125\1\116\2\141\1\uffff\1\75\6"
        u"\uffff\3\75\3\uffff\1\52\1\uffff\1\60\1\uffff\1\56\2\uffff\2\60"
        u"\1\145\1\165\1\163\1\162\1\156\1\154\1\124\1\120\1\162\1\164\20"
        u"\uffff\1\156\2\145\1\60\1\143\1\163\1\120\1\125\1\60\1\145\3\60"
        u"\1\uffff\1\164\1\145\1\125\1\124\1\uffff\1\60\3\uffff\1\151\1\60"
        u"\1\124\1\60\1\uffff\1\157\1\uffff\1\60\1\uffff\1\156\1\uffff\1"
        u"\60\1\uffff"
        )

    DFA20_max = DFA.unpack(
        u"\1\175\1\156\1\162\1\154\1\165\1\125\1\116\2\141\1\uffff\1\75\6"
        u"\uffff\3\75\3\uffff\1\57\1\uffff\1\71\1\uffff\1\145\2\uffff\2\172"
        u"\1\145\1\165\1\163\1\162\1\156\1\154\1\124\1\120\1\162\1\164\20"
        u"\uffff\1\156\2\145\1\172\1\143\1\163\1\120\1\125\1\172\1\145\3"
        u"\172\1\uffff\1\164\1\145\1\125\1\124\1\uffff\1\172\3\uffff\1\151"
        u"\1\172\1\124\1\172\1\uffff\1\157\1\uffff\1\172\1\uffff\1\156\1"
        u"\uffff\1\172\1\uffff"
        )

    DFA20_accept = DFA.unpack(
        u"\11\uffff\1\15\1\uffff\1\17\1\20\1\21\1\22\1\23\1\24\3\uffff\1"
        u"\33\1\34\1\35\1\uffff\1\40\1\uffff\1\42\1\uffff\1\46\1\47\14\uffff"
        u"\1\25\1\16\1\26\1\37\1\30\1\27\1\32\1\31\1\35\1\45\1\36\1\41\1"
        u"\44\1\43\1\1\1\13\15\uffff\1\4\4\uffff\1\10\1\uffff\1\2\1\11\1"
        u"\3\4\uffff\1\14\1\uffff\1\12\1\uffff\1\7\1\uffff\1\6\1\uffff\1"
        u"\5"
        )

    DFA20_special = DFA.unpack(
        u"\136\uffff"
        )

            
    DFA20_transition = [
        DFA.unpack(u"\2\34\2\uffff\1\34\22\uffff\1\34\1\21\1\35\3\uffff\1"
        u"\20\1\uffff\1\15\1\16\1\26\1\24\1\30\1\25\1\31\1\27\12\33\1\uffff"
        u"\1\11\1\22\1\12\1\23\2\uffff\10\32\1\6\5\32\1\5\13\32\4\uffff\1"
        u"\32\1\uffff\3\32\1\10\1\3\1\4\2\32\1\1\12\32\1\2\1\32\1\7\4\32"
        u"\1\13\1\17\1\14"),
        DFA.unpack(u"\1\36\7\uffff\1\37"),
        DFA.unpack(u"\1\40\11\uffff\1\41"),
        DFA.unpack(u"\1\42"),
        DFA.unpack(u"\1\45\15\uffff\1\43\5\uffff\1\44"),
        DFA.unpack(u"\1\46"),
        DFA.unpack(u"\1\47"),
        DFA.unpack(u"\1\50"),
        DFA.unpack(u"\1\51"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\52"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\54"),
        DFA.unpack(u"\1\56"),
        DFA.unpack(u"\1\60"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\63\4\uffff\1\63"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\uffff\12\33\13\uffff\1\66\37\uffff\1\66"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\32\7\uffff\32\32\4\uffff\1\32\1\uffff\32\32"),
        DFA.unpack(u"\12\32\7\uffff\32\32\4\uffff\1\32\1\uffff\32\32"),
        DFA.unpack(u"\1\72"),
        DFA.unpack(u"\1\73"),
        DFA.unpack(u"\1\74"),
        DFA.unpack(u"\1\75"),
        DFA.unpack(u"\1\76"),
        DFA.unpack(u"\1\77"),
        DFA.unpack(u"\1\100"),
        DFA.unpack(u"\1\101"),
        DFA.unpack(u"\1\102"),
        DFA.unpack(u"\1\103"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\104"),
        DFA.unpack(u"\1\105"),
        DFA.unpack(u"\1\106"),
        DFA.unpack(u"\12\32\7\uffff\32\32\4\uffff\1\32\1\uffff\32\32"),
        DFA.unpack(u"\1\110"),
        DFA.unpack(u"\1\111"),
        DFA.unpack(u"\1\112"),
        DFA.unpack(u"\1\113"),
        DFA.unpack(u"\12\32\7\uffff\32\32\4\uffff\1\32\1\uffff\32\32"),
        DFA.unpack(u"\1\115"),
        DFA.unpack(u"\12\32\7\uffff\32\32\4\uffff\1\32\1\uffff\32\32"),
        DFA.unpack(u"\12\32\7\uffff\32\32\4\uffff\1\32\1\uffff\32\32"),
        DFA.unpack(u"\12\32\7\uffff\32\32\4\uffff\1\32\1\uffff\32\32"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\121"),
        DFA.unpack(u"\1\122"),
        DFA.unpack(u"\1\123"),
        DFA.unpack(u"\1\124"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\32\7\uffff\32\32\4\uffff\1\32\1\uffff\32\32"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\126"),
        DFA.unpack(u"\12\32\7\uffff\32\32\4\uffff\1\32\1\uffff\32\32"),
        DFA.unpack(u"\1\130"),
        DFA.unpack(u"\12\32\7\uffff\32\32\4\uffff\1\32\1\uffff\32\32"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\132"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\32\7\uffff\32\32\4\uffff\1\32\1\uffff\32\32"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\134"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\32\7\uffff\32\32\4\uffff\1\32\1\uffff\32\32"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #20

    class DFA20(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(BatchScriptLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
