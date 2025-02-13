# Generated from main/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2J")
        buf.write("\u024f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3&\3&\3&\3")
        buf.write("\'\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3")
        buf.write("-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\5\61\u0172\n\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\7:\u0186")
        buf.write("\n:\f:\16:\u0189\13:\3;\3;\5;\u018d\n;\3;\3;\3;\7;\u0192")
        buf.write("\n;\f;\16;\u0195\13;\5;\u0197\n;\3<\3<\3<\6<\u019c\n<")
        buf.write("\r<\16<\u019d\3<\3<\3=\3=\3=\6=\u01a5\n=\r=\16=\u01a6")
        buf.write("\3=\3=\3>\3>\3>\6>\u01ae\n>\r>\16>\u01af\3>\3>\3?\3?\3")
        buf.write("@\3@\3A\3A\3B\3B\5B\u01bc\nB\3B\3B\3B\7B\u01c1\nB\fB\16")
        buf.write("B\u01c4\13B\5B\u01c6\nB\3C\3C\3C\7C\u01cb\nC\fC\16C\u01ce")
        buf.write("\13C\3C\5C\u01d1\nC\3C\3C\6C\u01d5\nC\rC\16C\u01d6\3C")
        buf.write("\5C\u01da\nC\3C\6C\u01dd\nC\rC\16C\u01de\3C\5C\u01e2\n")
        buf.write("C\3D\3D\3D\7D\u01e7\nD\fD\16D\u01ea\13D\5D\u01ec\nD\3")
        buf.write("E\3E\3E\3E\3E\3E\7E\u01f4\nE\fE\16E\u01f7\13E\3E\3E\3")
        buf.write("E\3F\3F\3F\3F\3F\3F\3F\3F\3F\5F\u0205\nF\3G\3G\3G\3G\3")
        buf.write("H\3H\3H\3H\7H\u020f\nH\fH\16H\u0212\13H\3H\3H\3I\3I\3")
        buf.write("I\3I\3I\7I\u021b\nI\fI\16I\u021e\13I\3I\3I\3I\3I\3I\3")
        buf.write("J\6J\u0226\nJ\rJ\16J\u0227\3J\3J\3K\3K\3K\3L\3L\3L\3L")
        buf.write("\3L\3L\7L\u0235\nL\fL\16L\u0238\13L\3L\5L\u023b\nL\3L")
        buf.write("\3L\3M\3M\3N\3N\3N\3N\3N\3N\7N\u0247\nN\fN\16N\u024a\13")
        buf.write("N\3N\3N\3N\3N\3\u021c\2O\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o9q:s;u<w=y>{?}\2\177\2\u0081\2\u0083")
        buf.write("\2\u0085@\u0087\2\u0089A\u008bB\u008dC\u008fD\u0091E\u0093")
        buf.write("F\u0095G\u0097H\u0099I\u009bJ\3\2\24\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\3\2\63;\3\2\62;\4\2DDdd\4\2QQqq\4\2ZZzz\5\2\62")
        buf.write(";CHch\3\2\629\3\2\62\63\4\2GGgg\4\2--//\5\2\f\f$$^^\7")
        buf.write("\2$$^^ppttvv\4\2\f\f\17\17\5\2\13\f\16\17\"\"\3\3\f\f")
        buf.write("\7\2))^^ppttvv\2\u026f\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2\u0085\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\3\u009d\3\2\2")
        buf.write("\2\5\u009f\3\2\2\2\7\u00a2\3\2\2\2\t\u00a7\3\2\2\2\13")
        buf.write("\u00ab\3\2\2\2\r\u00b2\3\2\2\2\17\u00b7\3\2\2\2\21\u00bc")
        buf.write("\3\2\2\2\23\u00c3\3\2\2\2\25\u00cd\3\2\2\2\27\u00d1\3")
        buf.write("\2\2\2\31\u00d8\3\2\2\2\33\u00dc\3\2\2\2\35\u00e2\3\2")
        buf.write("\2\2\37\u00ea\3\2\2\2!\u00f0\3\2\2\2#\u00f4\3\2\2\2%\u00fd")
        buf.write("\3\2\2\2\'\u0103\3\2\2\2)\u0109\3\2\2\2+\u010d\3\2\2\2")
        buf.write("-\u0112\3\2\2\2/\u0118\3\2\2\2\61\u0124\3\2\2\2\63\u012d")
        buf.write("\3\2\2\2\65\u0133\3\2\2\2\67\u0135\3\2\2\29\u0137\3\2")
        buf.write("\2\2;\u0139\3\2\2\2=\u013b\3\2\2\2?\u013d\3\2\2\2A\u0140")
        buf.write("\3\2\2\2C\u0143\3\2\2\2E\u0146\3\2\2\2G\u0149\3\2\2\2")
        buf.write("I\u014b\3\2\2\2K\u014d\3\2\2\2M\u0150\3\2\2\2O\u0153\3")
        buf.write("\2\2\2Q\u0155\3\2\2\2S\u0158\3\2\2\2U\u015b\3\2\2\2W\u015e")
        buf.write("\3\2\2\2Y\u0161\3\2\2\2[\u0164\3\2\2\2]\u0167\3\2\2\2")
        buf.write("_\u0169\3\2\2\2a\u0171\3\2\2\2c\u0173\3\2\2\2e\u0175\3")
        buf.write("\2\2\2g\u0177\3\2\2\2i\u0179\3\2\2\2k\u017b\3\2\2\2m\u017d")
        buf.write("\3\2\2\2o\u017f\3\2\2\2q\u0181\3\2\2\2s\u0183\3\2\2\2")
        buf.write("u\u018c\3\2\2\2w\u0198\3\2\2\2y\u01a1\3\2\2\2{\u01aa\3")
        buf.write("\2\2\2}\u01b3\3\2\2\2\177\u01b5\3\2\2\2\u0081\u01b7\3")
        buf.write("\2\2\2\u0083\u01b9\3\2\2\2\u0085\u01e1\3\2\2\2\u0087\u01eb")
        buf.write("\3\2\2\2\u0089\u01ed\3\2\2\2\u008b\u0204\3\2\2\2\u008d")
        buf.write("\u0206\3\2\2\2\u008f\u020a\3\2\2\2\u0091\u0215\3\2\2\2")
        buf.write("\u0093\u0225\3\2\2\2\u0095\u022b\3\2\2\2\u0097\u022e\3")
        buf.write("\2\2\2\u0099\u023e\3\2\2\2\u009b\u0240\3\2\2\2\u009d\u009e")
        buf.write("\7<\2\2\u009e\4\3\2\2\2\u009f\u00a0\7k\2\2\u00a0\u00a1")
        buf.write("\7h\2\2\u00a1\6\3\2\2\2\u00a2\u00a3\7g\2\2\u00a3\u00a4")
        buf.write("\7n\2\2\u00a4\u00a5\7u\2\2\u00a5\u00a6\7g\2\2\u00a6\b")
        buf.write("\3\2\2\2\u00a7\u00a8\7h\2\2\u00a8\u00a9\7q\2\2\u00a9\u00aa")
        buf.write("\7t\2\2\u00aa\n\3\2\2\2\u00ab\u00ac\7t\2\2\u00ac\u00ad")
        buf.write("\7g\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af\7w\2\2\u00af\u00b0")
        buf.write("\7t\2\2\u00b0\u00b1\7p\2\2\u00b1\f\3\2\2\2\u00b2\u00b3")
        buf.write("\7h\2\2\u00b3\u00b4\7w\2\2\u00b4\u00b5\7p\2\2\u00b5\u00b6")
        buf.write("\7e\2\2\u00b6\16\3\2\2\2\u00b7\u00b8\7v\2\2\u00b8\u00b9")
        buf.write("\7{\2\2\u00b9\u00ba\7r\2\2\u00ba\u00bb\7g\2\2\u00bb\20")
        buf.write("\3\2\2\2\u00bc\u00bd\7u\2\2\u00bd\u00be\7v\2\2\u00be\u00bf")
        buf.write("\7t\2\2\u00bf\u00c0\7w\2\2\u00c0\u00c1\7e\2\2\u00c1\u00c2")
        buf.write("\7v\2\2\u00c2\22\3\2\2\2\u00c3\u00c4\7k\2\2\u00c4\u00c5")
        buf.write("\7p\2\2\u00c5\u00c6\7v\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8")
        buf.write("\7t\2\2\u00c8\u00c9\7h\2\2\u00c9\u00ca\7c\2\2\u00ca\u00cb")
        buf.write("\7e\2\2\u00cb\u00cc\7g\2\2\u00cc\24\3\2\2\2\u00cd\u00ce")
        buf.write("\7u\2\2\u00ce\u00cf\7v\2\2\u00cf\u00d0\7t\2\2\u00d0\26")
        buf.write("\3\2\2\2\u00d1\u00d2\7u\2\2\u00d2\u00d3\7v\2\2\u00d3\u00d4")
        buf.write("\7t\2\2\u00d4\u00d5\7k\2\2\u00d5\u00d6\7p\2\2\u00d6\u00d7")
        buf.write("\7i\2\2\u00d7\30\3\2\2\2\u00d8\u00d9\7k\2\2\u00d9\u00da")
        buf.write("\7p\2\2\u00da\u00db\7v\2\2\u00db\32\3\2\2\2\u00dc\u00dd")
        buf.write("\7h\2\2\u00dd\u00de\7n\2\2\u00de\u00df\7q\2\2\u00df\u00e0")
        buf.write("\7c\2\2\u00e0\u00e1\7v\2\2\u00e1\34\3\2\2\2\u00e2\u00e3")
        buf.write("\7d\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5\7q\2\2\u00e5\u00e6")
        buf.write("\7n\2\2\u00e6\u00e7\7g\2\2\u00e7\u00e8\7c\2\2\u00e8\u00e9")
        buf.write("\7p\2\2\u00e9\36\3\2\2\2\u00ea\u00eb\7e\2\2\u00eb\u00ec")
        buf.write("\7q\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee\7u\2\2\u00ee\u00ef")
        buf.write("\7v\2\2\u00ef \3\2\2\2\u00f0\u00f1\7x\2\2\u00f1\u00f2")
        buf.write("\7c\2\2\u00f2\u00f3\7t\2\2\u00f3\"\3\2\2\2\u00f4\u00f5")
        buf.write("\7e\2\2\u00f5\u00f6\7q\2\2\u00f6\u00f7\7p\2\2\u00f7\u00f8")
        buf.write("\7v\2\2\u00f8\u00f9\7k\2\2\u00f9\u00fa\7p\2\2\u00fa\u00fb")
        buf.write("\7w\2\2\u00fb\u00fc\7g\2\2\u00fc$\3\2\2\2\u00fd\u00fe")
        buf.write("\7d\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100\7g\2\2\u0100\u0101")
        buf.write("\7c\2\2\u0101\u0102\7m\2\2\u0102&\3\2\2\2\u0103\u0104")
        buf.write("\7t\2\2\u0104\u0105\7c\2\2\u0105\u0106\7p\2\2\u0106\u0107")
        buf.write("\7i\2\2\u0107\u0108\7g\2\2\u0108(\3\2\2\2\u0109\u010a")
        buf.write("\7p\2\2\u010a\u010b\7k\2\2\u010b\u010c\7n\2\2\u010c*\3")
        buf.write("\2\2\2\u010d\u010e\7v\2\2\u010e\u010f\7t\2\2\u010f\u0110")
        buf.write("\7w\2\2\u0110\u0111\7g\2\2\u0111,\3\2\2\2\u0112\u0113")
        buf.write("\7h\2\2\u0113\u0114\7c\2\2\u0114\u0115\7n\2\2\u0115\u0116")
        buf.write("\7u\2\2\u0116\u0117\7g\2\2\u0117.\3\2\2\2\u0118\u0119")
        buf.write("\7R\2\2\u0119\u011a\7w\2\2\u011a\u011b\7v\2\2\u011b\u011c")
        buf.write("\7U\2\2\u011c\u011d\7v\2\2\u011d\u011e\7t\2\2\u011e\u011f")
        buf.write("\7k\2\2\u011f\u0120\7p\2\2\u0120\u0121\7i\2\2\u0121\u0122")
        buf.write("\7N\2\2\u0122\u0123\7p\2\2\u0123\60\3\2\2\2\u0124\u0125")
        buf.write("\7R\2\2\u0125\u0126\7w\2\2\u0126\u0127\7v\2\2\u0127\u0128")
        buf.write("\7K\2\2\u0128\u0129\7p\2\2\u0129\u012a\7v\2\2\u012a\u012b")
        buf.write("\7N\2\2\u012b\u012c\7p\2\2\u012c\62\3\2\2\2\u012d\u012e")
        buf.write("\7c\2\2\u012e\u012f\7t\2\2\u012f\u0130\7t\2\2\u0130\u0131")
        buf.write("\7c\2\2\u0131\u0132\7{\2\2\u0132\64\3\2\2\2\u0133\u0134")
        buf.write("\7-\2\2\u0134\66\3\2\2\2\u0135\u0136\7/\2\2\u01368\3\2")
        buf.write("\2\2\u0137\u0138\7,\2\2\u0138:\3\2\2\2\u0139\u013a\7\61")
        buf.write("\2\2\u013a<\3\2\2\2\u013b\u013c\7\'\2\2\u013c>\3\2\2\2")
        buf.write("\u013d\u013e\7?\2\2\u013e\u013f\7?\2\2\u013f@\3\2\2\2")
        buf.write("\u0140\u0141\7#\2\2\u0141\u0142\7?\2\2\u0142B\3\2\2\2")
        buf.write("\u0143\u0144\7>\2\2\u0144\u0145\7?\2\2\u0145D\3\2\2\2")
        buf.write("\u0146\u0147\7@\2\2\u0147\u0148\7?\2\2\u0148F\3\2\2\2")
        buf.write("\u0149\u014a\7>\2\2\u014aH\3\2\2\2\u014b\u014c\7@\2\2")
        buf.write("\u014cJ\3\2\2\2\u014d\u014e\7(\2\2\u014e\u014f\7(\2\2")
        buf.write("\u014fL\3\2\2\2\u0150\u0151\7~\2\2\u0151\u0152\7~\2\2")
        buf.write("\u0152N\3\2\2\2\u0153\u0154\7#\2\2\u0154P\3\2\2\2\u0155")
        buf.write("\u0156\7-\2\2\u0156\u0157\7?\2\2\u0157R\3\2\2\2\u0158")
        buf.write("\u0159\7/\2\2\u0159\u015a\7?\2\2\u015aT\3\2\2\2\u015b")
        buf.write("\u015c\7,\2\2\u015c\u015d\7?\2\2\u015dV\3\2\2\2\u015e")
        buf.write("\u015f\7\61\2\2\u015f\u0160\7?\2\2\u0160X\3\2\2\2\u0161")
        buf.write("\u0162\7\'\2\2\u0162\u0163\7?\2\2\u0163Z\3\2\2\2\u0164")
        buf.write("\u0165\7<\2\2\u0165\u0166\7?\2\2\u0166\\\3\2\2\2\u0167")
        buf.write("\u0168\7?\2\2\u0168^\3\2\2\2\u0169\u016a\7\60\2\2\u016a")
        buf.write("`\3\2\2\2\u016b\u0172\5[.\2\u016c\u0172\5Q)\2\u016d\u0172")
        buf.write("\5S*\2\u016e\u0172\5U+\2\u016f\u0172\5W,\2\u0170\u0172")
        buf.write("\5Y-\2\u0171\u016b\3\2\2\2\u0171\u016c\3\2\2\2\u0171\u016d")
        buf.write("\3\2\2\2\u0171\u016e\3\2\2\2\u0171\u016f\3\2\2\2\u0171")
        buf.write("\u0170\3\2\2\2\u0172b\3\2\2\2\u0173\u0174\7*\2\2\u0174")
        buf.write("d\3\2\2\2\u0175\u0176\7+\2\2\u0176f\3\2\2\2\u0177\u0178")
        buf.write("\7}\2\2\u0178h\3\2\2\2\u0179\u017a\7\177\2\2\u017aj\3")
        buf.write("\2\2\2\u017b\u017c\7]\2\2\u017cl\3\2\2\2\u017d\u017e\7")
        buf.write("_\2\2\u017en\3\2\2\2\u017f\u0180\7.\2\2\u0180p\3\2\2\2")
        buf.write("\u0181\u0182\7=\2\2\u0182r\3\2\2\2\u0183\u0187\t\2\2\2")
        buf.write("\u0184\u0186\t\3\2\2\u0185\u0184\3\2\2\2\u0186\u0189\3")
        buf.write("\2\2\2\u0187\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188t")
        buf.write("\3\2\2\2\u0189\u0187\3\2\2\2\u018a\u018d\5\67\34\2\u018b")
        buf.write("\u018d\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018b\3\2\2\2")
        buf.write("\u018d\u0196\3\2\2\2\u018e\u0197\7\62\2\2\u018f\u0193")
        buf.write("\t\4\2\2\u0190\u0192\t\5\2\2\u0191\u0190\3\2\2\2\u0192")
        buf.write("\u0195\3\2\2\2\u0193\u0191\3\2\2\2\u0193\u0194\3\2\2\2")
        buf.write("\u0194\u0197\3\2\2\2\u0195\u0193\3\2\2\2\u0196\u018e\3")
        buf.write("\2\2\2\u0196\u018f\3\2\2\2\u0197v\3\2\2\2\u0198\u0199")
        buf.write("\7\62\2\2\u0199\u019b\t\6\2\2\u019a\u019c\5\u0081A\2\u019b")
        buf.write("\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019b\3\2\2\2")
        buf.write("\u019d\u019e\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a0\b")
        buf.write("<\2\2\u01a0x\3\2\2\2\u01a1\u01a2\7\62\2\2\u01a2\u01a4")
        buf.write("\t\7\2\2\u01a3\u01a5\5\177@\2\u01a4\u01a3\3\2\2\2\u01a5")
        buf.write("\u01a6\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2")
        buf.write("\u01a7\u01a8\3\2\2\2\u01a8\u01a9\b=\3\2\u01a9z\3\2\2\2")
        buf.write("\u01aa\u01ab\7\62\2\2\u01ab\u01ad\t\b\2\2\u01ac\u01ae")
        buf.write("\5}?\2\u01ad\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01ad")
        buf.write("\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1")
        buf.write("\u01b2\b>\4\2\u01b2|\3\2\2\2\u01b3\u01b4\t\t\2\2\u01b4")
        buf.write("~\3\2\2\2\u01b5\u01b6\t\n\2\2\u01b6\u0080\3\2\2\2\u01b7")
        buf.write("\u01b8\t\13\2\2\u01b8\u0082\3\2\2\2\u01b9\u01bb\t\f\2")
        buf.write("\2\u01ba\u01bc\t\r\2\2\u01bb\u01ba\3\2\2\2\u01bb\u01bc")
        buf.write("\3\2\2\2\u01bc\u01c5\3\2\2\2\u01bd\u01c6\7\62\2\2\u01be")
        buf.write("\u01c2\t\4\2\2\u01bf\u01c1\t\5\2\2\u01c0\u01bf\3\2\2\2")
        buf.write("\u01c1\u01c4\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c3\3")
        buf.write("\2\2\2\u01c3\u01c6\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c5\u01bd")
        buf.write("\3\2\2\2\u01c5\u01be\3\2\2\2\u01c6\u0084\3\2\2\2\u01c7")
        buf.write("\u01c8\5\u0087D\2\u01c8\u01cc\7\60\2\2\u01c9\u01cb\t\5")
        buf.write("\2\2\u01ca\u01c9\3\2\2\2\u01cb\u01ce\3\2\2\2\u01cc\u01ca")
        buf.write("\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01d0\3\2\2\2\u01ce")
        buf.write("\u01cc\3\2\2\2\u01cf\u01d1\5\u0083B\2\u01d0\u01cf\3\2")
        buf.write("\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01e2\3\2\2\2\u01d2\u01d4")
        buf.write("\7\60\2\2\u01d3\u01d5\t\5\2\2\u01d4\u01d3\3\2\2\2\u01d5")
        buf.write("\u01d6\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2")
        buf.write("\u01d7\u01d9\3\2\2\2\u01d8\u01da\5\u0083B\2\u01d9\u01d8")
        buf.write("\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01e2\3\2\2\2\u01db")
        buf.write("\u01dd\t\5\2\2\u01dc\u01db\3\2\2\2\u01dd\u01de\3\2\2\2")
        buf.write("\u01de\u01dc\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01e0\3")
        buf.write("\2\2\2\u01e0\u01e2\5\u0083B\2\u01e1\u01c7\3\2\2\2\u01e1")
        buf.write("\u01d2\3\2\2\2\u01e1\u01dc\3\2\2\2\u01e2\u0086\3\2\2\2")
        buf.write("\u01e3\u01ec\7\62\2\2\u01e4\u01e8\t\4\2\2\u01e5\u01e7")
        buf.write("\t\5\2\2\u01e6\u01e5\3\2\2\2\u01e7\u01ea\3\2\2\2\u01e8")
        buf.write("\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01ec\3\2\2\2")
        buf.write("\u01ea\u01e8\3\2\2\2\u01eb\u01e3\3\2\2\2\u01eb\u01e4\3")
        buf.write("\2\2\2\u01ec\u0088\3\2\2\2\u01ed\u01f5\7$\2\2\u01ee\u01f4")
        buf.write("\n\16\2\2\u01ef\u01f0\7^\2\2\u01f0\u01f4\t\17\2\2\u01f1")
        buf.write("\u01f2\7)\2\2\u01f2\u01f4\7$\2\2\u01f3\u01ee\3\2\2\2\u01f3")
        buf.write("\u01ef\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f4\u01f7\3\2\2\2")
        buf.write("\u01f5\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f8\3")
        buf.write("\2\2\2\u01f7\u01f5\3\2\2\2\u01f8\u01f9\7$\2\2\u01f9\u01fa")
        buf.write("\bE\5\2\u01fa\u008a\3\2\2\2\u01fb\u01fc\7v\2\2\u01fc\u01fd")
        buf.write("\7t\2\2\u01fd\u01fe\7w\2\2\u01fe\u0205\7g\2\2\u01ff\u0200")
        buf.write("\7h\2\2\u0200\u0201\7c\2\2\u0201\u0202\7n\2\2\u0202\u0203")
        buf.write("\7u\2\2\u0203\u0205\7g\2\2\u0204\u01fb\3\2\2\2\u0204\u01ff")
        buf.write("\3\2\2\2\u0205\u008c\3\2\2\2\u0206\u0207\7p\2\2\u0207")
        buf.write("\u0208\7k\2\2\u0208\u0209\7n\2\2\u0209\u008e\3\2\2\2\u020a")
        buf.write("\u020b\7\61\2\2\u020b\u020c\7\61\2\2\u020c\u0210\3\2\2")
        buf.write("\2\u020d\u020f\n\20\2\2\u020e\u020d\3\2\2\2\u020f\u0212")
        buf.write("\3\2\2\2\u0210\u020e\3\2\2\2\u0210\u0211\3\2\2\2\u0211")
        buf.write("\u0213\3\2\2\2\u0212\u0210\3\2\2\2\u0213\u0214\bH\6\2")
        buf.write("\u0214\u0090\3\2\2\2\u0215\u0216\7\61\2\2\u0216\u0217")
        buf.write("\7,\2\2\u0217\u021c\3\2\2\2\u0218\u021b\5\u0091I\2\u0219")
        buf.write("\u021b\13\2\2\2\u021a\u0218\3\2\2\2\u021a\u0219\3\2\2")
        buf.write("\2\u021b\u021e\3\2\2\2\u021c\u021d\3\2\2\2\u021c\u021a")
        buf.write("\3\2\2\2\u021d\u021f\3\2\2\2\u021e\u021c\3\2\2\2\u021f")
        buf.write("\u0220\7,\2\2\u0220\u0221\7\61\2\2\u0221\u0222\3\2\2\2")
        buf.write("\u0222\u0223\bI\6\2\u0223\u0092\3\2\2\2\u0224\u0226\t")
        buf.write("\21\2\2\u0225\u0224\3\2\2\2\u0226\u0227\3\2\2\2\u0227")
        buf.write("\u0225\3\2\2\2\u0227\u0228\3\2\2\2\u0228\u0229\3\2\2\2")
        buf.write("\u0229\u022a\bJ\6\2\u022a\u0094\3\2\2\2\u022b\u022c\13")
        buf.write("\2\2\2\u022c\u022d\bK\7\2\u022d\u0096\3\2\2\2\u022e\u0236")
        buf.write("\7$\2\2\u022f\u0235\n\16\2\2\u0230\u0231\7^\2\2\u0231")
        buf.write("\u0235\t\17\2\2\u0232\u0233\7)\2\2\u0233\u0235\7$\2\2")
        buf.write("\u0234\u022f\3\2\2\2\u0234\u0230\3\2\2\2\u0234\u0232\3")
        buf.write("\2\2\2\u0235\u0238\3\2\2\2\u0236\u0234\3\2\2\2\u0236\u0237")
        buf.write("\3\2\2\2\u0237\u023a\3\2\2\2\u0238\u0236\3\2\2\2\u0239")
        buf.write("\u023b\t\22\2\2\u023a\u0239\3\2\2\2\u023b\u023c\3\2\2")
        buf.write("\2\u023c\u023d\bL\b\2\u023d\u0098\3\2\2\2\u023e\u023f")
        buf.write("\t\17\2\2\u023f\u009a\3\2\2\2\u0240\u0248\7$\2\2\u0241")
        buf.write("\u0247\n\16\2\2\u0242\u0243\7^\2\2\u0243\u0247\t\17\2")
        buf.write("\2\u0244\u0245\7)\2\2\u0245\u0247\7$\2\2\u0246\u0241\3")
        buf.write("\2\2\2\u0246\u0242\3\2\2\2\u0246\u0244\3\2\2\2\u0247\u024a")
        buf.write("\3\2\2\2\u0248\u0246\3\2\2\2\u0248\u0249\3\2\2\2\u0249")
        buf.write("\u024b\3\2\2\2\u024a\u0248\3\2\2\2\u024b\u024c\7^\2\2")
        buf.write("\u024c\u024d\n\23\2\2\u024d\u024e\bN\t\2\u024e\u009c\3")
        buf.write("\2\2\2\"\2\u0171\u0187\u018c\u0193\u0196\u019d\u01a6\u01af")
        buf.write("\u01bb\u01c2\u01c5\u01cc\u01d0\u01d6\u01d9\u01de\u01e1")
        buf.write("\u01e8\u01eb\u01f3\u01f5\u0204\u0210\u021a\u021c\u0227")
        buf.write("\u0234\u0236\u023a\u0246\u0248\n\3<\2\3=\3\3>\4\3E\5\b")
        buf.write("\2\2\3K\6\3L\7\3N\b")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    IF = 2
    ELSE = 3
    FOR = 4
    RETURN = 5
    FUNC = 6
    TYPE = 7
    STRUCT = 8
    INTERFACE = 9
    STR = 10
    STRING = 11
    INT = 12
    FLOAT = 13
    BOOLEAN = 14
    CONST = 15
    VAR = 16
    CONTINUE = 17
    BREAK = 18
    RANGE = 19
    NIL = 20
    TRUE = 21
    FALSE = 22
    PUTSTRINGLN = 23
    PUTINTLN = 24
    ARRAY = 25
    PLUS = 26
    MINUS = 27
    MUL = 28
    DIV = 29
    MOD = 30
    EQUAL = 31
    NOTEQUAL = 32
    LE = 33
    GE = 34
    LT = 35
    GT = 36
    AND = 37
    OR = 38
    NOT = 39
    PLUSEQ = 40
    MINUSEQ = 41
    MULEQ = 42
    DIVEQ = 43
    MODEQ = 44
    COLONEQ = 45
    ASSIGN = 46
    DOT = 47
    ASSIGN_OPERATOR = 48
    LPAREN = 49
    RPAREN = 50
    LBRACE = 51
    RBRACE = 52
    LBRACK = 53
    RBRACK = 54
    COMMA = 55
    SEMI = 56
    ID = 57
    DECIMAL_LIT = 58
    BINARY_LIT = 59
    OCT_LIT = 60
    HEXA_LIT = 61
    FLOAT_LIT = 62
    STRING_LIT = 63
    BOOLEAN_LIT = 64
    NIL_LIT = 65
    SINGLE_LINE_COMMENT = 66
    MULTI_LINE_COMMENT = 67
    WS = 68
    ERROR_CHAR = 69
    UNCLOSE_STRING = 70
    VALID_ESCAPES = 71
    ILLEGAL_ESCAPE = 72

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", 
            "'struct'", "'interface'", "'str'", "'string'", "'int'", "'float'", 
            "'boolean'", "'const'", "'var'", "'continue'", "'break'", "'range'", 
            "'true'", "'false'", "'PutStringLn'", "'PutIntLn'", "'array'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'<='", "'>='", 
            "'<'", "'>'", "'&&'", "'||'", "'!'", "'+='", "'-='", "'*='", 
            "'/='", "'%='", "':='", "'='", "'.'", "'('", "')'", "'{'", "'}'", 
            "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STR", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", 
            "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "PUTSTRINGLN", 
            "PUTINTLN", "ARRAY", "PLUS", "MINUS", "MUL", "DIV", "MOD", "EQUAL", 
            "NOTEQUAL", "LE", "GE", "LT", "GT", "AND", "OR", "NOT", "PLUSEQ", 
            "MINUSEQ", "MULEQ", "DIVEQ", "MODEQ", "COLONEQ", "ASSIGN", "DOT", 
            "ASSIGN_OPERATOR", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
            "RBRACK", "COMMA", "SEMI", "ID", "DECIMAL_LIT", "BINARY_LIT", 
            "OCT_LIT", "HEXA_LIT", "FLOAT_LIT", "STRING_LIT", "BOOLEAN_LIT", 
            "NIL_LIT", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", "WS", 
            "ERROR_CHAR", "UNCLOSE_STRING", "VALID_ESCAPES", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", 
                  "STRUCT", "INTERFACE", "STR", "STRING", "INT", "FLOAT", 
                  "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                  "NIL", "TRUE", "FALSE", "PUTSTRINGLN", "PUTINTLN", "ARRAY", 
                  "PLUS", "MINUS", "MUL", "DIV", "MOD", "EQUAL", "NOTEQUAL", 
                  "LE", "GE", "LT", "GT", "AND", "OR", "NOT", "PLUSEQ", 
                  "MINUSEQ", "MULEQ", "DIVEQ", "MODEQ", "COLONEQ", "ASSIGN", 
                  "DOT", "ASSIGN_OPERATOR", "LPAREN", "RPAREN", "LBRACE", 
                  "RBRACE", "LBRACK", "RBRACK", "COMMA", "SEMI", "ID", "DECIMAL_LIT", 
                  "BINARY_LIT", "OCT_LIT", "HEXA_LIT", "HEX_DIGIT", "OCTAL_DIGIT", 
                  "BIN_DIGIT", "EXP", "FLOAT_LIT", "DECIMALS", "STRING_LIT", 
                  "BOOLEAN_LIT", "NIL_LIT", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "VALID_ESCAPES", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[58] = self.BINARY_LIT_action 
            actions[59] = self.OCT_LIT_action 
            actions[60] = self.HEXA_LIT_action 
            actions[67] = self.STRING_LIT_action 
            actions[73] = self.ERROR_CHAR_action 
            actions[74] = self.UNCLOSE_STRING_action 
            actions[76] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def BINARY_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             self.text = str(int(self.text, 2)) 
     

    def OCT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             self.text = str(int(self.text, 8)) 
     

    def HEXA_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             self.text = str(int(self.text, 16)) 
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
                    raise UncloseString(self.text[1:-2]) 
                elif (self.text[-1] == '\n'):
                    raise UncloseString(self.text[1:-1]) 
                else:
                    raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

                VAL_ESCAPES = ['n', 't', 'r', '"', '\\']
                for i in range(1, len(self.text)-1):
                    if self.text[i] == '\\' and self.text[i+1] not in VAL_ESCAPES:
                        raise IllegalEscape(self.text[1:i+2])

     


