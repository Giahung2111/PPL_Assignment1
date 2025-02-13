# Generated from main/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3J")
        buf.write("\u0233\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\5\3\u0089\n\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7\u0099\n\7\3\b\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00a8\n\n")
        buf.write("\3\13\3\13\5\13\u00ac\n\13\3\f\3\f\3\f\3\f\3\f\5\f\u00b3")
        buf.write("\n\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\5\17\u00c1\n\17\3\20\3\20\3\20\3\20\3\20\5\20\u00c8")
        buf.write("\n\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\5\22\u00d2")
        buf.write("\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00dc")
        buf.write("\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\5\24\u00e9\n\24\3\25\3\25\3\25\3\25\3\25\3\26\3")
        buf.write("\26\3\26\5\26\u00f3\n\26\3\27\3\27\3\27\5\27\u00f8\n\27")
        buf.write("\3\27\3\27\5\27\u00fc\n\27\3\27\3\27\3\27\3\27\3\30\3")
        buf.write("\30\3\30\5\30\u0105\n\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\5\37\u0131\n\37\3\37\3\37\3 \3 \3 \3 ")
        buf.write("\3 \3 \7 \u013b\n \f \16 \u013e\13 \3!\3!\3!\3!\3!\3!")
        buf.write("\7!\u0146\n!\f!\16!\u0149\13!\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\7\"\u0151\n\"\f\"\16\"\u0154\13\"\3#\3#\3#\3#\3#\3#\7")
        buf.write("#\u015c\n#\f#\16#\u015f\13#\3$\3$\3$\3$\3$\3$\7$\u0167")
        buf.write("\n$\f$\16$\u016a\13$\3%\3%\3%\3%\3%\5%\u0171\n%\3&\3&")
        buf.write("\3&\3&\3&\3&\3&\3&\3&\3&\3&\7&\u017e\n&\f&\16&\u0181\13")
        buf.write("&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u018b\n\'\3(\3(")
        buf.write("\3(\3(\3(\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3*\5*\u019f")
        buf.write("\n*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\5,\u01b0")
        buf.write("\n,\3,\3,\3,\3,\3-\3-\5-\u01b8\n-\3.\3.\3.\3.\3.\5.\u01bf")
        buf.write("\n.\3/\3/\3/\5/\u01c4\n/\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\5\60\u01d1\n\60\3\60\3\60\3")
        buf.write("\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\62\5\62\u01e2\n\62\3\63\3\63\3\63\3\63\3\64\3")
        buf.write("\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\5\65\u01f1\n\65")
        buf.write("\3\66\3\66\3\66\3\66\3\66\5\66\u01f8\n\66\3\67\3\67\3")
        buf.write("\67\3\67\38\38\39\39\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;")
        buf.write("\3;\3;\3;\3;\3;\3;\3<\3<\3=\3=\3=\3=\3=\3=\3=\3=\3=\5")
        buf.write("=\u021e\n=\3>\3>\3>\3>\5>\u0224\n>\3?\3?\3?\3?\3?\3?\5")
        buf.write("?\u022c\n?\3?\3?\3?\5?\u0231\n?\3?\2\b>@BDFJ@\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write(":<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|\2\b\3\2\27\30\3\2")
        buf.write("!&\3\2\34\35\3\2\36 \4\2\35\35))\3\2\31\32\2\u023a\2~")
        buf.write("\3\2\2\2\4\u0088\3\2\2\2\6\u008a\3\2\2\2\b\u008c\3\2\2")
        buf.write("\2\n\u008f\3\2\2\2\f\u0098\3\2\2\2\16\u009a\3\2\2\2\20")
        buf.write("\u009e\3\2\2\2\22\u00a7\3\2\2\2\24\u00ab\3\2\2\2\26\u00b2")
        buf.write("\3\2\2\2\30\u00b4\3\2\2\2\32\u00b9\3\2\2\2\34\u00c0\3")
        buf.write("\2\2\2\36\u00c7\3\2\2\2 \u00c9\3\2\2\2\"\u00d1\3\2\2\2")
        buf.write("$\u00db\3\2\2\2&\u00e8\3\2\2\2(\u00ea\3\2\2\2*\u00f2\3")
        buf.write("\2\2\2,\u00fb\3\2\2\2.\u0104\3\2\2\2\60\u0106\3\2\2\2")
        buf.write("\62\u010c\3\2\2\2\64\u0116\3\2\2\2\66\u0121\3\2\2\28\u0124")
        buf.write("\3\2\2\2:\u0127\3\2\2\2<\u012d\3\2\2\2>\u0134\3\2\2\2")
        buf.write("@\u013f\3\2\2\2B\u014a\3\2\2\2D\u0155\3\2\2\2F\u0160\3")
        buf.write("\2\2\2H\u0170\3\2\2\2J\u0172\3\2\2\2L\u018a\3\2\2\2N\u018c")
        buf.write("\3\2\2\2P\u0191\3\2\2\2R\u0195\3\2\2\2T\u01a2\3\2\2\2")
        buf.write("V\u01a8\3\2\2\2X\u01b7\3\2\2\2Z\u01be\3\2\2\2\\\u01c0")
        buf.write("\3\2\2\2^\u01c5\3\2\2\2`\u01d6\3\2\2\2b\u01e1\3\2\2\2")
        buf.write("d\u01e3\3\2\2\2f\u01e7\3\2\2\2h\u01f0\3\2\2\2j\u01f7\3")
        buf.write("\2\2\2l\u01f9\3\2\2\2n\u01fd\3\2\2\2p\u01ff\3\2\2\2r\u0201")
        buf.write("\3\2\2\2t\u0205\3\2\2\2v\u0212\3\2\2\2x\u0214\3\2\2\2")
        buf.write("z\u0223\3\2\2\2|\u0225\3\2\2\2~\177\5\"\22\2\177\u0080")
        buf.write("\7\2\2\3\u0080\3\3\2\2\2\u0081\u0089\5\n\6\2\u0082\u0089")
        buf.write("\5\32\16\2\u0083\u0089\7<\2\2\u0084\u0089\7@\2\2\u0085")
        buf.write("\u0089\7A\2\2\u0086\u0089\5\6\4\2\u0087\u0089\7C\2\2\u0088")
        buf.write("\u0081\3\2\2\2\u0088\u0082\3\2\2\2\u0088\u0083\3\2\2\2")
        buf.write("\u0088\u0084\3\2\2\2\u0088\u0085\3\2\2\2\u0088\u0086\3")
        buf.write("\2\2\2\u0088\u0087\3\2\2\2\u0089\5\3\2\2\2\u008a\u008b")
        buf.write("\t\2\2\2\u008b\7\3\2\2\2\u008c\u008d\5\f\7\2\u008d\u008e")
        buf.write("\5\22\n\2\u008e\t\3\2\2\2\u008f\u0090\5\b\5\2\u0090\u0091")
        buf.write("\7\65\2\2\u0091\u0092\5\24\13\2\u0092\u0093\7\66\2\2\u0093")
        buf.write("\13\3\2\2\2\u0094\u0095\5\16\b\2\u0095\u0096\5\f\7\2\u0096")
        buf.write("\u0099\3\2\2\2\u0097\u0099\5\16\b\2\u0098\u0094\3\2\2")
        buf.write("\2\u0098\u0097\3\2\2\2\u0099\r\3\2\2\2\u009a\u009b\7\67")
        buf.write("\2\2\u009b\u009c\7<\2\2\u009c\u009d\78\2\2\u009d\17\3")
        buf.write("\2\2\2\u009e\u009f\7;\2\2\u009f\21\3\2\2\2\u00a0\u00a8")
        buf.write("\7\16\2\2\u00a1\u00a8\7\17\2\2\u00a2\u00a8\7\20\2\2\u00a3")
        buf.write("\u00a8\7\r\2\2\u00a4\u00a8\7\f\2\2\u00a5\u00a8\5\20\t")
        buf.write("\2\u00a6\u00a8\5\b\5\2\u00a7\u00a0\3\2\2\2\u00a7\u00a1")
        buf.write("\3\2\2\2\u00a7\u00a2\3\2\2\2\u00a7\u00a3\3\2\2\2\u00a7")
        buf.write("\u00a4\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a6\3\2\2\2")
        buf.write("\u00a8\23\3\2\2\2\u00a9\u00ac\5\26\f\2\u00aa\u00ac\3\2")
        buf.write("\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00aa\3\2\2\2\u00ac\25")
        buf.write("\3\2\2\2\u00ad\u00ae\5> \2\u00ae\u00af\79\2\2\u00af\u00b0")
        buf.write("\5\26\f\2\u00b0\u00b3\3\2\2\2\u00b1\u00b3\5> \2\u00b2")
        buf.write("\u00ad\3\2\2\2\u00b2\u00b1\3\2\2\2\u00b3\27\3\2\2\2\u00b4")
        buf.write("\u00b5\7;\2\2\u00b5\u00b6\7\67\2\2\u00b6\u00b7\7<\2\2")
        buf.write("\u00b7\u00b8\78\2\2\u00b8\31\3\2\2\2\u00b9\u00ba\7;\2")
        buf.write("\2\u00ba\u00bb\7\65\2\2\u00bb\u00bc\5\34\17\2\u00bc\u00bd")
        buf.write("\7\66\2\2\u00bd\33\3\2\2\2\u00be\u00c1\5\36\20\2\u00bf")
        buf.write("\u00c1\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0\u00bf\3\2\2\2")
        buf.write("\u00c1\35\3\2\2\2\u00c2\u00c3\5 \21\2\u00c3\u00c4\79\2")
        buf.write("\2\u00c4\u00c5\5\36\20\2\u00c5\u00c8\3\2\2\2\u00c6\u00c8")
        buf.write("\5 \21\2\u00c7\u00c2\3\2\2\2\u00c7\u00c6\3\2\2\2\u00c8")
        buf.write("\37\3\2\2\2\u00c9\u00ca\7;\2\2\u00ca\u00cb\7\3\2\2\u00cb")
        buf.write("\u00cc\5> \2\u00cc!\3\2\2\2\u00cd\u00ce\5$\23\2\u00ce")
        buf.write("\u00cf\5\"\22\2\u00cf\u00d2\3\2\2\2\u00d0\u00d2\5$\23")
        buf.write("\2\u00d1\u00cd\3\2\2\2\u00d1\u00d0\3\2\2\2\u00d2#\3\2")
        buf.write("\2\2\u00d3\u00dc\5&\24\2\u00d4\u00dc\5:\36\2\u00d5\u00dc")
        buf.write("\5(\25\2\u00d6\u00dc\5,\27\2\u00d7\u00dc\5.\30\2\u00d8")
        buf.write("\u00dc\5\66\34\2\u00d9\u00dc\58\35\2\u00da\u00dc\5<\37")
        buf.write("\2\u00db\u00d3\3\2\2\2\u00db\u00d4\3\2\2\2\u00db\u00d5")
        buf.write("\3\2\2\2\u00db\u00d6\3\2\2\2\u00db\u00d7\3\2\2\2\u00db")
        buf.write("\u00d8\3\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00da\3\2\2\2")
        buf.write("\u00dc%\3\2\2\2\u00dd\u00e9\5R*\2\u00de\u00e9\5T+\2\u00df")
        buf.write("\u00e9\5V,\2\u00e0\u00e9\5^\60\2\u00e1\u00e9\5`\61\2\u00e2")
        buf.write("\u00e9\5f\64\2\u00e3\u00e9\5p9\2\u00e4\u00e9\5r:\2\u00e5")
        buf.write("\u00e9\5t;\2\u00e6\u00e9\5v<\2\u00e7\u00e9\5x=\2\u00e8")
        buf.write("\u00dd\3\2\2\2\u00e8\u00de\3\2\2\2\u00e8\u00df\3\2\2\2")
        buf.write("\u00e8\u00e0\3\2\2\2\u00e8\u00e1\3\2\2\2\u00e8\u00e2\3")
        buf.write("\2\2\2\u00e8\u00e3\3\2\2\2\u00e8\u00e4\3\2\2\2\u00e8\u00e5")
        buf.write("\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e8\u00e7\3\2\2\2\u00e9")
        buf.write("\'\3\2\2\2\u00ea\u00eb\5*\26\2\u00eb\u00ec\7\62\2\2\u00ec")
        buf.write("\u00ed\5> \2\u00ed\u00ee\7:\2\2\u00ee)\3\2\2\2\u00ef\u00f3")
        buf.write("\5> \2\u00f0\u00f3\5\30\r\2\u00f1\u00f3\5p9\2\u00f2\u00ef")
        buf.write("\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3")
        buf.write("+\3\2\2\2\u00f4\u00f8\7\4\2\2\u00f5\u00f6\7\5\2\2\u00f6")
        buf.write("\u00f8\7\4\2\2\u00f7\u00f4\3\2\2\2\u00f7\u00f5\3\2\2\2")
        buf.write("\u00f8\u00f9\3\2\2\2\u00f9\u00fc\5> \2\u00fa\u00fc\7\5")
        buf.write("\2\2\u00fb\u00f7\3\2\2\2\u00fb\u00fa\3\2\2\2\u00fc\u00fd")
        buf.write("\3\2\2\2\u00fd\u00fe\7\65\2\2\u00fe\u00ff\5\"\22\2\u00ff")
        buf.write("\u0100\7\66\2\2\u0100-\3\2\2\2\u0101\u0105\5\60\31\2\u0102")
        buf.write("\u0105\5\62\32\2\u0103\u0105\5\64\33\2\u0104\u0101\3\2")
        buf.write("\2\2\u0104\u0102\3\2\2\2\u0104\u0103\3\2\2\2\u0105/\3")
        buf.write("\2\2\2\u0106\u0107\7\6\2\2\u0107\u0108\5> \2\u0108\u0109")
        buf.write("\7\65\2\2\u0109\u010a\5\"\22\2\u010a\u010b\7\66\2\2\u010b")
        buf.write("\61\3\2\2\2\u010c\u010d\7\6\2\2\u010d\u010e\5(\25\2\u010e")
        buf.write("\u010f\7:\2\2\u010f\u0110\5> \2\u0110\u0111\7:\2\2\u0111")
        buf.write("\u0112\5(\25\2\u0112\u0113\7\65\2\2\u0113\u0114\5\"\22")
        buf.write("\2\u0114\u0115\7\66\2\2\u0115\63\3\2\2\2\u0116\u0117\7")
        buf.write("\6\2\2\u0117\u0118\5> \2\u0118\u0119\79\2\2\u0119\u011a")
        buf.write("\5> \2\u011a\u011b\7/\2\2\u011b\u011c\7\25\2\2\u011c\u011d")
        buf.write("\5> \2\u011d\u011e\7\65\2\2\u011e\u011f\5\"\22\2\u011f")
        buf.write("\u0120\7\66\2\2\u0120\65\3\2\2\2\u0121\u0122\7\24\2\2")
        buf.write("\u0122\u0123\7:\2\2\u0123\67\3\2\2\2\u0124\u0125\7\23")
        buf.write("\2\2\u0125\u0126\7:\2\2\u01269\3\2\2\2\u0127\u0128\7;")
        buf.write("\2\2\u0128\u0129\7\63\2\2\u0129\u012a\5\24\13\2\u012a")
        buf.write("\u012b\7\64\2\2\u012b\u012c\7:\2\2\u012c;\3\2\2\2\u012d")
        buf.write("\u0130\7\7\2\2\u012e\u0131\5> \2\u012f\u0131\3\2\2\2\u0130")
        buf.write("\u012e\3\2\2\2\u0130\u012f\3\2\2\2\u0131\u0132\3\2\2\2")
        buf.write("\u0132\u0133\7:\2\2\u0133=\3\2\2\2\u0134\u0135\b \1\2")
        buf.write("\u0135\u0136\5@!\2\u0136\u013c\3\2\2\2\u0137\u0138\f\4")
        buf.write("\2\2\u0138\u0139\7(\2\2\u0139\u013b\5@!\2\u013a\u0137")
        buf.write("\3\2\2\2\u013b\u013e\3\2\2\2\u013c\u013a\3\2\2\2\u013c")
        buf.write("\u013d\3\2\2\2\u013d?\3\2\2\2\u013e\u013c\3\2\2\2\u013f")
        buf.write("\u0140\b!\1\2\u0140\u0141\5B\"\2\u0141\u0147\3\2\2\2\u0142")
        buf.write("\u0143\f\4\2\2\u0143\u0144\7\'\2\2\u0144\u0146\5B\"\2")
        buf.write("\u0145\u0142\3\2\2\2\u0146\u0149\3\2\2\2\u0147\u0145\3")
        buf.write("\2\2\2\u0147\u0148\3\2\2\2\u0148A\3\2\2\2\u0149\u0147")
        buf.write("\3\2\2\2\u014a\u014b\b\"\1\2\u014b\u014c\5D#\2\u014c\u0152")
        buf.write("\3\2\2\2\u014d\u014e\f\4\2\2\u014e\u014f\t\3\2\2\u014f")
        buf.write("\u0151\5D#\2\u0150\u014d\3\2\2\2\u0151\u0154\3\2\2\2\u0152")
        buf.write("\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153C\3\2\2\2\u0154")
        buf.write("\u0152\3\2\2\2\u0155\u0156\b#\1\2\u0156\u0157\5F$\2\u0157")
        buf.write("\u015d\3\2\2\2\u0158\u0159\f\4\2\2\u0159\u015a\t\4\2\2")
        buf.write("\u015a\u015c\5F$\2\u015b\u0158\3\2\2\2\u015c\u015f\3\2")
        buf.write("\2\2\u015d\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015eE\3")
        buf.write("\2\2\2\u015f\u015d\3\2\2\2\u0160\u0161\b$\1\2\u0161\u0162")
        buf.write("\5H%\2\u0162\u0168\3\2\2\2\u0163\u0164\f\4\2\2\u0164\u0165")
        buf.write("\t\5\2\2\u0165\u0167\5H%\2\u0166\u0163\3\2\2\2\u0167\u016a")
        buf.write("\3\2\2\2\u0168\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169")
        buf.write("G\3\2\2\2\u016a\u0168\3\2\2\2\u016b\u016c\5J&\2\u016c")
        buf.write("\u016d\t\6\2\2\u016d\u016e\5H%\2\u016e\u0171\3\2\2\2\u016f")
        buf.write("\u0171\5J&\2\u0170\u016b\3\2\2\2\u0170\u016f\3\2\2\2\u0171")
        buf.write("I\3\2\2\2\u0172\u0173\b&\1\2\u0173\u0174\5L\'\2\u0174")
        buf.write("\u017f\3\2\2\2\u0175\u0176\f\5\2\2\u0176\u0177\7\61\2")
        buf.write("\2\u0177\u017e\5L\'\2\u0178\u0179\f\4\2\2\u0179\u017a")
        buf.write("\7\67\2\2\u017a\u017b\5> \2\u017b\u017c\78\2\2\u017c\u017e")
        buf.write("\3\2\2\2\u017d\u0175\3\2\2\2\u017d\u0178\3\2\2\2\u017e")
        buf.write("\u0181\3\2\2\2\u017f\u017d\3\2\2\2\u017f\u0180\3\2\2\2")
        buf.write("\u0180K\3\2\2\2\u0181\u017f\3\2\2\2\u0182\u018b\7;\2\2")
        buf.write("\u0183\u018b\5\4\3\2\u0184\u018b\5N(\2\u0185\u0186\7\63")
        buf.write("\2\2\u0186\u0187\5> \2\u0187\u0188\7\64\2\2\u0188\u018b")
        buf.write("\3\2\2\2\u0189\u018b\5\30\r\2\u018a\u0182\3\2\2\2\u018a")
        buf.write("\u0183\3\2\2\2\u018a\u0184\3\2\2\2\u018a\u0185\3\2\2\2")
        buf.write("\u018a\u0189\3\2\2\2\u018bM\3\2\2\2\u018c\u018d\7;\2\2")
        buf.write("\u018d\u018e\7\63\2\2\u018e\u018f\5\24\13\2\u018f\u0190")
        buf.write("\7\64\2\2\u0190O\3\2\2\2\u0191\u0192\5> \2\u0192\u0193")
        buf.write("\7\61\2\2\u0193\u0194\5> \2\u0194Q\3\2\2\2\u0195\u0196")
        buf.write("\7\22\2\2\u0196\u019e\5> \2\u0197\u0198\5\22\n\2\u0198")
        buf.write("\u0199\7\60\2\2\u0199\u019a\5> \2\u019a\u019f\3\2\2\2")
        buf.write("\u019b\u019c\7\60\2\2\u019c\u019f\5> \2\u019d\u019f\5")
        buf.write("\22\n\2\u019e\u0197\3\2\2\2\u019e\u019b\3\2\2\2\u019e")
        buf.write("\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a1\7:\2\2")
        buf.write("\u01a1S\3\2\2\2\u01a2\u01a3\7\21\2\2\u01a3\u01a4\7;\2")
        buf.write("\2\u01a4\u01a5\7\60\2\2\u01a5\u01a6\5> \2\u01a6\u01a7")
        buf.write("\7:\2\2\u01a7U\3\2\2\2\u01a8\u01a9\7\b\2\2\u01a9\u01aa")
        buf.write("\7;\2\2\u01aa\u01ab\7\63\2\2\u01ab\u01ac\5X-\2\u01ac\u01af")
        buf.write("\7\64\2\2\u01ad\u01b0\5\22\n\2\u01ae\u01b0\3\2\2\2\u01af")
        buf.write("\u01ad\3\2\2\2\u01af\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2")
        buf.write("\u01b1\u01b2\7\65\2\2\u01b2\u01b3\5\"\22\2\u01b3\u01b4")
        buf.write("\7\66\2\2\u01b4W\3\2\2\2\u01b5\u01b8\5Z.\2\u01b6\u01b8")
        buf.write("\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b6\3\2\2\2\u01b8")
        buf.write("Y\3\2\2\2\u01b9\u01ba\5\\/\2\u01ba\u01bb\79\2\2\u01bb")
        buf.write("\u01bc\5Z.\2\u01bc\u01bf\3\2\2\2\u01bd\u01bf\5\\/\2\u01be")
        buf.write("\u01b9\3\2\2\2\u01be\u01bd\3\2\2\2\u01bf[\3\2\2\2\u01c0")
        buf.write("\u01c3\7;\2\2\u01c1\u01c4\5\22\n\2\u01c2\u01c4\3\2\2\2")
        buf.write("\u01c3\u01c1\3\2\2\2\u01c3\u01c2\3\2\2\2\u01c4]\3\2\2")
        buf.write("\2\u01c5\u01c6\7\b\2\2\u01c6\u01c7\7\63\2\2\u01c7\u01c8")
        buf.write("\5> \2\u01c8\u01c9\5> \2\u01c9\u01ca\7\64\2\2\u01ca\u01cb")
        buf.write("\5> \2\u01cb\u01cc\7\63\2\2\u01cc\u01cd\5X-\2\u01cd\u01d0")
        buf.write("\7\64\2\2\u01ce\u01d1\5\22\n\2\u01cf\u01d1\3\2\2\2\u01d0")
        buf.write("\u01ce\3\2\2\2\u01d0\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2")
        buf.write("\u01d2\u01d3\7\65\2\2\u01d3\u01d4\5\"\22\2\u01d4\u01d5")
        buf.write("\7\66\2\2\u01d5_\3\2\2\2\u01d6\u01d7\7\t\2\2\u01d7\u01d8")
        buf.write("\5> \2\u01d8\u01d9\7\n\2\2\u01d9\u01da\7\65\2\2\u01da")
        buf.write("\u01db\5b\62\2\u01db\u01dc\7\66\2\2\u01dca\3\2\2\2\u01dd")
        buf.write("\u01de\5d\63\2\u01de\u01df\5b\62\2\u01df\u01e2\3\2\2\2")
        buf.write("\u01e0\u01e2\5d\63\2\u01e1\u01dd\3\2\2\2\u01e1\u01e0\3")
        buf.write("\2\2\2\u01e2c\3\2\2\2\u01e3\u01e4\5> \2\u01e4\u01e5\5")
        buf.write("\22\n\2\u01e5\u01e6\7:\2\2\u01e6e\3\2\2\2\u01e7\u01e8")
        buf.write("\7;\2\2\u01e8\u01e9\7/\2\2\u01e9\u01ea\7;\2\2\u01ea\u01eb")
        buf.write("\7\65\2\2\u01eb\u01ec\5h\65\2\u01ec\u01ed\7\66\2\2\u01ed")
        buf.write("g\3\2\2\2\u01ee\u01f1\5j\66\2\u01ef\u01f1\3\2\2\2\u01f0")
        buf.write("\u01ee\3\2\2\2\u01f0\u01ef\3\2\2\2\u01f1i\3\2\2\2\u01f2")
        buf.write("\u01f3\5l\67\2\u01f3\u01f4\79\2\2\u01f4\u01f5\5j\66\2")
        buf.write("\u01f5\u01f8\3\2\2\2\u01f6\u01f8\5l\67\2\u01f7\u01f2\3")
        buf.write("\2\2\2\u01f7\u01f6\3\2\2\2\u01f8k\3\2\2\2\u01f9\u01fa")
        buf.write("\5> \2\u01fa\u01fb\7\3\2\2\u01fb\u01fc\5> \2\u01fcm\3")
        buf.write("\2\2\2\u01fd\u01fe\t\7\2\2\u01feo\3\2\2\2\u01ff\u0200")
        buf.write("\5> \2\u0200q\3\2\2\2\u0201\u0202\5> \2\u0202\u0203\7")
        buf.write("/\2\2\u0203\u0204\5> \2\u0204s\3\2\2\2\u0205\u0206\7\b")
        buf.write("\2\2\u0206\u0207\7\63\2\2\u0207\u0208\5> \2\u0208\u0209")
        buf.write("\5> \2\u0209\u020a\7\64\2\2\u020a\u020b\5> \2\u020b\u020c")
        buf.write("\7\63\2\2\u020c\u020d\7\64\2\2\u020d\u020e\5\22\n\2\u020e")
        buf.write("\u020f\7\65\2\2\u020f\u0210\5\"\22\2\u0210\u0211\7\66")
        buf.write("\2\2\u0211u\3\2\2\2\u0212\u0213\5> \2\u0213w\3\2\2\2\u0214")
        buf.write("\u0215\7\t\2\2\u0215\u0216\7;\2\2\u0216\u0217\7\13\2\2")
        buf.write("\u0217\u0218\7\65\2\2\u0218\u0219\5z>\2\u0219\u021d\7")
        buf.write("\66\2\2\u021a\u021e\7:\2\2\u021b\u021e\7F\2\2\u021c\u021e")
        buf.write("\3\2\2\2\u021d\u021a\3\2\2\2\u021d\u021b\3\2\2\2\u021d")
        buf.write("\u021c\3\2\2\2\u021ey\3\2\2\2\u021f\u0220\5|?\2\u0220")
        buf.write("\u0221\5z>\2\u0221\u0224\3\2\2\2\u0222\u0224\5|?\2\u0223")
        buf.write("\u021f\3\2\2\2\u0223\u0222\3\2\2\2\u0224{\3\2\2\2\u0225")
        buf.write("\u0226\7;\2\2\u0226\u0227\7\63\2\2\u0227\u0228\5X-\2\u0228")
        buf.write("\u022b\7\64\2\2\u0229\u022c\5\22\n\2\u022a\u022c\3\2\2")
        buf.write("\2\u022b\u0229\3\2\2\2\u022b\u022a\3\2\2\2\u022c\u0230")
        buf.write("\3\2\2\2\u022d\u0231\7:\2\2\u022e\u0231\7F\2\2\u022f\u0231")
        buf.write("\3\2\2\2\u0230\u022d\3\2\2\2\u0230\u022e\3\2\2\2\u0230")
        buf.write("\u022f\3\2\2\2\u0231}\3\2\2\2\'\u0088\u0098\u00a7\u00ab")
        buf.write("\u00b2\u00c0\u00c7\u00d1\u00db\u00e8\u00f2\u00f7\u00fb")
        buf.write("\u0104\u0130\u013c\u0147\u0152\u015d\u0168\u0170\u017d")
        buf.write("\u017f\u018a\u019e\u01af\u01b7\u01be\u01c3\u01d0\u01e1")
        buf.write("\u01f0\u01f7\u021d\u0223\u022b\u0230")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'str'", 
                     "'string'", "'int'", "'float'", "'boolean'", "'const'", 
                     "'var'", "'continue'", "'break'", "'range'", "<INVALID>", 
                     "'true'", "'false'", "'PutStringLn'", "'PutIntLn'", 
                     "'array'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<='", "'>='", "'<'", "'>'", "'&&'", "'||'", 
                     "'!'", "'+='", "'-='", "'*='", "'/='", "'%='", "':='", 
                     "'='", "'.'", "<INVALID>", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "IF", "ELSE", "FOR", "RETURN", 
                      "FUNC", "TYPE", "STRUCT", "INTERFACE", "STR", "STRING", 
                      "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
                      "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "PUTSTRINGLN", 
                      "PUTINTLN", "ARRAY", "PLUS", "MINUS", "MUL", "DIV", 
                      "MOD", "EQUAL", "NOTEQUAL", "LE", "GE", "LT", "GT", 
                      "AND", "OR", "NOT", "PLUSEQ", "MINUSEQ", "MULEQ", 
                      "DIVEQ", "MODEQ", "COLONEQ", "ASSIGN", "DOT", "ASSIGN_OPERATOR", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
                      "RBRACK", "COMMA", "SEMI", "ID", "DECIMAL_LIT", "BINARY_LIT", 
                      "OCT_LIT", "HEXA_LIT", "FLOAT_LIT", "STRING_LIT", 
                      "BOOLEAN_LIT", "NIL_LIT", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", 
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "VALID_ESCAPES", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_literal = 1
    RULE_bool_lit = 2
    RULE_type_array = 3
    RULE_array_lit = 4
    RULE_dimension_dec_list = 5
    RULE_dimension_dec = 6
    RULE_type_struct = 7
    RULE_typ = 8
    RULE_list_expression = 9
    RULE_list_expr = 10
    RULE_access_array_elm = 11
    RULE_struct_lit = 12
    RULE_list_elements = 13
    RULE_list_elem = 14
    RULE_element = 15
    RULE_statements_list = 16
    RULE_statement = 17
    RULE_declaration_statement = 18
    RULE_assignment_statement = 19
    RULE_lhs = 20
    RULE_if_statement = 21
    RULE_for_statement = 22
    RULE_basic_loop = 23
    RULE_ini_con_upd_loop = 24
    RULE_range_loop = 25
    RULE_break_statement = 26
    RULE_continue_statement = 27
    RULE_call_statement = 28
    RULE_return_statement = 29
    RULE_expression = 30
    RULE_expression1 = 31
    RULE_expression2 = 32
    RULE_expression3 = 33
    RULE_expression4 = 34
    RULE_expression5 = 35
    RULE_expression6 = 36
    RULE_expression7 = 37
    RULE_function_call = 38
    RULE_method_call = 39
    RULE_variables = 40
    RULE_constants = 41
    RULE_functions = 42
    RULE_paramaters_list = 43
    RULE_paramaters = 44
    RULE_paramater = 45
    RULE_methods = 46
    RULE_struct = 47
    RULE_fieldname_list = 48
    RULE_fieldname = 49
    RULE_struct_instance = 50
    RULE_valueinstance_list = 51
    RULE_valueinstance_prime = 52
    RULE_valueinstance = 53
    RULE_print_line = 54
    RULE_accessing_struct_fields = 55
    RULE_modify_fields = 56
    RULE_define_method = 57
    RULE_call_instancemethod = 58
    RULE_interface = 59
    RULE_interface_method_list = 60
    RULE_interface_method = 61

    ruleNames =  [ "program", "literal", "bool_lit", "type_array", "array_lit", 
                   "dimension_dec_list", "dimension_dec", "type_struct", 
                   "typ", "list_expression", "list_expr", "access_array_elm", 
                   "struct_lit", "list_elements", "list_elem", "element", 
                   "statements_list", "statement", "declaration_statement", 
                   "assignment_statement", "lhs", "if_statement", "for_statement", 
                   "basic_loop", "ini_con_upd_loop", "range_loop", "break_statement", 
                   "continue_statement", "call_statement", "return_statement", 
                   "expression", "expression1", "expression2", "expression3", 
                   "expression4", "expression5", "expression6", "expression7", 
                   "function_call", "method_call", "variables", "constants", 
                   "functions", "paramaters_list", "paramaters", "paramater", 
                   "methods", "struct", "fieldname_list", "fieldname", "struct_instance", 
                   "valueinstance_list", "valueinstance_prime", "valueinstance", 
                   "print_line", "accessing_struct_fields", "modify_fields", 
                   "define_method", "call_instancemethod", "interface", 
                   "interface_method_list", "interface_method" ]

    EOF = Token.EOF
    T__0=1
    IF=2
    ELSE=3
    FOR=4
    RETURN=5
    FUNC=6
    TYPE=7
    STRUCT=8
    INTERFACE=9
    STR=10
    STRING=11
    INT=12
    FLOAT=13
    BOOLEAN=14
    CONST=15
    VAR=16
    CONTINUE=17
    BREAK=18
    RANGE=19
    NIL=20
    TRUE=21
    FALSE=22
    PUTSTRINGLN=23
    PUTINTLN=24
    ARRAY=25
    PLUS=26
    MINUS=27
    MUL=28
    DIV=29
    MOD=30
    EQUAL=31
    NOTEQUAL=32
    LE=33
    GE=34
    LT=35
    GT=36
    AND=37
    OR=38
    NOT=39
    PLUSEQ=40
    MINUSEQ=41
    MULEQ=42
    DIVEQ=43
    MODEQ=44
    COLONEQ=45
    ASSIGN=46
    DOT=47
    ASSIGN_OPERATOR=48
    LPAREN=49
    RPAREN=50
    LBRACE=51
    RBRACE=52
    LBRACK=53
    RBRACK=54
    COMMA=55
    SEMI=56
    ID=57
    DECIMAL_LIT=58
    BINARY_LIT=59
    OCT_LIT=60
    HEXA_LIT=61
    FLOAT_LIT=62
    STRING_LIT=63
    BOOLEAN_LIT=64
    NIL_LIT=65
    SINGLE_LINE_COMMENT=66
    MULTI_LINE_COMMENT=67
    WS=68
    ERROR_CHAR=69
    UNCLOSE_STRING=70
    VALID_ESCAPES=71
    ILLEGAL_ESCAPE=72

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements_list(self):
            return self.getTypedRuleContext(MiniGoParser.Statements_listContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.statements_list()
            self.state = 125
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Array_litContext,0)


        def struct_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_litContext,0)


        def DECIMAL_LIT(self):
            return self.getToken(MiniGoParser.DECIMAL_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def bool_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Bool_litContext,0)


        def NIL_LIT(self):
            return self.getToken(MiniGoParser.NIL_LIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_literal)
        try:
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.array_lit()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.struct_lit()
                pass
            elif token in [MiniGoParser.DECIMAL_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.match(MiniGoParser.DECIMAL_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 130
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 131
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 132
                self.bool_lit()
                pass
            elif token in [MiniGoParser.NIL_LIT]:
                self.enterOuterAlt(localctx, 7)
                self.state = 133
                self.match(MiniGoParser.NIL_LIT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_bool_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_lit" ):
                return visitor.visitBool_lit(self)
            else:
                return visitor.visitChildren(self)




    def bool_lit(self):

        localctx = MiniGoParser.Bool_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bool_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.TRUE or _la==MiniGoParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension_dec_list(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_dec_listContext,0)


        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_array" ):
                return visitor.visitType_array(self)
            else:
                return visitor.visitChildren(self)




    def type_array(self):

        localctx = MiniGoParser.Type_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.dimension_dec_list()
            self.state = 139
            self.typ()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_array(self):
            return self.getTypedRuleContext(MiniGoParser.Type_arrayContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = MiniGoParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.type_array()
            self.state = 142
            self.match(MiniGoParser.LBRACE)
            self.state = 143
            self.list_expression()
            self.state = 144
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimension_dec_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension_dec(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_decContext,0)


        def dimension_dec_list(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_dec_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_dimension_dec_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension_dec_list" ):
                return visitor.visitDimension_dec_list(self)
            else:
                return visitor.visitChildren(self)




    def dimension_dec_list(self):

        localctx = MiniGoParser.Dimension_dec_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_dimension_dec_list)
        try:
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.dimension_dec()
                self.state = 147
                self.dimension_dec_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.dimension_dec()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimension_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def DECIMAL_LIT(self):
            return self.getToken(MiniGoParser.DECIMAL_LIT, 0)

        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dimension_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension_dec" ):
                return visitor.visitDimension_dec(self)
            else:
                return visitor.visitChildren(self)




    def dimension_dec(self):

        localctx = MiniGoParser.Dimension_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_dimension_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(MiniGoParser.LBRACK)
            self.state = 153
            self.match(MiniGoParser.DECIMAL_LIT)
            self.state = 154
            self.match(MiniGoParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_structContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_type_struct

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_struct" ):
                return visitor.visitType_struct(self)
            else:
                return visitor.visitChildren(self)




    def type_struct(self):

        localctx = MiniGoParser.Type_structContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_type_struct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def STR(self):
            return self.getToken(MiniGoParser.STR, 0)

        def type_struct(self):
            return self.getTypedRuleContext(MiniGoParser.Type_structContext,0)


        def type_array(self):
            return self.getTypedRuleContext(MiniGoParser.Type_arrayContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = MiniGoParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_typ)
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 160
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 161
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.STR]:
                self.enterOuterAlt(localctx, 5)
                self.state = 162
                self.match(MiniGoParser.STR)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 163
                self.type_struct()
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 7)
                self.state = 164
                self.type_array()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expression" ):
                return visitor.visitList_expression(self)
            else:
                return visitor.visitChildren(self)




    def list_expression(self):

        localctx = MiniGoParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_list_expression)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.ID, MiniGoParser.DECIMAL_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.NIL_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.list_expr()
                pass
            elif token in [MiniGoParser.RPAREN, MiniGoParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr" ):
                return visitor.visitList_expr(self)
            else:
                return visitor.visitChildren(self)




    def list_expr(self):

        localctx = MiniGoParser.List_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_list_expr)
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.expression(0)
                self.state = 172
                self.match(MiniGoParser.COMMA)
                self.state = 173
                self.list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Access_array_elmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def DECIMAL_LIT(self):
            return self.getToken(MiniGoParser.DECIMAL_LIT, 0)

        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_access_array_elm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccess_array_elm" ):
                return visitor.visitAccess_array_elm(self)
            else:
                return visitor.visitChildren(self)




    def access_array_elm(self):

        localctx = MiniGoParser.Access_array_elmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_access_array_elm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(MiniGoParser.ID)
            self.state = 179
            self.match(MiniGoParser.LBRACK)
            self.state = 180
            self.match(MiniGoParser.DECIMAL_LIT)
            self.state = 181
            self.match(MiniGoParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_elements(self):
            return self.getTypedRuleContext(MiniGoParser.List_elementsContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_lit" ):
                return visitor.visitStruct_lit(self)
            else:
                return visitor.visitChildren(self)




    def struct_lit(self):

        localctx = MiniGoParser.Struct_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_struct_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(MiniGoParser.ID)
            self.state = 184
            self.match(MiniGoParser.LBRACE)
            self.state = 185
            self.list_elements()
            self.state = 186
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_elementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_elem(self):
            return self.getTypedRuleContext(MiniGoParser.List_elemContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_elements" ):
                return visitor.visitList_elements(self)
            else:
                return visitor.visitChildren(self)




    def list_elements(self):

        localctx = MiniGoParser.List_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_list_elements)
        try:
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.list_elem()
                pass
            elif token in [MiniGoParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_elemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(MiniGoParser.ElementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_elem(self):
            return self.getTypedRuleContext(MiniGoParser.List_elemContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_elem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_elem" ):
                return visitor.visitList_elem(self)
            else:
                return visitor.visitChildren(self)




    def list_elem(self):

        localctx = MiniGoParser.List_elemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_list_elem)
        try:
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.element()
                self.state = 193
                self.match(MiniGoParser.COMMA)
                self.state = 194
                self.list_elem()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = MiniGoParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(MiniGoParser.ID)
            self.state = 200
            self.match(MiniGoParser.T__0)
            self.state = 201
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statements_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def statements_list(self):
            return self.getTypedRuleContext(MiniGoParser.Statements_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statements_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements_list" ):
                return visitor.visitStatements_list(self)
            else:
                return visitor.visitChildren(self)




    def statements_list(self):

        localctx = MiniGoParser.Statements_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_statements_list)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.statement()
                self.state = 204
                self.statements_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Declaration_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Call_statementContext,0)


        def assignment_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MiniGoParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Return_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_statement)
        try:
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.declaration_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.call_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 211
                self.assignment_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 212
                self.if_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 213
                self.for_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 214
                self.break_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 215
                self.continue_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 216
                self.return_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables(self):
            return self.getTypedRuleContext(MiniGoParser.VariablesContext,0)


        def constants(self):
            return self.getTypedRuleContext(MiniGoParser.ConstantsContext,0)


        def functions(self):
            return self.getTypedRuleContext(MiniGoParser.FunctionsContext,0)


        def methods(self):
            return self.getTypedRuleContext(MiniGoParser.MethodsContext,0)


        def struct(self):
            return self.getTypedRuleContext(MiniGoParser.StructContext,0)


        def struct_instance(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_instanceContext,0)


        def accessing_struct_fields(self):
            return self.getTypedRuleContext(MiniGoParser.Accessing_struct_fieldsContext,0)


        def modify_fields(self):
            return self.getTypedRuleContext(MiniGoParser.Modify_fieldsContext,0)


        def define_method(self):
            return self.getTypedRuleContext(MiniGoParser.Define_methodContext,0)


        def call_instancemethod(self):
            return self.getTypedRuleContext(MiniGoParser.Call_instancemethodContext,0)


        def interface(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declaration_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_statement" ):
                return visitor.visitDeclaration_statement(self)
            else:
                return visitor.visitChildren(self)




    def declaration_statement(self):

        localctx = MiniGoParser.Declaration_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_declaration_statement)
        try:
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.variables()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.constants()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
                self.functions()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 222
                self.methods()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 223
                self.struct()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 224
                self.struct_instance()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 225
                self.accessing_struct_fields()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 226
                self.modify_fields()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 227
                self.define_method()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 228
                self.call_instancemethod()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 229
                self.interface()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def ASSIGN_OPERATOR(self):
            return self.getToken(MiniGoParser.ASSIGN_OPERATOR, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = MiniGoParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.lhs()
            self.state = 233
            self.match(MiniGoParser.ASSIGN_OPERATOR)
            self.state = 234
            self.expression(0)
            self.state = 235
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def access_array_elm(self):
            return self.getTypedRuleContext(MiniGoParser.Access_array_elmContext,0)


        def accessing_struct_fields(self):
            return self.getTypedRuleContext(MiniGoParser.Accessing_struct_fieldsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_lhs)
        try:
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.access_array_elm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 239
                self.accessing_struct_fields()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def statements_list(self):
            return self.getTypedRuleContext(MiniGoParser.Statements_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MiniGoParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 245
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.IF]:
                    self.state = 242
                    self.match(MiniGoParser.IF)
                    pass
                elif token in [MiniGoParser.ELSE]:
                    self.state = 243
                    self.match(MiniGoParser.ELSE)
                    self.state = 244
                    self.match(MiniGoParser.IF)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 247
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 248
                self.match(MiniGoParser.ELSE)
                pass


            self.state = 251
            self.match(MiniGoParser.LBRACE)
            self.state = 252
            self.statements_list()
            self.state = 253
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Basic_loopContext,0)


        def ini_con_upd_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Ini_con_upd_loopContext,0)


        def range_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Range_loopContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = MiniGoParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_for_statement)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.basic_loop()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.ini_con_upd_loop()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 257
                self.range_loop()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def statements_list(self):
            return self.getTypedRuleContext(MiniGoParser.Statements_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_basic_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_loop" ):
                return visitor.visitBasic_loop(self)
            else:
                return visitor.visitChildren(self)




    def basic_loop(self):

        localctx = MiniGoParser.Basic_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_basic_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(MiniGoParser.FOR)
            self.state = 261
            self.expression(0)
            self.state = 262
            self.match(MiniGoParser.LBRACE)
            self.state = 263
            self.statements_list()
            self.state = 264
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ini_con_upd_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def assignment_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Assignment_statementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Assignment_statementContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def statements_list(self):
            return self.getTypedRuleContext(MiniGoParser.Statements_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ini_con_upd_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIni_con_upd_loop" ):
                return visitor.visitIni_con_upd_loop(self)
            else:
                return visitor.visitChildren(self)




    def ini_con_upd_loop(self):

        localctx = MiniGoParser.Ini_con_upd_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_ini_con_upd_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(MiniGoParser.FOR)
            self.state = 267
            self.assignment_statement()
            self.state = 268
            self.match(MiniGoParser.SEMI)
            self.state = 269
            self.expression(0)
            self.state = 270
            self.match(MiniGoParser.SEMI)
            self.state = 271
            self.assignment_statement()
            self.state = 272
            self.match(MiniGoParser.LBRACE)
            self.state = 273
            self.statements_list()
            self.state = 274
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def COLONEQ(self):
            return self.getToken(MiniGoParser.COLONEQ, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def statements_list(self):
            return self.getTypedRuleContext(MiniGoParser.Statements_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_range_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_loop" ):
                return visitor.visitRange_loop(self)
            else:
                return visitor.visitChildren(self)




    def range_loop(self):

        localctx = MiniGoParser.Range_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_range_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(MiniGoParser.FOR)
            self.state = 277
            self.expression(0)
            self.state = 278
            self.match(MiniGoParser.COMMA)
            self.state = 279
            self.expression(0)
            self.state = 280
            self.match(MiniGoParser.COLONEQ)
            self.state = 281
            self.match(MiniGoParser.RANGE)
            self.state = 282
            self.expression(0)
            self.state = 283
            self.match(MiniGoParser.LBRACE)
            self.state = 284
            self.statements_list()
            self.state = 285
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = MiniGoParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(MiniGoParser.BREAK)
            self.state = 288
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = MiniGoParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(MiniGoParser.CONTINUE)
            self.state = 291
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = MiniGoParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(MiniGoParser.ID)
            self.state = 294
            self.match(MiniGoParser.LPAREN)
            self.state = 295
            self.list_expression()
            self.state = 296
            self.match(MiniGoParser.RPAREN)
            self.state = 297
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = MiniGoParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(MiniGoParser.RETURN)
            self.state = 302
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.ID, MiniGoParser.DECIMAL_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.NIL_LIT]:
                self.state = 300
                self.expression(0)
                pass
            elif token in [MiniGoParser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 304
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 314
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 309
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 310
                    self.match(MiniGoParser.OR)
                    self.state = 311
                    self.expression1(0) 
                self.state = 316
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)



    def expression1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 325
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 320
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 321
                    self.match(MiniGoParser.AND)
                    self.state = 322
                    self.expression2(0) 
                self.state = 327
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(MiniGoParser.NOTEQUAL, 0)

        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LE(self):
            return self.getToken(MiniGoParser.LE, 0)

        def GT(self):
            return self.getToken(MiniGoParser.GT, 0)

        def GE(self):
            return self.getToken(MiniGoParser.GE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 336
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 331
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 332
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.NOTEQUAL) | (1 << MiniGoParser.LE) | (1 << MiniGoParser.GE) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.GT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 333
                    self.expression3(0) 
                self.state = 338
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def PLUS(self):
            return self.getToken(MiniGoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 347
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 342
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 343
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 344
                    self.expression4(0) 
                self.state = 349
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 358
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 353
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 354
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 355
                    self.expression5() 
                self.state = 360
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = MiniGoParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expression5)
        self._la = 0 # Token type
        try:
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.expression6(0)
                self.state = 362
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 363
                self.expression5()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
                self.expression6(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7(self):
            return self.getTypedRuleContext(MiniGoParser.Expression7Context,0)


        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)



    def expression6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_expression6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.expression7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 381
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 379
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 371
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 372
                        self.match(MiniGoParser.DOT)
                        self.state = 373
                        self.expression7()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 374
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 375
                        self.match(MiniGoParser.LBRACK)
                        self.state = 376
                        self.expression(0)
                        self.state = 377
                        self.match(MiniGoParser.RBRACK)
                        pass

             
                self.state = 383
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Function_callContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def access_array_elm(self):
            return self.getTypedRuleContext(MiniGoParser.Access_array_elmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




    def expression7(self):

        localctx = MiniGoParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expression7)
        try:
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 386
                self.function_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 387
                self.match(MiniGoParser.LPAREN)
                self.state = 388
                self.expression(0)
                self.state = 389
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 391
                self.access_array_elm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = MiniGoParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.match(MiniGoParser.ID)
            self.state = 395
            self.match(MiniGoParser.LPAREN)
            self.state = 396
            self.list_expression()
            self.state = 397
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_method_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_call" ):
                return visitor.visitMethod_call(self)
            else:
                return visitor.visitChildren(self)




    def method_call(self):

        localctx = MiniGoParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_method_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.expression(0)
            self.state = 400
            self.match(MiniGoParser.DOT)
            self.state = 401
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_variables

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables" ):
                return visitor.visitVariables(self)
            else:
                return visitor.visitChildren(self)




    def variables(self):

        localctx = MiniGoParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_variables)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(MiniGoParser.VAR)
            self.state = 404
            self.expression(0)
            self.state = 412
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 405
                self.typ()
                self.state = 406
                self.match(MiniGoParser.ASSIGN)
                self.state = 407
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 409
                self.match(MiniGoParser.ASSIGN)
                self.state = 410
                self.expression(0)
                pass

            elif la_ == 3:
                self.state = 411
                self.typ()
                pass


            self.state = 414
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_constants

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstants" ):
                return visitor.visitConstants(self)
            else:
                return visitor.visitChildren(self)




    def constants(self):

        localctx = MiniGoParser.ConstantsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_constants)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(MiniGoParser.CONST)
            self.state = 417
            self.match(MiniGoParser.ID)
            self.state = 418
            self.match(MiniGoParser.ASSIGN)
            self.state = 419
            self.expression(0)
            self.state = 420
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def paramaters_list(self):
            return self.getTypedRuleContext(MiniGoParser.Paramaters_listContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def statements_list(self):
            return self.getTypedRuleContext(MiniGoParser.Statements_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_functions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctions" ):
                return visitor.visitFunctions(self)
            else:
                return visitor.visitChildren(self)




    def functions(self):

        localctx = MiniGoParser.FunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_functions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(MiniGoParser.FUNC)
            self.state = 423
            self.match(MiniGoParser.ID)
            self.state = 424
            self.match(MiniGoParser.LPAREN)
            self.state = 425
            self.paramaters_list()
            self.state = 426
            self.match(MiniGoParser.RPAREN)
            self.state = 429
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STR, MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACK, MiniGoParser.ID]:
                self.state = 427
                self.typ()
                pass
            elif token in [MiniGoParser.LBRACE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 431
            self.match(MiniGoParser.LBRACE)
            self.state = 432
            self.statements_list()
            self.state = 433
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Paramaters_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramaters(self):
            return self.getTypedRuleContext(MiniGoParser.ParamatersContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramaters_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamaters_list" ):
                return visitor.visitParamaters_list(self)
            else:
                return visitor.visitChildren(self)




    def paramaters_list(self):

        localctx = MiniGoParser.Paramaters_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_paramaters_list)
        try:
            self.state = 437
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.paramaters()
                pass
            elif token in [MiniGoParser.RPAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamatersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramater(self):
            return self.getTypedRuleContext(MiniGoParser.ParamaterContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def paramaters(self):
            return self.getTypedRuleContext(MiniGoParser.ParamatersContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramaters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamaters" ):
                return visitor.visitParamaters(self)
            else:
                return visitor.visitChildren(self)




    def paramaters(self):

        localctx = MiniGoParser.ParamatersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_paramaters)
        try:
            self.state = 444
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 439
                self.paramater()
                self.state = 440
                self.match(MiniGoParser.COMMA)
                self.state = 441
                self.paramaters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 443
                self.paramater()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamaterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramater

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamater" ):
                return visitor.visitParamater(self)
            else:
                return visitor.visitChildren(self)




    def paramater(self):

        localctx = MiniGoParser.ParamaterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_paramater)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.match(MiniGoParser.ID)
            self.state = 449
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STR, MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACK, MiniGoParser.ID]:
                self.state = 447
                self.typ()
                pass
            elif token in [MiniGoParser.RPAREN, MiniGoParser.COMMA]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LPAREN)
            else:
                return self.getToken(MiniGoParser.LPAREN, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RPAREN)
            else:
                return self.getToken(MiniGoParser.RPAREN, i)

        def paramaters_list(self):
            return self.getTypedRuleContext(MiniGoParser.Paramaters_listContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def statements_list(self):
            return self.getTypedRuleContext(MiniGoParser.Statements_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methods

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethods" ):
                return visitor.visitMethods(self)
            else:
                return visitor.visitChildren(self)




    def methods(self):

        localctx = MiniGoParser.MethodsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_methods)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(MiniGoParser.FUNC)
            self.state = 452
            self.match(MiniGoParser.LPAREN)
            self.state = 453
            self.expression(0)
            self.state = 454
            self.expression(0)
            self.state = 455
            self.match(MiniGoParser.RPAREN)
            self.state = 456
            self.expression(0)
            self.state = 457
            self.match(MiniGoParser.LPAREN)
            self.state = 458
            self.paramaters_list()
            self.state = 459
            self.match(MiniGoParser.RPAREN)
            self.state = 462
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STR, MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACK, MiniGoParser.ID]:
                self.state = 460
                self.typ()
                pass
            elif token in [MiniGoParser.LBRACE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 464
            self.match(MiniGoParser.LBRACE)
            self.state = 465
            self.statements_list()
            self.state = 466
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def fieldname_list(self):
            return self.getTypedRuleContext(MiniGoParser.Fieldname_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct" ):
                return visitor.visitStruct(self)
            else:
                return visitor.visitChildren(self)




    def struct(self):

        localctx = MiniGoParser.StructContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_struct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.match(MiniGoParser.TYPE)
            self.state = 469
            self.expression(0)
            self.state = 470
            self.match(MiniGoParser.STRUCT)
            self.state = 471
            self.match(MiniGoParser.LBRACE)
            self.state = 472
            self.fieldname_list()
            self.state = 473
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fieldname_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldname(self):
            return self.getTypedRuleContext(MiniGoParser.FieldnameContext,0)


        def fieldname_list(self):
            return self.getTypedRuleContext(MiniGoParser.Fieldname_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldname_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldname_list" ):
                return visitor.visitFieldname_list(self)
            else:
                return visitor.visitChildren(self)




    def fieldname_list(self):

        localctx = MiniGoParser.Fieldname_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_fieldname_list)
        try:
            self.state = 479
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 475
                self.fieldname()
                self.state = 476
                self.fieldname_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 478
                self.fieldname()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldname

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldname" ):
                return visitor.visitFieldname(self)
            else:
                return visitor.visitChildren(self)




    def fieldname(self):

        localctx = MiniGoParser.FieldnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_fieldname)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self.expression(0)
            self.state = 482
            self.typ()
            self.state = 483
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_instanceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COLONEQ(self):
            return self.getToken(MiniGoParser.COLONEQ, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def valueinstance_list(self):
            return self.getTypedRuleContext(MiniGoParser.Valueinstance_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_instance

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_instance" ):
                return visitor.visitStruct_instance(self)
            else:
                return visitor.visitChildren(self)




    def struct_instance(self):

        localctx = MiniGoParser.Struct_instanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_struct_instance)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.match(MiniGoParser.ID)
            self.state = 486
            self.match(MiniGoParser.COLONEQ)
            self.state = 487
            self.match(MiniGoParser.ID)
            self.state = 488
            self.match(MiniGoParser.LBRACE)
            self.state = 489
            self.valueinstance_list()
            self.state = 490
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Valueinstance_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def valueinstance_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Valueinstance_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_valueinstance_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValueinstance_list" ):
                return visitor.visitValueinstance_list(self)
            else:
                return visitor.visitChildren(self)




    def valueinstance_list(self):

        localctx = MiniGoParser.Valueinstance_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_valueinstance_list)
        try:
            self.state = 494
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.ID, MiniGoParser.DECIMAL_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.NIL_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 492
                self.valueinstance_prime()
                pass
            elif token in [MiniGoParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Valueinstance_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def valueinstance(self):
            return self.getTypedRuleContext(MiniGoParser.ValueinstanceContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def valueinstance_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Valueinstance_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_valueinstance_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValueinstance_prime" ):
                return visitor.visitValueinstance_prime(self)
            else:
                return visitor.visitChildren(self)




    def valueinstance_prime(self):

        localctx = MiniGoParser.Valueinstance_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_valueinstance_prime)
        try:
            self.state = 501
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 496
                self.valueinstance()
                self.state = 497
                self.match(MiniGoParser.COMMA)
                self.state = 498
                self.valueinstance_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 500
                self.valueinstance()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueinstanceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_valueinstance

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValueinstance" ):
                return visitor.visitValueinstance(self)
            else:
                return visitor.visitChildren(self)




    def valueinstance(self):

        localctx = MiniGoParser.ValueinstanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_valueinstance)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.expression(0)
            self.state = 504
            self.match(MiniGoParser.T__0)
            self.state = 505
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_lineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUTINTLN(self):
            return self.getToken(MiniGoParser.PUTINTLN, 0)

        def PUTSTRINGLN(self):
            return self.getToken(MiniGoParser.PUTSTRINGLN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_print_line

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_line" ):
                return visitor.visitPrint_line(self)
            else:
                return visitor.visitChildren(self)




    def print_line(self):

        localctx = MiniGoParser.Print_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_print_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.PUTSTRINGLN or _la==MiniGoParser.PUTINTLN):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Accessing_struct_fieldsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_accessing_struct_fields

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccessing_struct_fields" ):
                return visitor.visitAccessing_struct_fields(self)
            else:
                return visitor.visitChildren(self)




    def accessing_struct_fields(self):

        localctx = MiniGoParser.Accessing_struct_fieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_accessing_struct_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 509
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Modify_fieldsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def COLONEQ(self):
            return self.getToken(MiniGoParser.COLONEQ, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_modify_fields

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModify_fields" ):
                return visitor.visitModify_fields(self)
            else:
                return visitor.visitChildren(self)




    def modify_fields(self):

        localctx = MiniGoParser.Modify_fieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_modify_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            self.expression(0)
            self.state = 512
            self.match(MiniGoParser.COLONEQ)
            self.state = 513
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Define_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LPAREN)
            else:
                return self.getToken(MiniGoParser.LPAREN, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RPAREN)
            else:
                return self.getToken(MiniGoParser.RPAREN, i)

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def statements_list(self):
            return self.getTypedRuleContext(MiniGoParser.Statements_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_define_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefine_method" ):
                return visitor.visitDefine_method(self)
            else:
                return visitor.visitChildren(self)




    def define_method(self):

        localctx = MiniGoParser.Define_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_define_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.match(MiniGoParser.FUNC)
            self.state = 516
            self.match(MiniGoParser.LPAREN)
            self.state = 517
            self.expression(0)
            self.state = 518
            self.expression(0)
            self.state = 519
            self.match(MiniGoParser.RPAREN)
            self.state = 520
            self.expression(0)
            self.state = 521
            self.match(MiniGoParser.LPAREN)
            self.state = 522
            self.match(MiniGoParser.RPAREN)
            self.state = 523
            self.typ()
            self.state = 524
            self.match(MiniGoParser.LBRACE)
            self.state = 525
            self.statements_list()
            self.state = 526
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_instancemethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_instancemethod

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_instancemethod" ):
                return visitor.visitCall_instancemethod(self)
            else:
                return visitor.visitChildren(self)




    def call_instancemethod(self):

        localctx = MiniGoParser.Call_instancemethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_call_instancemethod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def interface_method_list(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def WS(self):
            return self.getToken(MiniGoParser.WS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface" ):
                return visitor.visitInterface(self)
            else:
                return visitor.visitChildren(self)




    def interface(self):

        localctx = MiniGoParser.InterfaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_interface)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self.match(MiniGoParser.TYPE)
            self.state = 531
            self.match(MiniGoParser.ID)
            self.state = 532
            self.match(MiniGoParser.INTERFACE)
            self.state = 533
            self.match(MiniGoParser.LBRACE)
            self.state = 534
            self.interface_method_list()
            self.state = 535
            self.match(MiniGoParser.RBRACE)
            self.state = 539
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SEMI]:
                self.state = 536
                self.match(MiniGoParser.SEMI)
                pass
            elif token in [MiniGoParser.WS]:
                self.state = 537
                self.match(MiniGoParser.WS)
                pass
            elif token in [MiniGoParser.EOF, MiniGoParser.IF, MiniGoParser.ELSE, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LPAREN, MiniGoParser.RBRACE, MiniGoParser.LBRACK, MiniGoParser.ID, MiniGoParser.DECIMAL_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.NIL_LIT]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_method_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_method(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_methodContext,0)


        def interface_method_list(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method_list" ):
                return visitor.visitInterface_method_list(self)
            else:
                return visitor.visitChildren(self)




    def interface_method_list(self):

        localctx = MiniGoParser.Interface_method_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_interface_method_list)
        try:
            self.state = 545
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 541
                self.interface_method()
                self.state = 542
                self.interface_method_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 544
                self.interface_method()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def paramaters_list(self):
            return self.getTypedRuleContext(MiniGoParser.Paramaters_listContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def WS(self):
            return self.getToken(MiniGoParser.WS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method" ):
                return visitor.visitInterface_method(self)
            else:
                return visitor.visitChildren(self)




    def interface_method(self):

        localctx = MiniGoParser.Interface_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_interface_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self.match(MiniGoParser.ID)
            self.state = 548
            self.match(MiniGoParser.LPAREN)
            self.state = 549
            self.paramaters_list()
            self.state = 550
            self.match(MiniGoParser.RPAREN)
            self.state = 553
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 551
                self.typ()
                pass

            elif la_ == 2:
                pass


            self.state = 558
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SEMI]:
                self.state = 555
                self.match(MiniGoParser.SEMI)
                pass
            elif token in [MiniGoParser.WS]:
                self.state = 556
                self.match(MiniGoParser.WS)
                pass
            elif token in [MiniGoParser.RBRACE, MiniGoParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[30] = self.expression_sempred
        self._predicates[31] = self.expression1_sempred
        self._predicates[32] = self.expression2_sempred
        self._predicates[33] = self.expression3_sempred
        self._predicates[34] = self.expression4_sempred
        self._predicates[36] = self.expression6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression1_sempred(self, localctx:Expression1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expression6_sempred(self, localctx:Expression6Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




